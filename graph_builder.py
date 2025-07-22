from langgraph.graph import StateGraph
from typing import Optional, TypedDict
from agents.plot_writer import plot_writer
from agents.casting_agent import casting_agent
from agents.title_agent import title_agent
from agents.critic_agent import critic_agent
from agents.director_style_agent import director_style_agent
import matplotlib.pyplot as plt
import networkx as nx
from IPython.display import Image, display

class MovieState(TypedDict):
    genre: str
    plot: str
    cast: str
    title: str
    verdict: str
    director_style: Optional[str]
    additional_notes: Optional[str]
    retries: int

def build_graph():
    builder = StateGraph(MovieState)

    builder.add_node("PlotWriter", plot_writer)
    builder.add_node("CastingAgent", casting_agent)
    builder.add_node("TitleAgent", title_agent)
    builder.add_node("CriticAgent", critic_agent)
    builder.add_node("DirectorStyleAgent", director_style_agent)

    builder.set_entry_point("PlotWriter")
    builder.add_edge("PlotWriter", "DirectorStyleAgent")
    builder.add_edge("DirectorStyleAgent", "CastingAgent")
    builder.add_edge("CastingAgent", "TitleAgent")
    builder.add_edge("TitleAgent", "CriticAgent")

    builder.add_conditional_edges(
    "CriticAgent",
    lambda state: "FinalOutput"
    if state["verdict"] == "Consistent" or state.get("retries", 0) >= 24
    else "PlotWriter"
    )

    # Final output node
    builder.add_node("FinalOutput", lambda s: print("\n🎬 FINAL MOVIE PITCH:\n", s))

    graph = builder.compile()
    draw_graph(graph) 
    return graph


def draw_graph(graph):
    png_data = graph.get_graph().draw_mermaid_png()

    # Save it
    with open("langgraph_diagram.png", "wb") as f:
        f.write(png_data)

    # Auto-open it
    import webbrowser
    import os
    file_path = os.path.abspath("langgraph_diagram.png")
    webbrowser.open(f"file://{file_path}")

    print("✅ LangGraph visual saved as 'langgraph_diagram.png'")


