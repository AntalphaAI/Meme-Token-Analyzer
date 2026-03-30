# Meme Token Analyzer 🚀

> **The Ultimate Meme Token "Wealth Gene" Detection System**

A powerful LangGraph workflow that analyzes Meme tokens with humor and expertise, generating comprehensive wealth gene detection reports using real-time web sentiment, AI-generated prediction images, and multimodal AI analysis.


---

## 🎯 What Makes This Special?

**Edge Case Mastery**: Our analyzer doesn't just look at market caps—it scans the deep web for sentiment even on random strings. Whether it's a legendary meme like `$PEPE`, a major coin like `$BTC`, or a keyboard smash like `qwertyuiop`, it delivers intelligent analysis with real data!

---

## ✨ Features

### Core Capabilities
- **🔍 Real-Time Web Search**: Fetches latest news, social media sentiment, and market trends with **1-month time filter** for fresh data
- **🎨 AI Image Generation**: Creates "Moonshot" prediction images with cyberpunk aesthetic
- **🧹 Smart Data Cleaning**: Condenses search results into LLM-friendly summaries with **date freshness validation**
- **🤖 Multimodal AI Analysis**: Combines text sentiment + visual analysis using vision-language models
- **💎 Wealth Gene Rating**: Four-tier rating system with Degen-style humor

### Intelligent Features
- **🧠 Smart Detection**: Automatically identifies major coins (BTC/ETH/SOL), handles missing data, and filters irrelevant results
- **📅 Data Freshness Check**: Validates search result dates and warns if data is outdated
- **🎯 Edge Case Handling**: Gracefully processes random strings, unknown tokens, and obscure names

---

## 🏆 Wealth Gene Rating System

| Rating | Meaning | Potential |
|--------|---------|-----------|
| 🌟 **Diamond Hand** | Next 10000x coin | Legendary potential |
| 🌙 **Moonshot** | 100x expected | High growth potential |
| 🗑️ **Paper Hand** | Likely a rug | High risk |
| 💩 **Shitcoin** | Stay far away | Avoid |

---

## 📊 Case Studies

### Case 1: Classic Meme Token - $PEPE ✅

**Input**: `PEPE`

**Result**: 🌙 **Moonshot**

**Highlights**:
- Found real community discussions with recent dates
- Analyzed narrative magic (iconic meme + celebrity triggers)
- Detected viral visual gene potential
- Recommended for degens with risk tolerance

**Key Insight**: *"PEPE has the wealth gene pumping through its digital veins!"*

---

### Case 2: Major Cryptocurrency - $BTC ⚠️

**Input**: `BTC`

**Result**: 🌟 **Diamond Hand** (with special warning)

**Highlights**:
- **Triggered**: Smart detection for non-meme major coin
- **Warning**: "⚠️ Detected non-typical Meme, now performing cross-border scan with [Top Value Coin] perspective"
- Analyzed as value coin rather than meme token
- Still provided comprehensive analysis

**Key Insight**: *"BTC is not just a currency, it's a legend!"*

---

### Case 3: Edge Case - `qwertyuiop` 🎹

**Input**: `qwertyuiop` (keyboard smash)

**Result**: 🌙 **Moonshot**

**Highlights**:
- ✅ **Found real data**: 126 unique individuals discussing
- ✅ **Real sentiment**: 47.37% bullish sentiment detected
- ✅ **Activity ranking**: 446th in mentions
- ✅ **Intelligent analysis**: "Unique but underdeveloped narrative"
- ✅ **Actionable advice**: "If they lean into keyboard meme + cyberpunk anime, could 100x"

**Key Insight**: *"Even a keyboard smash has a story if you know where to look!"*

**This demonstrates our Edge Case Mastery**:
- No fabricated data or hallucinated prices
- Real web scraping capabilities
- Intelligent handling of unknown tokens
- Constructive analysis even for obscure inputs

---

## 🎨 Output Format

### Analysis Report Structure

