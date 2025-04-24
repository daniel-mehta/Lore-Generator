# 🌍 Lore Generator — LLM-Powered Worldbuilder Tool
![Python](https://img.shields.io/badge/python-3.8-blue)
![Built with VS Code](https://img.shields.io/badge/built%20with-VS%20Code-1f425f.svg)
![Streamlit UI](https://img.shields.io/badge/UI-Streamlit-red)
![Ollama](https://img.shields.io/badge/LLM-Ollama-green)
![Mistral](https://img.shields.io/badge/Model-Mistral-blueviolet)
![License](https://img.shields.io/badge/license-MIT-green)
![Status: MVP](https://img.shields.io/badge/status-MVP-yellow)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)

A local lore-generation tool that builds detailed sci-fi and fantasy civilizations using open-source LLMs via Ollama — with both a terminal mode and a full UI built in Streamlit.

> 🧪 Originally built in a single day to explore creative LLM use, prompt chaining, and worldbuilding workflows. The next day, a UI was added to make the generator accessible to non-technical users.

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

## 📸 UI Showcase
A streamlit-based UI was built the following day to turn the core tool into an interactive experience — no coding required.

> The backend was written in a single day, followed by a second day spent designing and connecting the Streamlit UI.

- All features from the terminal version are available: full input customization, markdown export, and reroll support
- Sample input inspired by the Oblivion Remake generated immersive fantasy lore for a setting called Nerathis
  
You can explore the full UI and result via the included PDF:
[Lore Generator UI.pdf](https://github.com/user-attachments/files/19895909/Lore.Generator.UI.pdf)

---

## 🚀 Quickstart

### 1. Install Ollama and Streamlit
Download from [ollama.com/download](https://ollama.com/download)

Then pull a model (tested with Mistral):
```bash
ollama run mistral
```

Streamlit (UI Framework)

Install via pip:
```bash
pip install streamlit
```
> You'll need both installed if you want to use the full interactive UI. If you're using only the terminal version, Streamlit is optional.

### 2. Clone this repo
```bash
git clone https://github.com/daniel-mehta/Lore-Generator
cd Lore-Generator
```
### 3. Choose How You Want to Run It
🔧 Terminal (CLI Mode)

For fast, no-UI usage:
```bash
python lore_builder.py
```
Follow the prompts to:
- Enter your worldbuilding inputs
- Generates culture, government, and conflict/timeline
- Outputs full markdown and saves it to /output

🖼️ Streamlit UI

For a visual interface with form fields and download button:
```bash
streamlit run app.py
```
- Use a form to input race, planet, tone, etc.
- View live markdown output
- Download results directly from your browser

---

## 🕐 Performance Note
Each run makes 3 model calls (one per section) using a local LLM. Depending on your hardware, a full generation may take 5–10 minutes.

---

## 🗂 Project Structure

```bash
Lore-Generator/
├── output/                 # Saved markdown lore files
│   └── dogtopia.md, earth.md, nerathis.md, etc
├── app.py                  # Streamlit UI frontend
├── lore_builder.py         # Main generation logic
├── utils.py                # Model interface + helpers
├── prototype.ipynb         # Initial dev notebook
├── Lore Generator UI.pdf   # UI + sample output showcase
└── README.md               # You're here
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
- Streamlit (UI framework)
- Ollama (local LLM runner)
- Mistral 7B (model)
- Jupyter Notebook (prototype phase)
- Visual Studio Code

---

## 📸 Screenshots of UI
![Lore Generator UI_page-0001](https://github.com/user-attachments/assets/dae2e84b-64bd-47f9-8456-c3e239a9bc0d)
![Lore Generator UI_page-0002](https://github.com/user-attachments/assets/b0eb195a-9995-41ae-975d-32746f06ad4a)
![Lore Generator UI_page-0003](https://github.com/user-attachments/assets/3ea131f6-3c51-4f39-8c50-fd1e49c54a62)
![Lore Generator UI_page-0004](https://github.com/user-attachments/assets/c730d92a-3227-41e8-ac1a-2c8c7a9d4c45)

---

## 📄 License

- MIT — free to use, modify, or build on.

---

## ✍️ Notes

This project was built in a single day as a creative experiment — blending storytelling and AI into a reusable pipeline. It's also a stepping stone for more structured, game-integrated LLM tools. Suggestions and forks welcome.

---
