import os
import json
import logging
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from coze_coding_dev_sdk import LLMClient
from langchain_core.messages import SystemMessage, HumanMessage
from jinja2 import Template
from graphs.state import AnalysisNodeInput, AnalysisNodeOutput

logger = logging.getLogger(__name__)


def analysis_node(
    state: AnalysisNodeInput,
    config: RunnableConfig,
    runtime: Runtime[Context]
) -> AnalysisNodeOutput:
    """
    title: 深度分析
    desc: 使用多模态大模型分析代币舆情数据和预测图片，生成综合报告
    integrations: llm
    """
    ctx = runtime.context
    
    try:
        # 读取配置文件
        cfg_file = os.path.join(os.getenv("COZE_WORKSPACE_PATH"), config['metadata']['llm_cfg'])
        with open(cfg_file, 'r', encoding='utf-8') as fd:
            _cfg = json.load(fd)
        
        llm_config = _cfg.get("config", {})
        sp = _cfg.get("sp", "")
        up = _cfg.get("up", "")
        
        # 渲染用户提示词
        up_tpl = Template(up)
        user_prompt_content = up_tpl.render({
            "token_name": state.token_name,
            "cleaned_text": state.cleaned_text
        })
        
        logger.info(f"Analysis for token: {state.token_name}")
        
        # 初始化LLM客户端
        client = LLMClient(ctx=ctx)
        
        # 构建多模态消息（文本 + 图片）
        messages = [
            SystemMessage(content=sp),
            HumanMessage(content=[
                {
                    "type": "text",
                    "text": user_prompt_content
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": state.generated_image_url
                    }
                }
            ])
        ]
        
        # 调用模型
        response = client.invoke(
            messages=messages,
            model=llm_config.get("model", "doubao-seed-1-6-vision-250815"),
            temperature=llm_config.get("temperature", 0.7),
            max_completion_tokens=llm_config.get("max_completion_tokens", 4096)
        )
        
        # 提取响应内容
        if isinstance(response.content, str):
            analysis_report = response.content
        elif isinstance(response.content, list):
            # 处理多模态响应
            text_parts = []
            for item in response.content:
                if isinstance(item, dict) and item.get("type") == "text":
                    text_parts.append(item.get("text", ""))
            analysis_report = "\n".join(text_parts)
        else:
            analysis_report = str(response.content)
        
        logger.info(f"Analysis report generated, length: {len(analysis_report)}")
        
        return AnalysisNodeOutput(analysis_report=analysis_report)
        
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}", exc_info=True)
        raise
