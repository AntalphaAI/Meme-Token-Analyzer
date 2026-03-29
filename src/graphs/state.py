from typing import List, Optional, Any, Dict
from pydantic import BaseModel, Field


# ========== Graph Input/Output ==========
class GraphInput(BaseModel):
    """工作流输入参数"""
    token_name: str = Field(..., description="代币名称，例如：PEPE 或 Dogecoin")


class GraphOutput(BaseModel):
    """工作流输出结果"""
    analysis_report: str = Field(..., description="深度分析报告")
    generated_image_url: str = Field(..., description="生成的代币冲月预测图URL")


# ========== Global State ==========
class GlobalState(BaseModel):
    """全局状态定义"""
    token_name: str = Field(default="", description="代币名称")
    search_results: List[Dict[str, Any]] = Field(default=[], description="搜索结果列表")
    search_summary: str = Field(default="", description="搜索结果摘要")
    cleaned_text: str = Field(default="", description="清洗后的文本")
    generated_image_url: str = Field(default="", description="生成的图片URL")
    analysis_report: str = Field(default="", description="暴富基因检测报告")


# ========== Node Input/Output Definitions ==========

# Search Node
class SearchNodeInput(BaseModel):
    """搜索节点输入"""
    token_name: str = Field(..., description="代币名称")


class SearchNodeOutput(BaseModel):
    """搜索节点输出"""
    search_results: List[Dict[str, Any]] = Field(default=[], description="搜索结果列表")
    search_summary: str = Field(default="", description="搜索结果AI摘要")


# Image Generation Node
class ImageGenNodeInput(BaseModel):
    """图片生成节点输入"""
    token_name: str = Field(..., description="代币名称")


class ImageGenNodeOutput(BaseModel):
    """图片生成节点输出"""
    generated_image_url: str = Field(..., description="生成的图片URL")


# Clean Data Node
class CleanDataNodeInput(BaseModel):
    """舆情清洗节点输入"""
    search_results: List[Dict[str, Any]] = Field(default=[], description="搜索结果列表")
    search_summary: str = Field(default="", description="搜索结果摘要")


class CleanDataNodeOutput(BaseModel):
    """舆情清洗节点输出"""
    cleaned_text: str = Field(..., description="清洗后的文本摘要")


# Analysis Node
class AnalysisNodeInput(BaseModel):
    """分析节点输入"""
    token_name: str = Field(..., description="代币名称")
    cleaned_text: str = Field(..., description="清洗后的舆情数据")
    generated_image_url: str = Field(..., description="生成的 Meme 预测图片URL")


class AnalysisNodeOutput(BaseModel):
    """分析节点输出"""
    analysis_report: str = Field(..., description="暴富基因检测报告")
