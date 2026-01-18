import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Synthetic networks
G1 = nx.erdos_renyi_graph(n=100, p=0.05)
G2 = nx.barabasi_albert_graph(n=100, m=2)
G3 = nx.watts_strogatz_graph(n=100, k=4, p=0.1)
synthetic_networks = [G1, G2, G3]

# Real networks (SNAP)
# edge list files from https://snap.stanford.edu/data/
real_files = ["web-BerkStan.txt", "web-Google.txt", "web-NotreDame.txt"]
real_networks = []
for f in real_files:
    G = nx.read_edgelist(f, comments="#", nodetype=int)
    G.remove_edges_from(nx.selfloop_edges(G))
    real_networks.append(G)


# Helper functions
def largest_connected_subgraph(G, max_nodes=1000):
    if G.is_directed():
        components = list(nx.weakly_connected_components(G))
    else:
        components = list(nx.connected_components(G))

    largest = max(components, key=len)
    LCC = G.subgraph(largest).copy()  # largest connected component

    if len(LCC) > max_nodes:
        # chose a subgraph from LCC
        start = np.random.choice(list(LCC.nodes()))
        bfs_nodes = list(nx.bfs_tree(LCC, source=start))
        if len(bfs_nodes) > max_nodes:
            bfs_nodes = bfs_nodes[:max_nodes]
        return LCC.subgraph(bfs_nodes).copy()
    else:
        return LCC

def compute_measures(G):
    n = G.number_of_nodes()

    # PageRank
    pr = nx.pagerank(G, alpha=0.85)

    # Normalized degree
    if G.is_directed():
        deg = dict(G.in_degree())
    else:
        deg = dict(G.degree())
    norm_deg = {node: val / (n - 1) for node, val in deg.items()}

    return pr, norm_deg


def plot_scatter(pr, norm_deg, title):
    x = list(norm_deg.values())
    y = [pr[node] for node in norm_deg.keys()]

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c=y, cmap=plt.cm.RdBu, alpha=0.6)
    plt.xlabel("Normalized Degree")
    plt.ylabel("PageRank")
    plt.title(title)
    plt.colorbar(label="PageRank")
    plt.show()


def plot_network(G, pr, norm_deg, title):
    pos = nx.spring_layout(G, seed=42)
    node_sizes = [deg * 100 for deg in norm_deg.values()]
    node_colors = [pr[node] for node in G.nodes()]

    fig, ax = plt.subplots(figsize=(8, 8))
    nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors,
        cmap=plt.cm.RdBu, ax=ax
    )
    nx.draw_networkx_edges(G, pos, alpha=0.3, ax=ax)
    ax.set_title(title)
    ax.axis('off')

    sm = plt.cm.ScalarMappable(
        cmap=plt.cm.RdBu,
        norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors))
    )
    sm.set_array([])
    fig.colorbar(sm, ax=ax, label="PageRank")

    plt.show()


# Plot Synthetic Networks
for i, G in enumerate(synthetic_networks, 1):
    pr, norm_deg = compute_measures(G)
    plot_scatter(pr, norm_deg, f"Synthetic Network {i}: PageRank vs Normalized Degree")
    plot_network(G, pr, norm_deg, f"Synthetic Network {i}: Network Visualization")

# Plot Real Networks
for i, G in enumerate(real_networks, 1):
    G_vis = largest_connected_subgraph(G, max_nodes=500)
    print(f"G_vis Graph with {G_vis.number_of_nodes()} nodes and {G_vis.number_of_edges()} edges")
    pr, norm_deg = compute_measures(G_vis)
    plot_scatter(pr, norm_deg, f"Real Network {i}: PageRank vs Normalized Degree")
    plot_network(G_vis, pr, norm_deg, f"Real Network {i}: Network Visualization")
