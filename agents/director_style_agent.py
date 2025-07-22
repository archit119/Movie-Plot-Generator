from utils.llm_tools import call_llm

def director_style_agent(state):
    if not state.get("director_style"):  # Optional check
        return state  # Skip if no style was given

    style = state["director_style"]
    plot = state["plot"]

    user_prompt = f"Rewrite the movie plot below as if it were directed in the style of {style}. Maintain the same core story, but adjust tone, pacing, and mood to reflect their typical directorial style.\n\n{plot}"
    system_prompt = """
Rewrite the following movie plot, cast, and tone in the style of [director]. You may change character personalities, plot structure, pacing, and genre conventions to reflect this director's signature. If the director is known for humor, add dark comedy or absurdity. If they’re known for stylized visuals or subversion, make the world feel more eccentric. Do NOT simply rephrase the original — reinterpret it completely in the director’s voice.
If an already existing franchise / character has been mentioned do the following:
Try not to change any key origin stories or characters
"""

    state["plot"] = call_llm(user_prompt, system_prompt)
    return state
