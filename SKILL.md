---
name: meme-token-analyzer
description: Meme Token 分析工作流，实现网络搜索、图片生成、数据清洗和多模态分析，输出"暴富基因"检测报告。当用户需要分析 Meme 币的舆情、生成预测图片、并输出专业的投资分析报告时，请使用此技能。支持多维度分析、智能检测和幽默专业的报告生成。
license: MIT
---

# Meme Token Analyzer Skill

This skill guides the implementation of an automated, multimodal Meme token analysis tool using LangGraph and coze-coding-dev-sdk, combining real-time sentiment search, AI-generated prediction images, and comprehensive wealth gene detection analysis.

## Overview

Meme Token Analyzer enables you to build applications that automatically analyze Meme tokens by:
- 🔍 **Searching** latest news, social media sentiment, and market trends with time range filtering
- 🎨 **Generating** "Moonshot" prediction images for tokens
- 🧹 **Cleaning** search results into LLM-friendly summaries
- 🤖 **Analyzing** sentiment data and visual elements with multimodal AI
- 💎 **Rating** tokens with a four-tier wealth gene system (Diamond Hand, Moonshot, Paper Hand, Shitcoin)

## Supported Languages

This skill supports Python SDK.

**Mandatory (required): When you use this skill, you MUST immediately open and read the SDK guide for the language you are implementing in for installation, client initialization, and usage examples, and then follow it exactly. Do not guess APIs, do not proceed before reading the corresponding SDK guide.**

- **Python SDK**: Read first: [python/README.md](python/README.md)

## Key Features

### 🔍 Web Search
- Searches latest news, social media sentiment, and market trends
- Time range filter (1 month) for fresh data
- AI-generated summary of search results

### 🎨 Image Generation
- Creates "Moonshot" prediction images for tokens
- High-quality 2K resolution images
- Dynamic, cinematic visual style

### 🧹 Data Cleaning
- Condenses search results into LLM-friendly summaries
- Date freshness validation
- Removes irrelevant information

### 🤖 AI Analysis
- Multimodal analysis combining sentiment data and visual elements
- Four-dimensional analysis framework:
  1. 🎯 **Narrative Magic Analysis** - Name and concept memorability
  2. 📢 **Community Hype Ability Prediction** - Community activity and shilling intensity
  3. 🎨 **Visual Gene Detection** - Meme image's viral potential
  4. 🏆 **Wealth Gene Rating** - Final verdict

### 💎 Wealth Gene Rating System
- 🌟 **Diamond Hand** - 10000x potential
- 🌙 **Moonshot** - 100x expected
- 🗑️ **Paper Hand** - Likely a rug
- 💩 **Shitcoin** - Stay away

### 🧠 Smart Detection
- Automatically detects major coins (BTC/ETH/SOL) with cross-border scan perspective
- Handles missing data gracefully without fabrication
- Identifies irrelevant search results with appropriate warnings

## Workflow Architecture

```
START
  ├── search (Web Search) ──> clean_data (Data Cleaning) ──┐
  └── image_gen (Image Generation) ────────────────────────┤
                                                            ├─> analysis (Wealth Gene Detection) ──> END
```

**Parallel Execution**: Search and image generation run in parallel for efficiency.

**Convergence**: Analysis waits for both data cleaning and image generation to complete.

## Input/Output

**Input**:
- `token_name` (String): Token name, e.g., "PEPE", "SHIB", "Dogecoin"

**Output**:
- `analysis_report` (String): Humorous and professional wealth gene detection report
- `generated_image_url` (String): Generated prediction image URL

## Prerequisites

The following packages are already installed:
- `coze-coding-dev-sdk`: For LLM, search, and image generation clients
- `langgraph`: For workflow orchestration
- `langchain-core`: For message types
- `pydantic`: For data models

## Quick Start

```python
from langgraph.graph import StateGraph, END, START
from coze_coding_dev_sdk import LLMClient, SearchClient, ImageGenerationClient

# Define your nodes
def search_node(state, config, runtime):
    client = SearchClient(ctx=runtime.context)
    response = client.search(query=f"{state.token_name} token news", need_summary=True)
    return {"search_results": response.web_items, "search_summary": response.summary}

# Build your workflow
builder = StateGraph(GlobalState, input_schema=GraphInput, output_schema=GraphOutput)
builder.add_node("search", search_node)
builder.add_edge(START, "search")
# ... add more nodes and edges
main_graph = builder.compile()
```

For complete implementation details, see [python/README.md](python/README.md).

## Use Cases

### Analyze a Single Token
```python
result = main_graph.invoke({"token_name": "PEPE"})
print(result["analysis_report"])
```

### Batch Analysis
```python
tokens = ["PEPE", "SHIB", "DOGE"]
for token in tokens:
    result = main_graph.invoke({"token_name": token})
    print(f"{token}: {result['analysis_report'][:100]}...")
```

### Integration with Trading Bots
```python
def analyze_before_trade(token_name):
    result = main_graph.invoke({"token_name": token_name})
    report = result["analysis_report"]
    
    if "Diamond Hand" in report:
        return "BUY", result["generated_image_url"]
    elif "Shitcoin" in report:
        return "AVOID", None
    else:
        return "RESEARCH", result["generated_image_url"]
```

## Best Practices

1. **Use Time Range Filtering**: Always filter search results by time range for fresh data
2. **Handle Missing Data**: Gracefully handle cases where no search results are found
3. **Multimodal Analysis**: Combine text and image analysis for comprehensive insights
4. **Error Handling**: Implement robust error handling for API calls
5. **Rate Limiting**: Respect API rate limits when analyzing multiple tokens

## Limitations

- Search results depend on public web data availability
- Image generation quality varies based on token name clarity
- Analysis is for educational purposes only, not financial advice
- API rate limits may apply for high-volume usage

## Security Considerations

- Never expose API keys in client-side code
- All LLM and search calls must be made from backend code
- Sanitize token names before search queries
- Validate and sanitize all user inputs

## Troubleshooting

**Issue**: Search returns no results
- **Solution**: Check if token name is correct and publicly known
- **Solution**: Verify network connectivity and API status

**Issue**: Image generation fails
- **Solution**: Check if prompt is appropriate and follows content guidelines
- **Solution**: Verify ImageGenerationClient initialization and API status

**Issue**: Analysis returns empty report
- **Solution**: Check if sentiment_data and image_url are properly passed
- **Solution**: Verify LLM model availability and configuration

## Support

For detailed implementation guide:
- Python SDK: [python/README.md](python/README.md)

For skill-related issues:
- Check the troubleshooting section
- Review the complete code examples in python/README.md
- Ensure all prerequisites are met
