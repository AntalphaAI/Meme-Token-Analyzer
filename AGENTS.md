# Meme Token Analyzer Workflow

## Project Overview
- **Name**: Meme_Token_Analyzer
- **Function**: Analyze Meme Token sentiment, generate "Moonshot" prediction image, and output wealth gene detection report

## Node Inventory

| Node Name | File Location | Type | Description | Branch Logic | Config File |
|-------|---------|------|---------|---------|---------|
| search | `nodes/search_node.py` | task | Search token news and social media sentiment | - | - |
| image_gen | `nodes/image_gen_node.py` | task | Generate token moonshot prediction image | - | - |
| clean_data | `nodes/clean_data_node.py` | task | Clean search results into summary text | - | - |
| analysis | `nodes/analysis_node.py` | agent | Multimodal wealth gene detection analysis | - | `config/analysis_llm_cfg.json` |

**Type Legend**: task (task node) / agent (LLM) / condition (conditional branch) / looparray (list loop) / loopcond (conditional loop)

## Subgraph Inventory
No subgraphs

## Skills Used
- Node `search` uses skill `web-search` for web search
- Node `image_gen` uses skill `image-generation` for image generation
- Node `analysis` uses skill `llm` for multimodal analysis (doubao-seed-1-6-vision-250815)

## Workflow Structure
```
START
  ├── search (Web Search) ──> clean_data (Data Cleaning) ──┐
  └── image_gen (Image Generation) ────────────────────────┤
                                                            ├─> analysis (Wealth Gene Detection) ──> END
```

## Input/Output
- **Input**: token_name (String) - Token name, e.g., "PEPE", "SHIB", "Dogecoin"
- **Output**: 
  - analysis_report (String) - Humorous and professional wealth gene detection report
  - generated_image_url (String) - Generated prediction image URL

## Analysis Framework
Report contains four dimensions:
1. 🎯 **Narrative Magic Analysis** - Whether name and concept are memorable
2. 📢 **Community Hype Ability Prediction** - Community activity and shilling intensity
3. 🎨 **Visual Gene Detection** - Meme image's viral potential
4. 🏆 **Wealth Gene Rating** - Final verdict
   - 🌟 Diamond Hand - 10000x potential
   - 🌙 Moonshot - 100x expected
   - 🗑️ Paper Hand - Likely a rug
   - 💩 Shitcoin - Stay away
