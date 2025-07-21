import time
import gradio as gr
from graph_builder import build_graph
import webbrowser
from IPython.display import Image, display

# Build the LangGraph once when app starts
graph = build_graph()

def generate_movie_pitch(genre, director_style):

    try:
        initial_state = {"genre": genre}
        if director_style.strip():
            initial_state["director_style"] = director_style.strip()

        result = graph.invoke(initial_state)

        title = result.get("title", "N/A").strip()
        plot = result.get("plot", "N/A").strip()
        cast = result.get("cast", "N/A").strip()
        verdict = result.get("verdict", "N/A").strip()

        # Create a list of lines to stream out one by one
        lines = [
            f"🎬 **Title**: {title}",
            "",
            f"🧠 **Plot**: {plot}",
            "",
            f"🎭 **Cast**: {cast}",
            "",
            f"🧪 **Verdict**: {verdict}"
        ]

        full_output = ""
        for line in lines:
            full_output += line + "\n"
            yield full_output
            time.sleep(0.3)  # control typing speed

    except Exception as e:
        yield "", f"❌ Error occurred: {str(e)}"


# Build the Gradio interface
demo = gr.Interface(
    fn=generate_movie_pitch,
    inputs=[
        gr.Textbox(label="🎥 Enter a Movie Genre"),
        gr.Textbox(label="🎬 Optional: Director Style (e.g. Jordan Peele, Christopher Nolan)")
    ],
    outputs = gr.Markdown(label="🎬 Movie Pitch Result"),
    title="LangGraph Movie Pitch Generator",
    description="Create AI-generated movie pitches with optional director tone/style.",
    allow_flagging="never"
).queue()


# Launch the app
if __name__ == "__main__":
    url = "http://localhost:7860"
    webbrowser.open(url) 
    demo.launch()

#display(Image(graph.get_graph().draw_mermaid_png()))