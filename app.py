import time
import gradio as gr
from graph_builder import build_graph
import webbrowser
from IPython.display import Image, display
import os
from openai import OpenAI

# Build the LangGraph once when app starts
graph = build_graph()

def generate_with_feedback(genre, director_style, additional_notes):
    yield gr.update(value="⏳ Generating... Please wait."), gr.update(), gr.update()
    
    try:
        pitch, script = generate_movie_pitch(genre, director_style, additional_notes)
        yield gr.update(value="✅ Done!"), gr.update(value=pitch), gr.update(value=script)

    except Exception as e:
        yield gr.update(value=f"❌ Error: {str(e)}"), gr.update(), gr.update()

def generate_movie_pitch(genre, director_style, additional_notes):
    try:
        # Build initial state for LangGraph
        initial_state = {
            "genre": genre,
            "additional_notes": additional_notes
        }

        if director_style.strip():
            initial_state["director_style"] = director_style.strip()

        result = graph.invoke(initial_state)

        # Extract results
        title = result.get("title", "N/A").strip()
        plot = result.get("plot", "N/A").strip()
        cast = result.get("cast", "N/A").strip()
        verdict = result.get("verdict", "N/A").strip()

        # Format movie pitch
        pitch_lines = [
            f"🎬 **Title**: {title}",
            f"🧠 **Plot**: {plot}",
            f"🎭 **Cast**: {cast}",
            f"🧪 **Verdict**: {verdict}"
        ]
        pitch_text = "\n\n".join(pitch_lines)

        # 🆕 Generate full script using GPT-4o-mini
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        script_prompt = (
            f"Based on the following movie pitch, write a short screenplay:\n\n"
            f"Title: {title}\nPlot: {plot}\nCast: {cast}\nDirector Style: {director_style}\n"
            f"Additional Notes: {additional_notes}\n\n"
            f"Format it as a screenplay using standard movie script formatting."
        )

        response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": script_prompt}
        ],
        temperature=0.8
        )

        script_text = response.choices[0].message.content


        return pitch_text, script_text

    except Exception as e:
        return f"❌ Error: {str(e)}", ""



# Build the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("🎥 **LangGraph Movie Pitch & Script Generator**")

    with gr.Row():
        genre = gr.Textbox(label="🎞️ Movie Genre")
        director_style = gr.Textbox(label="🎬 Director Style (optional)")

    additional_notes = gr.Textbox(label="📝 Additional Notes (e.g. themes, setting, mood)", lines=4)

    with gr.Row():
        generate_btn = gr.Button("🎬 Generate Pitch + Script")
        status_text = gr.Markdown("")

    with gr.Tabs():
        with gr.TabItem("Movie Pitch"):
            pitch_output = gr.Markdown()
        with gr.TabItem("Script"):
            script_output = gr.Markdown()

    # ✅ This MUST be inside the `with gr.Blocks()` scope!
    generate_btn.click(
        fn=generate_with_feedback,
        inputs=[genre, director_style, additional_notes],
        outputs=[status_text, pitch_output, script_output]
    )
 


# Launch the app
if __name__ == "__main__":
    url = "http://localhost:7860"
    webbrowser.open(url) 
    demo.launch()

#display(Image(graph.get_graph().draw_mermaid_png()))