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
    title: Sentiment Cleaning
    desc: Clean Google search results into a concise summary for LLM analysis
    """
    ctx = runtime.context
    
    try:
        # Extract search result titles and snippets (top 5 most relevant)
        snippets: List[str] = []
        
        if state.search_results:
            for item in state.search_results[:5]:
                title = item.get("title", "")
                snippet = item.get("snippet", "")
                if title or snippet:
                    snippets.append(f"【{title}】\n{snippet}")
        
        # Handle no results case
        if not snippets:
            logger.warning("No search results found")
            return CleanDataNodeOutput(
                cleaned_text=f"Unable to find latest trending narratives for this token online."
            )
        
        # Add AI summary if available
        if state.search_summary:
            cleaned_text = f"=== AI Summary ===\n{state.search_summary}\n\n=== Detailed Information ===\n\n" + "\n---\n".join(snippets)
        else:
            cleaned_text = "\n---\n".join(snippets)
        
        logger.info(f"Cleaned {len(snippets)} search results, total length: {len(cleaned_text)} chars")
        
        return CleanDataNodeOutput(cleaned_text=cleaned_text)
        
    except Exception as e:
        logger.error(f"Data cleaning failed: {str(e)}", exc_info=True)
        return CleanDataNodeOutput(cleaned_text=f"Data cleaning failed: {str(e)}")
