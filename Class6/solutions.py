import networkx as nx
import matplotlib.pyplot as plt
from collections import Counter

n = 500
m_values = [1, 3, 5]

for m in m_values:
    G = nx.barabasi_albert_graph(n, m)

    degrees = [deg for node, deg in G.degree()]
    degree_count = Counter(degrees)
    deg, cnt = zip(*sorted(degree_count.items()))

    plt.figure(figsize=(6, 4))
    plt.scatter(deg, cnt, color='blue')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Degree (k)')
    plt.ylabel('Number of nodes with degree k')
    plt.title(f'Barabasi-Albert Graph: n={n}, m={m}')
    plt.grid(True, which="both", ls="--", lw=0.5)
    plt.show()
