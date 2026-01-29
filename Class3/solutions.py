import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Number of nodes
n = 500

# Range of p values to test
p_values = np.linspace(0, 0.05, 20)  # small p, because large n -> connectivity changes at small p

# Number of repetitions per p to estimate empirical frequencies
repeats = 50


connected_freq = []
largest_cc_size = []

for p in p_values:
    connected_count = 0
    largest_sizes = []

    for _ in range(repeats):
        G = nx.gnp_random_graph(n, p)

        if nx.is_connected(G):
            connected_count += 1

        # Size of largest connected component
        largest_cc = max(nx.connected_components(G), key=len)
        largest_sizes.append(len(largest_cc))

    connected_freq.append(connected_count / repeats)
    largest_cc_size.append(np.mean(largest_sizes))


plt.figure(figsize=(8,5))
plt.scatter(p_values, connected_freq, color='blue')
plt.xlabel("p")
plt.ylabel("Fraction of connected graphs")
plt.title(f"Connectivity of G(n={n}, p)")
plt.grid(True)
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(p_values, largest_cc_size, color='red')
plt.xlabel("p")
plt.ylabel("Average size of largest component")
plt.title(f"Largest connected component in G(n={n}, p)")
plt.grid(True)
plt.show()


