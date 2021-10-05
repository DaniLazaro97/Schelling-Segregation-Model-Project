'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Initial Segregation Map'''

import numpy as np
from random import shuffle


def initial_segregation(n_agents, l): 
    
    pos_list = [[i,j] for i in range(0,l) for j in range(0,l)]
    shuffle(pos_list)
    segregation_intmap = np.zeros((l,l))
    
    for i in range(0, int(n_agents/2)):
        blue_random_pos = pos_list[i]
        segregation_intmap[blue_random_pos[0], blue_random_pos[1]] = 1

        red_random_pos = pos_list[-(i+1)]
        segregation_intmap[red_random_pos[0], red_random_pos[1]] = 2

    return segregation_intmap


