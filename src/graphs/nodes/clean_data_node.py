import logging
from typing import List, Dict, Any
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from graphs.state import CleanDataNodeInput, CleanDataNodeOutput

logger = logging.getLogger(__name__)


def clean_data_node(
    state: CleanDataNodeInput,
    config: RunnableConfig,
    runtime: Runtime[Context]
) -> CleanDataNodeOutput:
    """
    title: 舆情清洗
    desc: 将搜索结果清洗整理为结构化的摘要文本
    """
    ctx = runtime.context
    
    try:
        # 构建清洗后的文本
        text_parts: List[str] = []
        
        # 1. 添加AI摘要（如果有）
        if state.search_summary:
            text_parts.append("=== 搜索摘要 ===")
            text_parts.append(state.search_summary)
            text_parts.append("")
        
        # 2. 整理搜索结果
        if state.search_results:
            text_parts.append("=== 搜索结果详情 ===")
            for i, result in enumerate(state.search_results, 1):
                title = result.get("title", "无标题")
                snippet = result.get("snippet", "")
                site_name = result.get("site_name", "")
                publish_time = result.get("publish_time", "")
                auth_info = result.get("auth_info_des", "")
                
                text_parts.append(f"\n【{i}】{title}")
                if site_name:
                    text_parts.append(f"来源: {site_name}")
                if publish_time:
                    text_parts.append(f"时间: {publish_time}")
                if auth_info:
                    text_parts.append(f"权威性: {auth_info}")
                if snippet:
                    text_parts.append(f"摘要: {snippet}")
        
        # 3. 合并为完整文本
        cleaned_text = "\n".join(text_parts)
        
        logger.info(f"Cleaned text length: {len(cleaned_text)} chars")
        
        return CleanDataNodeOutput(cleaned_text=cleaned_text)
        
    except Exception as e:
        logger.error(f"Data cleaning failed: {str(e)}", exc_info=True)
        # 返回空文本
        return CleanDataNodeOutput(cleaned_text=f"数据清洗失败: {str(e)}")
