# **Complex Systems Homework 2** 

### *Almudena Chapa, Dani Lazaro, Jon Ander Martin*
#### *April 12, 2021*

In this paper we will explore Thomas Schelling's model of segregation. In this model there is a certain number of agents, divided into 2 classes. The agents are happy if they have enough neighbors of their same class. The agents relocate using different policies, always looking for a spot where they are happier. In the following sections, we will present different relocation policies and study how each of them affects the distribution of the agents. 

In this work, we will apply Schelling's model in a 40x40 bi-dimensional grid. To avoid edge effects, the boundaries of the grid are periodic. The population of agents is N = 1400, and their position is assigned randomly at the beginning of each simulation. Note that this leaves 200 empty locations, a 12:5% of the total space. An agent is “happy" if more than 3 out of its 8 neighbors belong to its same class. All the simulations are performed over 20 epochs. In every epoch, all the unhappy agents try to move in a random order. The simulation for each of the cases is run 30 times and the results are averaged.
