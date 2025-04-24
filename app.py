import streamlit as st
from lore_builder import (
    generate_culture,
    generate_government,
    generate_conflicts,
    format_markdown,
    set_seed
)
from utils import save_lore

st.set_page_config(page_title="Lore Generator", layout="wide")
st.title("🌍 LLM-Powered Lore Generator")
st.caption("Build your world. Generate deep lore. Powered by a local LLM.")

# Reset button
if st.button("🛑 Cancel / Reset"):
    st.session_state.clear()
    st.experimental_rerun()

# Form
with st.form("lore_form"):
    race = st.text_input("Race", "")
    planet = st.text_input("Planet", "")
    era = st.text_input("Era", "")
    tech_level = st.text_input("Tech Level", "")
    climate = st.text_input("Climate", "")
    alignment = st.text_input("Dominant Alignment", "")
    governance_type = st.text_input("Governance Type", "")
    religion_style = st.text_input("Religion Style", "")
    economy_type = st.text_input("Economy Type", "")
    magic_or_ai = st.selectbox("Magic or AI?", ["Magic", "AI", "Both", "None"])
    faction_count = st.number_input("Number of Factions", min_value=1, value=3)
    figures = st.text_input("Notable Figures (comma-separated)", "")
    tone = st.text_input("Tone", "")
    inspirations = st.text_input("Inspiration Sources (comma-separated)", "")
    language_flavor = st.text_input("Language Flavor", "")
    conflict_type = st.text_input("Conflict Type (optional)", "")
    seed = st.text_input("Seed (optional)", "")

    submit = st.form_submit_button("✨ Generate Lore")

# Generation logic
if submit:
    inputs = {
        "race": race,
        "planet": planet,
        "era": era,
        "tech_level": tech_level,
        "climate": climate,
        "dominant_alignment": alignment,
        "governance_type": governance_type,
        "religion_style": religion_style,
        "economy_type": economy_type,
        "magic_or_ai": magic_or_ai,
        "faction_count": faction_count,
        "notable_figures": [f.strip() for f in figures.split(",") if f.strip()],
        "tone": tone,
        "inspiration_sources": [s.strip() for s in inspirations.split(",") if s.strip()],
        "language_flavor": language_flavor,
        "conflict_type": conflict_type or None,
        "seed": seed or None,
    }

    if seed:
        set_seed(seed)

    with st.spinner("Calling local model... this may take a few minutes."):
        culture = generate_culture(inputs)
        government = generate_government(culture, inputs)
        conflicts = generate_conflicts(culture, government, inputs)
        output_md = format_markdown(inputs, culture, government, conflicts)

        st.session_state["output_md"] = output_md
        st.session_state["planet"] = planet

# Output
if "output_md" in st.session_state:
    st.markdown("---")
    st.subheader("📝 Generated Lore")
    st.markdown(st.session_state["output_md"])

    filename = f"{st.session_state['planet'].strip().lower().replace(' ', '_') or 'lore'}.md"
    st.download_button("💾 Download Markdown", st.session_state["output_md"], file_name=filename)
