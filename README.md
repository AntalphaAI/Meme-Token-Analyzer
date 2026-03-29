# Meme Token Analyzer 🚀

A powerful LangGraph workflow that analyzes Meme tokens with humor and expertise, generating comprehensive wealth gene detection reports.

## Features ✨

- **🔍 Web Search**: Searches latest news, social media sentiment, and market trends
- **🎨 Image Generation**: Creates "Moonshot" prediction images for tokens
- **🧹 Data Cleaning**: Condenses search results into LLM-friendly summaries
- **🤖 AI Analysis**: Multimodal analysis combining sentiment data and visual elements
- **💎 Wealth Gene Rating**: Four-tier rating system (Diamond Hand, Moonshot, Paper Hand, Shitcoin)

## Workflow Architecture 📊

```
START
  ├── Search Node ──> Clean Data Node ──┐
  └── Image Gen Node ───────────────────┤
                                         ├─> Analysis Node ──> END
```

## Installation 🛠️

This project uses the Coze Coding platform with pre-installed dependencies. No additional installation required.

## Usage 💻

### Input
```json
{
  "token_name": "PEPE"
}
```

### Output
```json
{
  "analysis_report": "Full analysis report in Markdown format...",
  "generated_image_url": "https://..."
}
```

## Testing 🧪

Run the workflow with different tokens:
- `DOGE` - Dogecoin
- `SHIB` - Shiba Inu
- `BONK` - Bonk
- `WIF` - dogwifhat
- `PEPE` - Pepe

## Analysis Dimensions 📈

1. **🎯 Narrative Magic Analysis**
   - Name memorability
   - Concept uniqueness
   - Community sentiment

2. **📢 Community Hype Ability Prediction**
   - Community activity level
   - Shilling intensity
   - Social media buzz

3. **🎨 Visual Gene Detection**
   - Visual appeal
   - Viral potential
   - Brand recognition

4. **🏆 Wealth Gene Rating**
   - 🌟 **Diamond Hand**: 10000x potential
   - 🌙 **Moonshot**: 100x expected
   - 🗑️ **Paper Hand**: Likely a rug
   - 💩 **Shitcoin**: Stay away

## Tech Stack 🛠️

- **Framework**: LangGraph
- **LLM**: doubao-seed-1-6-vision-250815 (Multimodal)
- **Skills**: 
  - web-search (Coze Coding SDK)
  - image-generation (Coze Coding SDK)
  - llm (Coze Coding SDK)

## Project Structure 📁

```
src/
├── graphs/
│   ├── state.py              # State definitions
│   ├── graph.py               # Main graph orchestration
│   └── nodes/
│       ├── search_node.py     # Web search node
│       ├── image_gen_node.py  # Image generation node
│       ├── clean_data_node.py # Data cleaning node
│       └── analysis_node.py   # LLM analysis node
config/
└── analysis_llm_cfg.json      # LLM configuration
```

## Disclaimer ⚠️

This tool is for entertainment and educational purposes only. Not financial advice. Always DYOR (Do Your Own Research) before investing in any cryptocurrency. Meme tokens are highly volatile and risky investments.

## License 📄

MIT License

---

Made with 💎 by Coze Coding AI
