from langgraph.graph import StateGraph, END, START
from graphs.state import (
    GlobalState,
    GraphInput,
    GraphOutput
)
from graphs.nodes.search_node import search_node
from graphs.nodes.image_gen_node import image_gen_node
from graphs.nodes.clean_data_node import clean_data_node
from graphs.nodes.analysis_node import analysis_node

# 创建状态图
builder = StateGraph(
    GlobalState,
    input_schema=GraphInput,
    output_schema=GraphOutput
)

# ========== 添加节点 ==========

# 搜索节点
builder.add_node("search", search_node)

# 图片生成节点
builder.add_node("image_gen", image_gen_node)

# 数据清洗节点
builder.add_node("clean_data", clean_data_node)

# 分析节点
builder.add_node(
    "analysis",
    analysis_node,
    metadata={
        "type": "agent",
        "llm_cfg": "config/analysis_llm_cfg.json"
    }
)

# ========== 设置边 ==========

# 从 START 并行启动搜索和图片生成节点
builder.add_edge(START, "search")
builder.add_edge(START, "image_gen")

# 搜索完成后进行数据清洗
builder.add_edge("search", "clean_data")

# 数据清洗和图片生成完成后汇聚到分析节点
builder.add_edge(["clean_data", "image_gen"], "analysis")

# 分析完成后结束
builder.add_edge("analysis", END)

# ========== 编译图 ==========
main_graph = builder.compile()