```markdown
# $TOKEN Meme Token "Wealth Gene" Detection Report

## 🎯 Narrative Magic Analysis
[Memorability, concept uniqueness, sentiment]

## 📢 Community Hype Ability Prediction
[Community activity, shilling intensity]

## 🎨 Visual Gene Detection
[Visual appeal, viral potential]

## 🏆 Final Verdict: Wealth Gene Rating
[Rating: 🌟/🌙/🗑️/💩]

[Special warnings if applicable]
```

### Features
- ✅ Proper Markdown heading hierarchy
- ✅ Rich emoji annotations
- ✅ Mobile-friendly formatting
- ✅ Auto-embedded image URLs
- ✅ Clear visual hierarchy

---

## 🏗️ Architecture

### Workflow Structure

```
START
  ├── search (Web Search, 1m filter) ──> clean_data (Freshness Check) ──┐
  └── image_gen (2K Cyberpunk Image) ────────────────────────────────────┤
                                                                          ├─> analysis (Multimodal LLM) ──> END
```

### Tech Stack

- **Framework**: LangGraph (DAG-based workflow)
- **LLM**: doubao-seed-1-6-vision-250815 (Multimodal)
- **Skills**: 
  - web-search (Real-time data)
  - image-generation (AI art)
  - llm (Vision-language model)

---

## 📁 Project Structure

```
src/
├── graphs/
│   ├── state.py              # State definitions
│   ├── graph.py               # Main graph orchestration
│   └── nodes/
│       ├── search_node.py     # Web search (time_range="1m")
│       ├── image_gen_node.py  # Image generation (2K)
│       ├── clean_data_node.py # Data cleaning + freshness check
│       └── analysis_node.py   # Multimodal analysis
config/
└── analysis_llm_cfg.json      # LLM prompts & config
```

---

## 🧪 Testing

### Test Cases

| Token | Type | Expected Behavior | Status |
|-------|------|-------------------|--------|
| `PEPE` | Classic meme | Normal analysis | ✅ PASS |
| `DOGE` | Major meme | Diamond Hand rating | ✅ PASS |
| `BTC` | Major coin | Special warning + analysis | ✅ PASS |
| `ETH` | Major coin | Special warning + analysis | ✅ PASS |
| `qwertyuiop` | Edge case | Real data + Moonshot | ✅ PASS |
| `XYZABC123` | Unknown | Freshness warning + analysis | ✅ PASS |

### Performance Metrics
- **Search**: ~3-5 seconds
- **Image Gen**: ~5-8 seconds
- **Analysis**: ~8-12 seconds
- **Total**: ~15-25 seconds

---

## 🛡️ Error Handling

The workflow gracefully handles:

✅ **Unknown tokens** with minimal data
✅ **Major cryptocurrencies** (BTC/ETH/SOL) with warnings
✅ **Random strings** and keyboard smashes
✅ **Outdated information** with freshness warnings
✅ **Empty search results** without hallucination
✅ **Missing publication dates** with appropriate notes

---

## 🎓 Pro Tips

1. **Compare multiple tokens** to understand rating differences
2. **Check date warnings** for data freshness validation
3. **Trust major coin warnings** - they're analyzed differently
4. **Read between the lines** - humor often masks real insights
5. **Use ratings wisely** - Diamond Hand > Moonshot > Paper Hand > Shitcoin

---

## 🤖 Bot Configuration

See `BOT_CONFIG.md` for:
- Opening greeting messages
- Suggested commands
- Bot avatar recommendations
- User onboarding tips

**Suggested Commands:**
1. `探测 $PEPE 的暴富基因` (Classic meme analysis)
2. `看看 $BTC 的 Meme 属性` (Major coin detection)
3. `随便测个乱码：qwertyuiop` (Edge case demonstration)

---

## 📝 Documentation

- `AGENTS.md` - Technical documentation for developers
- `BOT_CONFIG.md` - Bot setup guide
- `README.md` - This file (user-facing documentation)

---

## ⚠️ Disclaimer

This tool is for **entertainment and educational purposes only**. Not financial advice. Always DYOR (Do Your Own Research) before investing in any cryptocurrency. Meme tokens are highly volatile and risky investments.

**Remember**: Even Diamond Hands need risk management! 💎

---

## 📄 License

MIT License

**From keyboard smashes to moonshots - we analyze them all! 🚀**
