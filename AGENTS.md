# Meme Token Analyzer 工作流

## 项目概述
- **名称**: Meme_Token_Analyzer
- **功能**: 分析 Meme Token 的网络舆情，生成"冲向月球"预测图，输出暴富基因检测报告

## 节点清单

| 节点名 | 文件位置 | 类型 | 功能描述 | 分支逻辑 | 配置文件 |
|-------|---------|------|---------|---------|---------|
| search | `nodes/search_node.py` | task | 网络搜索代币新闻和社交媒体情绪 | - | - |
| image_gen | `nodes/image_gen_node.py` | task | 生成代币冲向月球的预测图片 | - | - |
| clean_data | `nodes/clean_data_node.py` | task | 将搜索结果精简为摘要文本 | - | - |
| analysis | `nodes/analysis_node.py` | agent | 多模态暴富基因检测分析 | - | `config/analysis_llm_cfg.json` |

**类型说明**: task(task节点) / agent(大模型) / condition(条件分支) / looparray(列表循环) / loopcond(条件循环)

## 子图清单
无子图

## 技能使用
- 节点 `search` 使用技能 `web-search` 进行网络搜索
- 节点 `image_gen` 使用技能 `image-generation` 生成图片
- 节点 `analysis` 使用技能 `llm` 进行多模态分析（doubao-seed-1-6-vision-250815）

## 工作流结构
```
START
  ├── search (网络搜索) ──> clean_data (数据清洗) ──┐
  └── image_gen (图片生成) ────────────────────────┤
                                                    ├─> analysis (暴富基因检测) ──> END
```

## 输入输出
- **输入**: token_name (String) - 代币名称，如 "PEPE"、"SHIB"、"Dogecoin"
- **输出**: 
  - analysis_report (String) - 幽默风趣的暴富基因检测报告
  - generated_image_url (String) - 生成的预测图片URL

## 分析框架
报告包含四个维度：
1. 🎯 **叙事魔性度分析** - 名字、概念是否让人过目不忘
2. 📢 **社区 CX 能力预测** - 社区活跃度和喊单强度
3. 🎨 **视觉基因检测** - Meme 形象的爆款潜质
4. 🏆 **暴富基因等级** - 最终判决
   - 🌟 Diamond Hand (钻石手) - 万倍币潜质
   - 🌙 Moonshot (冲月球) - 百倍可期
   - 🗑️ Paper Hand (纸手) - 可能是 Rug
   - 💩 Shitcoin (屎币) - 远离
