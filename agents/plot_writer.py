from utils.llm_tools import call_llm

def plot_writer(state):
    genre = state["genre"]
    user_prompt = f"Write a short, original movie plot for a {genre} film."
    system_prompt = """
    "Write a 1-paragraph plot for a [genre] movie. 
    Avoid summarizing it afterward. Do not say 'this is a movie about...'. 
    Do not repeat the title. 
    Just jump straight into the story with character names and dramatic tension."
    """
    state["plot"] = call_llm(user_prompt, system_prompt)
    return state
