from utils.llm_tools import call_llm

def plot_writer(state):
    genre = state["genre"]
    notes = state.get("additional_notes", "")

    user_prompt = f"Write a one-paragraph movie plot for a {genre} film."

    system_prompt = f"""
You are a creative screenwriter.

If the user’s notes include the name of an existing movie or franchise (e.g., Transformers, Star Wars, Marvel, etc.):
- You MUST treat the plot as taking place in that franchise’s universe.
- Use only established characters, settings, and canon unless told otherwise.
- You MAY invent original side characters, but the main story must tie into the existing lore.
- Assume the audience is familiar with the franchise.
- Do not "borrow the tone" of a franchise — actually write in that universe.

If the notes do NOT mention a known franchise, invent everything from scratch.

Creative Notes:
{notes}

Avoid summarizing. Do not say “This is a movie about...” or repeat the title. Just write the plot itself with action, tension, and clear stakes.
"""

    plot = call_llm(user_prompt, system_prompt)
    state["plot"] = plot
    return state
