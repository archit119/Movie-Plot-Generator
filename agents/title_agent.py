from utils.llm_tools import call_llm

def title_agent(state):
    plot = state["plot"]
    user_prompt = f"Give a creative and catchy movie title for this plot: '{plot}'"
    system_prompt = "You are a creative screenwriter who names movies for Hollywood."
    state["title"] = call_llm(user_prompt, system_prompt)
    return state
