from utils.llm_tools import call_llm

def critic_agent(state):
    plot = state["plot"]
    cast = state["cast"]
    title = state["title"]

    user_prompt = f"""
Here is the movie pitch. Title: {title} | Plot: {plot} | Cast: {cast}.

If the tone, plot, and casting feel cohesive, reply 'Consistent'. If any part feels off-brand, overly generic, or contradictory (e.g. miscast actors, mismatched genre), reply 'Inconsistent'. Be very strict. Only use one word.

"""
    system_prompt = "You are a strict film critic evaluating whether movie pitches make sense."
    state["verdict"] = call_llm(user_prompt.strip(), system_prompt).strip()
    return state
