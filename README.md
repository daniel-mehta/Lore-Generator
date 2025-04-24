# 🌍 Lore Generator — LLM-Powered Worldbuilder Tool
![Python](https://img.shields.io/badge/python-3.8-blue)
![Built with VS Code](https://img.shields.io/badge/built%20with-VS%20Code-1f425f.svg)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![Mistral](https://img.shields.io/badge/Model-Mistral-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![Status: MVP](https://img.shields.io/badge/status-MVP-yellow)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)

A local, terminal-based lore generation tool that creates deep sci-fi/fantasy civilizations using open-source LLMs via [Ollama](https://ollama.com).

> 🧠 Written in a single day to explore the storytelling potential of local language models — and as a way to learn prompt chaining, project structure, and LLM-based creativity through a narrative lens.

---

## ✨ Features

- 📥 Input worldbuilding elements (race, planet, era, tech level, etc.)
- 🔗 Runs a **3-step prompt chain**:
  - `## Culture`
  - `## Government`
  - `## Conflicts & Timeline`
- 🧠 Prompts dynamically adapt to your inputs (tone, factions, notable figures, etc.)
- 📄 Outputs clean markdown, great for:
  - Wikis
  - Game dev world files
  - TTRPG prep
- 💾 Saves to `/output` as `planet_name.md`
- 🔁 Supports rerolling one section at a time
- 🎲 Optional seed for reproducible generation

---

## 🧠 Why?

This tool was created to experiment with **creative LLM workflows** beyond code and text summarization.

Ideal for:
- Game devs designing new universes
- Writers planning lore-rich settings
- Worldbuilders creating factions, timelines, and conflicts
- Anyone who wants to play God (responsibly)

---

## 🚀 Quickstart

### 1. Install Ollama
Download from [ollama.com/download](https://ollama.com/download)

Then pull a model (tested with Mistral):
```bash
ollama run mistral
```
### 2. Clone this repo
```bash
git clone https://github.com/daniel-mehta/Lore-Generator
cd Lore-Generator
```
### 3. Run it
```bash
python lore_builder.py
```
Follow the prompts to:
- Enter your race, planet, and world parameters
- Wait while it generates culture, government, and history
- Save or reroll a section if you want to refine the output

---

## 🕐 Performance Note
Each run makes 3 model calls (one per section) using a local LLM. Depending on your hardware, a full generation may take 5–10 minutes.

---

## 🗂 Project Structure

```bash
Lore-Generator/
├── output/              # Saved markdown files
│   └── dogtopia.md, earth.md, tamriel.md, etc
├── lore_builder.py      # Prompt logic + main pipeline
├── utils.py             # Model caller, file saver, etc.
└── README.md            # You're here
```

---

## 📄 Example Outputs
- Dogtopia: A tech-dominant AI empire of Puppiers
- Earth: A hopeful take on modern humanity under a Global Coalition

Each file includes:
- Full markdown
- Factions, power dynamics, timeline
- Rich lore usable for games or fiction

---

## 🌱 Future Ideas

- Export to JSON or docx for game import
- Stat-based generation (e.g., Militarism: 7/10)
- Built-in faction/naming generator
- Frontend with Streamlit or React
- Batch runs with seed presets

---

## 🛠 Built With

- Python 3.8+
- Ollama (local LLM runner)
- Mistral 7B (model)
- Visual Studio Code

---

## 📄 License

- MIT — free to use, modify, or build on.

---

## ✍️ Notes

This project was built in a single day as a creative experiment — blending storytelling and AI into a reusable pipeline. It's also a stepping stone for more structured, game-integrated LLM tools. Suggestions and forks welcome.

---
