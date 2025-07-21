from graph_builder import build_graph

if __name__ == "__main__":
    genre = input("🎥 Enter a movie genre (e.g. sci-fi thriller, romantic comedy): ")
    graph = build_graph()
    initial_state = {"genre": genre}
    graph.invoke(initial_state)
