from utils.llm_tools import call_llm

def critic_agent(state):
    plot = state["plot"]
    cast = state["cast"]
    title = state["title"]

    franchise = state.get("additional_notes", "")

    user_prompt = f"""
    Movie Pitch:
    Title: {title}
    Plot: {plot}
    Cast: {cast}

    User’s creative notes include: {franchise}

    Evaluate this pitch.

    If it is meant to be in a known franchise universe (e.g., Transformers, Star Wars, Harry Potter) but does not include canonical characters, settings, or lore — reply 'Inconsistent'.

    If the tone, plot, and casting feel cohesive **within the intended universe**, reply 'Consistent'.

    If any part feels generic, contradictory, or off-brand, reply 'Inconsistent'.

    Be extremely strict. Reply with only one word: 'Consistent' or 'Inconsistent'.
"""

    system_prompt = "You are a strict film critic evaluating whether movie pitches make sense within the context of franchise universes if mentioned."

    state["verdict"] = call_llm(user_prompt.strip(), system_prompt).strip()
    retries = state.get("retries", 0)
    return {**state, "verdict": state["verdict"], "retries": retries + 1}
