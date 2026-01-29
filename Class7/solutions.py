import networkx as nx
import numpy as np
import random


def simulate_sir_percolation(G, seed_set, p, iterations=1000):

    total_infected_counts = []

    for _ in range(iterations):
        open_edges = [(u, v) for u, v in G.edges() if random.random() < p]

        X_graph = nx.Graph()
        X_graph.add_nodes_from(G.nodes())
        X_graph.add_edges_from(open_edges)

        eventually_infected = set()
        for seed in seed_set:
            if seed in X_graph:
                reachable = nx.descendants(X_graph, seed) | {seed}
                eventually_infected.update(reachable)

        total_infected_counts.append(len(eventually_infected))

    return np.mean(total_infected_counts)


networks = {
    "Star Graph": nx.star_graph(10),
    "Cycle Graph": nx.cycle_graph(10),
    "Scale-Free Graph": nx.barabasi_albert_graph(20, 2)
}

p = 0.3
A1 = {0}
A2 = {0, 1}
u = {2}

print(f"{'Network Type':<20} | s(A1) | s(A2) | Gain(A1+u) | Gain(A2+u)")
print("-" * 65)

for name, G in networks.items():
    s_A1 = simulate_sir_percolation(G, A1, p)
    s_A2 = simulate_sir_percolation(G, A2, p)
    s_A1_u = simulate_sir_percolation(G, A1 | u, p)
    s_A2_u = simulate_sir_percolation(G, A2 | u, p)

    gain_A1 = s_A1_u - s_A1
    gain_A2 = s_A2_u - s_A2

    print(f"{name:<20} | {s_A1:.2f} | {s_A2:.2f} | {gain_A1:.2f}      | {gain_A2:.2f}")