import ollama
import os

MODEL = "mistral"
#def call_model(prompt, model="yarn-mistral:7b-128k", seed=None):
def call_model(prompt, model=MODEL, seed=None):
    messages = [{"role": "user", "content": prompt}]
    

    kwargs = {
        "model": model,
        "messages": messages,
    }

    if seed is not None:
        kwargs["seed"] = seed 

    try:
        response = ollama.chat(**kwargs)
        return response["message"]["content"]
    except Exception as e:
        print(f"❌ Model call failed: {e}")
        return "⚠️ Model call error."
    
def save_lore(text, planet_name):
    try:
        # Sanitize and format filename
        safe_name = planet_name.strip().lower().replace(" ", "_")
        if not safe_name:
            raise ValueError("Planet name is missing or invalid.")

        # Ensure output/ exists
        os.makedirs("output", exist_ok=True)

        path = os.path.join("output", f"{safe_name}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"✅ Lore saved to: {path}")
    except Exception as e:
        print(f"❌ Failed to save Lore: {e}")