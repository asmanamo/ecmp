# SLP: ECMP Hash Collision Profiler

The underlying math here is the **Birthday Paradox** [[3](https://www.kaggle.com/code/hmnshudhmn24/the-birthday-paradox-a-python-simulation)]. If you have an ECMP width of `N` paths, and you hash `K` massive Elephant Flows into them, the probability of at least one collision (where two flows hit the same link and cause congestion) grows shockingly fast.

### The Math (Collision Probability)
Here is the formula we are calculating:

    P(collision) = 1 - [ (N/N) * ((N-1)/N) * ((N-2)/N) * ... * ((N-K+1)/N) ]

Where:
1. **N** = Total number of ECMP paths (e.g., 64)
2. **K** = Number of active Elephant Flows (e.g., 12)

Even with a 64-way ECMP fabric, hashing just 12 AI Elephant Flows creates a ~67% chance of a collision. This mathematically proves why static hashing fails for AI workloads and why Dynamic Load Balancing (DLB) or packet spraying is required.

### Usage
Run the Python script to test your own fabric designs and calculate the collision probability for your specific topology [[5](https://www.probabilisticworld.com/birthday-problem-python-simulation/)].
