import networkx as nx
from matplotlib import pyplot as plt

# question 1
G = nx.read_weighted_edgelist("course_network_l2.adjlist", nodetype=str)

print(max(dict(G.degree()).values()))

# question 2
degrees = dict(G.degree())
avg_degree = sum(degrees.values()) / len(degrees)

# Node sizes: larger if degree > average
node_sizes = [300 if degrees[n] <= avg_degree else 700 for n in G.nodes()]

# Edge widths proportional to weight
edge_weights = [G[u][v]['weight'] for u,v in G.edges()]
# Normalize weights
edge_widths = [w*0.5 for w in edge_weights]

# Find top-5 nodes by degree for labeling
top5_nodes = sorted(degrees, key=degrees.get, reverse=True)[:5]
labels = {n: n if n in top5_nodes else '' for n in G.nodes()}

# Draw the graph
plt.figure(figsize=(12,8))
pos = nx.spring_layout(G, seed=42)  # any layout you like
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue')
nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color='gray')
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10, font_weight='bold')

plt.title("Course Network Visualization")
plt.axis('off')
plt.tight_layout()
plt.show()