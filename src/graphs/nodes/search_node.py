import json
import logging
from typing import List, Dict, Any
from langchain_core.runnables import RunnableConfig
from langgraph.runtime import Runtime
from coze_coding_utils.runtime_ctx.context import Context
from coze_coding_dev_sdk import SearchClient
from graphs.state import SearchNodeInput, SearchNodeOutput

logger = logging.getLogger(__name__)


def search_node(
    state: SearchNodeInput,
    config: RunnableConfig,
    runtime: Runtime[Context]
) -> SearchNodeOutput:
    """
    title: 网络搜索
    desc: 搜索指定代币的最新新闻、社交媒体情绪和市场动态
    integrations: web-search
    """
    ctx = runtime.context
    
    try:
        # 初始化搜索客户端
        client = SearchClient(ctx=ctx)
        
        # 构建搜索查询
        query = f"{state.token_name} token news twitter sentiment"
        
        logger.info(f"Searching for: {query}")
        
        # 执行搜索，包含AI摘要
        response = client.web_search_with_summary(
            query=query,
            count=10
        )
        
        # 提取搜索结果
        search_results: List[Dict[str, Any]] = []
        if response.web_items:
            for item in response.web_items:
                search_results.append({
                    "title": item.title,
                    "url": item.url,
                    "snippet": item.snippet,
                    "site_name": item.site_name,
                    "publish_time": item.publish_time,
                    "auth_info_des": item.auth_info_des
                })
        
        # 提取摘要
        summary = response.summary if response.summary else ""
        
        logger.info(f"Found {len(search_results)} results, summary length: {len(summary)}")
        
        return SearchNodeOutput(
            search_results=search_results,
            search_summary=summary
        )
        
    except Exception as e:
        logger.error(f"Search failed: {str(e)}", exc_info=True)
        # 返回空结果
        return SearchNodeOutput(
            search_results=[],
            search_summary=f"搜索失败: {str(e)}"
        )
