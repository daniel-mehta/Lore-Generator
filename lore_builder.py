import random
from utils import call_model, save_lore

def main():
    # 1. Gather user input
    inputs = collect_inputs()

    # 2. Set seed (for internal logic and future determinism)
    set_seed(inputs.get("seed"))

    # 3. Generate each lore section
    culture = generate_culture(inputs)
    government = generate_government(culture, inputs)
    conflicts_and_timeline = generate_conflicts(culture, government, inputs)

    # 4. Format final output
    final_output = format_markdown(inputs, culture, government, conflicts_and_timeline)

    # 5. Show result
    print("\n📝 FINAL LORE OUTPUT:\n")
    print(final_output)

    # 6. Save if requested
    if inputs.get("save_file"):
        save_lore(final_output, inputs["planet"])

    # 7. Optional reroll
    '''
    reroll = input("\n♻️ Reroll a section? [culture / government / conflict / none]: ").strip().lower()
    
    if reroll == "culture":
        culture = generate_culture(inputs)
    elif reroll == "government":
        government = generate_government(culture, inputs)
    elif reroll == "conflict":
        conflicts_and_timeline = generate_conflicts(culture, government, inputs)

    if reroll in ["culture", "government", "conflict"]:
        final_output = format_markdown(inputs, culture, government, conflicts_and_timeline)
        print("\n📝 UPDATED LORE OUTPUT:\n")
        print(final_output)

        if inputs.get("save_file"):
            save_lore(final_output, inputs["planet"])
    '''


def collect_inputs():
    print("🌍 LORE GENERATOR — Worldbuilding Input Wizard\n")

    inputs = {}

    # Core world inputs
    inputs["race"] = input("🧬 Race Name: ").strip()
    inputs["planet"] = input("🌍 Planet Name: ").strip()
    inputs["era"] = input("⏳ Era (e.g., Industrial, Galactic Age): ").strip()
    inputs["tech_level"] = input("🛠️ Tech Level (e.g., Spacefaring, Pre-industrial): ").strip()
    inputs["conflict_type"] = input("⚔️ Conflict Type (Optional): ").strip() or None
    seed_input = input("🎲 Seed (Optional, int or string): ").strip()
    inputs["seed"] = int(seed_input) if seed_input.isdigit() else seed_input if seed_input else None

    # World & society
    inputs["climate"] = input("🌦️ Climate (e.g., desert, arctic): ").strip()
    inputs["dominant_alignment"] = input("⚖️ Dominant Alignment (e.g., Lawful Evil, Neutral Good): ").strip()
    inputs["governance_type"] = input("🏛️ Governance Type (Optional, monarchy, AI council, etc.): ").strip() or None
    inputs["religion_style"] = input("⛩️ Religion Style (e.g., Mythology-driven, Animistic): ").strip()
    inputs["economy_type"] = input("💰 Economy Type (e.g., Agrarian, Technocapitalist): ").strip()
    inputs["magic_or_ai"] = input("🔮 Magic or AI? [Magic / AI / Both / None]: ").strip()

    try:
        faction_count = input("🏴 Number of Factions (e.g., 3): ").strip()
        inputs["faction_count"] = int(faction_count)
    except ValueError:
        inputs["faction_count"] = 3  # Default fallback

    # Notable Figures
    figures = input("👑 Notable Figures (comma-separated, optional): ").strip()
    inputs["notable_figures"] = [f.strip() for f in figures.split(",")] if figures else []

    # Tone & style
    inputs["tone"] = input("🧠 Tone (e.g., serious, satirical, hopeful): ").strip()
    inspirations = input("🎨 Inspiration Sources (comma-separated, optional): ").strip()
    inputs["inspiration_sources"] = [s.strip() for s in inspirations.split(",")] if inspirations else []

    inputs["language_flavor"] = input("🗣️ Language Flavor (e.g., Nordic, Slavic, custom phonetics): ").strip()

    # Save output
    save = input("💾 Save output to file? [y/N]: ").strip().lower()
    inputs["save_file"] = save == "y"

    print("\n✅ Inputs collected. Generating lore...\n")
    return inputs
def set_seed(seed_value):
    if seed_value is not None:
        try:
            random.seed(seed_value)
            print(f"🎲 Python seed set to: {seed_value}")
        except Exception as e:
            print(f"⚠️ Could not set seed: {e}")




def generate_culture(inputs):
    prompt = f"""
You are generating the **culture** of a race called **{inputs['race']}** living on the planet **{inputs['planet']}** during the **{inputs['era']}** era.
Their tech level is **{inputs['tech_level']}**, and the climate is **{inputs['climate']}**.

Their society aligns with **{inputs['dominant_alignment']}**, and uses **{inputs['magic_or_ai']}** as a dominant system.
The religion style is **{inputs['religion_style']}**, and the economy is **{inputs['economy_type']}**.

Use a **{inputs['tone']}** tone. Consider these inspirations: {", ".join(inputs['inspiration_sources']) or "None"}.
Use a naming style inspired by **{inputs['language_flavor']}**.

Describe their values, rituals, art, architecture, and general worldview in detail. 
Write this in a markdown section under:

## 🌐 Culture
"""
    return call_model(prompt.strip())


def generate_government(culture_text, inputs):
    prompt = f"""
Given the following cultural description of the race **{inputs['race']}**:

\"\"\"\n{culture_text.strip()}\n\"\"\"

Describe their **system of government** on the planet **{inputs['planet']}**.
Use a **{inputs['tone']}** tone. There are **{inputs['faction_count']} major factions** involved in the political structure.

If relevant, incorporate this governance type: **{inputs['governance_type']}**.

Cover leadership structure, power struggles, diplomacy, laws, and how the factions affect decision-making.

Write this in a markdown section under:

## 🏛️ Government
"""
    return call_model(prompt.strip())

def generate_conflicts(culture_text, government_text, inputs):
    notable = ", ".join(inputs['notable_figures']) if inputs['notable_figures'] else "None"
    
    prompt = f"""
Based on the following:

### Culture:
\"\"\"\n{culture_text.strip()}\n\"\"\"

### Government:
\"\"\"\n{government_text.strip()}\n\"\"\"

Generate **two major historical conflicts** for the planet **{inputs['planet']}**, considering a conflict style like **{inputs['conflict_type']}**.

Also include a **timeline of 5 major events**, featuring notable figures such as: {notable}.
Ensure the timeline is rich with consequence, alliances, or betrayals tied to the culture and government.

Use a **{inputs['tone']}** tone and naming conventions inspired by **{inputs['language_flavor']}**.

Write in two sections:
## ⚔️ Major Conflicts
## 📜 Timeline
"""
    return call_model(prompt.strip())

def format_markdown(inputs, culture, government, conflicts_and_timeline):
    title = f"# 🌍 {inputs['planet']}\n"
    subtitle = f"**Race:** {inputs['race']}  |  **Era:** {inputs['era']}  |  **Tech Level:** {inputs['tech_level']}\n\n"
    meta = f"**Climate:** {inputs['climate']}  |  **Magic/AI:** {inputs['magic_or_ai']}  |  **Tone:** {inputs['tone']}\n"
    
    body = "\n".join([
        culture.strip(),
        government.strip(),
        conflicts_and_timeline.strip()
    ])

    return f"{title}{subtitle}{meta}\n\n{body}"


if __name__ == "__main__":
    main()
