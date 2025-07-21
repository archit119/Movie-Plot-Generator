from utils.llm_tools import call_llm

def casting_agent(state):
    plot = state["plot"]
    user_prompt = f""""
    You are a proffesional casting director
    Based on this plot:
    {plot}

    Suggest a cast for this entire film
    The cast should be based on how good the actor will match the role
    Do not always go for the most famous actor choice, it is okay to even take relatively unkown actors if they will fit the role better
    """
    system_prompt = "You are a Hollywood casting director. Choose actors that match the story."
    state["cast"] = call_llm(user_prompt, system_prompt)
    return state