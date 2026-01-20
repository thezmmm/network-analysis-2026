# Helsinki Network Analysis

This repository contains my coursework and projects for the **Network Analysis** course at the **University of Helsinki**.  

The course focuses on:

- Graph theory and network representations  
- Network metrics: degree, density, clustering, centrality  
- Weighted and unweighted networks  
- Visualization of complex networks using Python (NetworkX, Matplotlib)  

## Project Highlights

1. **Course Network Visualization**  
   - Loading and analyzing a course network (`course_network_l2.adjlist`)  
   - Node sizes reflect degrees  
   - Edge thickness reflects number of shared topics  
   - Top-5 most connected courses labeled
2. **Network Centrality Analysis with PageRank**

   - Generating three synthetic networks: ER random graph, BA preferential attachment graph, WS small-world graph

   - Loading three real-world web networks and extracting their largest connected components

   - Computing PageRank and normalized degree for each node

   - Creating scatter plots comparing PageRank vs normalized degree

   - Visualizing networks with node color indicating PageRank and node size indicating degree
3. **Empirical Study of G(n, p) Random Graphs**

   - Generating G(n, p) graphs for fixed 𝑛 across different 𝑝 values

   - Measuring how often the graphs are connected and the average size of the largest component

   - Creating scatter plots showing connectivity frequency and largest component size vs 𝑝

   - Observing how increasing 𝑝 affects graph connectivity and component sizes

## Requirements

- Python >= 3.10  
- networkx  
- matplotlib
