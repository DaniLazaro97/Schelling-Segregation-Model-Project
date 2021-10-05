'''Grid Class'''

import numpy as np
'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''
from initial_segregation import initial_segregation
from happiness import happiness
from policy_1 import relocation_policy1
from policy_2 import relocation_policy2
from friendship import initial_id_map
from policy_3_lazaro import relocation_policy3_lazaro, initial_id_map_policy_lazaro
from policy_3_chapa import relocation_policy3_chapa
from policy_3_martin import relocation_policy3_martin

class grid:
    
    def __init__(self):
        print('Grid was created.')
        self.l = 40
        self.n_agents = 1400
        self.k = 3
        self.p = 3
        self.q = 100
        self.n_friends = 5
        self.p_friends = 5
    def init_maps(self): #Initializes all the initial variables needed
        self.empty_map = np.zeros((self.l,self.l))
        self.same_race_map = np.zeros((self.l,self.l))
        self.segregation_intmap = initial_segregation(self.n_agents, self.l) #2d array with the distribution of the agents (Class: 0=Empty, 1=Blue, 2=Red)
        self.happiness_map = happiness(self.segregation_intmap, self.k, self.p) #2d array with distribution of happiness (State: 0=Empty, 1=Happy, -1=Unhappy)
        self.id_map = initial_id_map(self.n_agents, self.l, self.n_friends, self.segregation_intmap, self.happiness_map, self.k, self.p)
    def init_maps_policy_lazaro(self):
        self.empty_map = np.zeros((self.l,self.l))
        self.same_race_map = np.zeros((self.l,self.l))
        self.segregation_intmap = initial_segregation(self.n_agents, self.l)
        self.happiness_map = happiness(self.segregation_intmap, self.k, self.p)    
        self.id_map = initial_id_map_policy_lazaro(self.n_agents, self.l, self.n_friends, self.segregation_intmap, self.happiness_map, self.k, self.p)
    def segregation_update_policy1(self):
        self.segregation_intmap, self.happiness_map = relocation_policy1(self.segregation_intmap, self.happiness_map, self.k, self.p, self.q)
    def segregation_update_policy2(self):
        self.segregation_intmap, self.happiness_map, self.id_map = relocation_policy2(self.segregation_intmap, self.happiness_map, self.id_map, self.k, self.p, self.p_friends, self.q, self.n_friends)
    def segregation_update_policy3_lazaro(self):
        self.segregation_intmap, self.happiness_map, self.id_map = relocation_policy3_lazaro(self.segregation_intmap, self.happiness_map, self.id_map, self.k, self.p, self.p_friends, self.q, self.n_friends) 
    def segregation_update_policy3_chapa(self):
         self.segregation_intmap, self.happiness_map = relocation_policy3_chapa(self.segregation_intmap, self.happiness_map, self.k, self.p, self.q)
    def segregation_update_policy3_martin(self):
         self.segregation_intmap, self.happiness_map, self.id_map = relocation_policy3_martin(self.segregation_intmap, self.happiness_map, self.id_map, self.k, self.p, self.p_friends, self.q, self.n_friends)
