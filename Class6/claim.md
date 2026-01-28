Claim

Consider a set of pages 1,2,…,N each creating **just one outbound link**. Let Lℓ(t) denote the number of in-links to page ℓ after t pages. If a new page j chooses a random earlier page i and copies i's link (the “copying model”), then

P(page j links to ℓ∣copying)=Lℓ(j−1)/j−1.

that is, the linking probability is **proportional to the current popularity** of page ℓ



Proof

Let A_j denote the page that j links to. Conditional on copying, we have
$$
P(A_j = \ell \mid \text{copying}) = \sum_{i=1}^{j-1} P(i \text{ is chosen}) \cdot \mathbf{1}_{\{i \text{ links to } \ell\}},
$$
Since i is chosen uniformly at random from (i,j-1),
$$
P(i \text{ is chosen}) = \frac{1}{j-1}
$$

$$
P(A_j = \ell \mid \text{copying}) = \sum_{i \text{ linking to } \ell} \frac{1}{j-1} = \frac{L_\ell(j-1)}{j-1}.
$$

