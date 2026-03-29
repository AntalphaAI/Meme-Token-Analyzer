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
    desc: 将 Google 搜索结果精简为 Claude 能读懂的摘要
    """
    ctx = runtime.context
    
    try:
        # 提取搜索结果的标题和摘要（只取前5条最相关的）
        snippets: List[str] = []
        
        if state.search_results:
            for item in state.search_results[:5]:
                title = item.get("title", "")
                snippet = item.get("snippet", "")
                if title or snippet:
                    snippets.append(f"【{title}】\n{snippet}")
        
        # 如果没有搜到结果
        if not snippets:
            logger.warning("No search results found")
            return CleanDataNodeOutput(
                cleaned_text=f"未能在网上找到关于该代币的最新爆点叙事。"
            )
        
        # 如果有AI摘要，优先添加
        if state.search_summary:
            cleaned_text = f"=== AI 摘要 ===\n{state.search_summary}\n\n=== 详细信息 ===\n\n" + "\n---\n".join(snippets)
        else:
            cleaned_text = "\n---\n".join(snippets)
        
        logger.info(f"Cleaned {len(snippets)} search results, total length: {len(cleaned_text)} chars")
        
        return CleanDataNodeOutput(cleaned_text=cleaned_text)
        
    except Exception as e:
        logger.error(f"Data cleaning failed: {str(e)}", exc_info=True)
        return CleanDataNodeOutput(cleaned_text=f"数据清洗失败: {str(e)}")
