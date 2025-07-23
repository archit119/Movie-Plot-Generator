from utils.llm_tools import call_llm

def scene_writer(state):
    full_script = ""
    outline = state.get("script_outline", [])

    for i, scene in enumerate(outline):
        prompt = f"""
Write Scene {i+1} of a feature film.

Scene Outline: {scene}
Title: {state['title']}
Characters: {state['cast']}
Style: {state['director_style'] or 'Hollywood action'}

Write the full scene with proper screenplay formatting. Include character names, dialogue, and stage directions.
"""

        scene_text = call_llm(prompt, system_prompt="You're a professional screenwriter.")
        full_script += f"\n\n{scene_text.strip()}"

    state["script"] = full_script
    return state
