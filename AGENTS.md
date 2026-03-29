# Meme Token Analyzer 工作流

## 项目概述
- **名称**: Meme_Token_Analyzer
- **功能**: 分析 Meme Token 的网络舆情,生成预测图片,并输出综合分析报告

## 节点清单

| 节点名 | 文件位置 | 类型 | 功能描述 | 分支逻辑 | 配置文件 |
|-------|---------|------|---------|---------|---------|
| search | `nodes/search_node.py` | task | 网络搜索代币新闻和社交媒体情绪 | - | - |
| image_gen | `nodes/image_gen_node.py` | task | 生成代币冲向月球的预测图片 | - | - |
| clean_data | `nodes/clean_data_node.py` | task | 清洗搜索结果为结构化文本 | - | - |
| analysis | `nodes/analysis_node.py` | agent | 多模态分析舆情数据和图片 | - | `config/analysis_llm_cfg.json` |

**类型说明**: task(task节点) / agent(大模型) / condition(条件分支) / looparray(列表循环) / loopcond(条件循环)

## 子图清单
无子图

## 技能使用
- 节点 `search` 使用技能 `web-search` 进行网络搜索
- 节点 `image_gen` 使用技能 `image-generation` 生成图片
- 节点 `analysis` 使用技能 `llm` 进行多模态分析

## 工作流结构
```
START
  ├── search (网络搜索) ──> clean_data (数据清洗) ──┐
  └── image_gen (图片生成) ────────────────────────┤
                                                    ├─> analysis (深度分析) ──> END
```

## 输入输出
- **输入**: token_name (String) - 代币名称,如 "PEPE" 或 "Dogecoin"
- **输出**: 
  - analysis_report (String) - 深度分析报告
  - generated_image_url (String) - 生成的预测图片URL
