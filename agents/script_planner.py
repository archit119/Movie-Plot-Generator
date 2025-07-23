from utils.llm_tools import call_llm

def script_planner(state):
    prompt = f"""
You are a screenplay planner. Given the following movie:

Title: {state['title']}
Plot: {state['plot']}
Cast: {state['cast']}

Create a 3-act scene-by-scene outline for a feature-length movie (~90 minutes).
Break it into ~15–20 brief scene descriptions.
"""

    scene_list = call_llm(prompt, system_prompt="Respond only with a numbered list of scene descriptions.")
    state["script_outline"] = scene_list.split("\n")  # turn into a list
    return state
