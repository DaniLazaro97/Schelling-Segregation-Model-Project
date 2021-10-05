'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Friendship Map'''
import numpy as np
from random import choice
from random import shuffle

from unhappy_and_empty_lists import unhappy_and_empty_info_extraction_for_policies
from happiness import coord_change


def initial_friendship(n_agents, n_friends): #Initializes the friends of each agent
    id_agents = [int(i) for i in range(1, n_agents+1)]
    friendship = [] 
    for i in id_agents:
        friends = [] 
        while len(friends) <= n_friends:
            friend = choice(id_agents)
            if friend not in friends:
                friends.append(friend)
        friendship.append(friends)
        
    return friendship


#Initializes the tensor that has all the information about the Social Network
def initial_id_map(n_agents, l, n_friends, segregation_intmap, happiness_map, k, p): 
    id_agents = [i for i in range(1, n_agents+1)]
    shuffle(id_agents)
    id_map = np.zeros((n_friends+1, l,l))
    #we just need the empties but whatever...
    empties, unhappies = unhappy_and_empty_info_extraction_for_policies(segregation_intmap, happiness_map, k, p)
    friendship = initial_friendship(n_agents, n_friends)
    counter = 0
    
    
    
    for i in range(l):
        for j in range(l):
            if segregation_intmap[i,j] != 0:
                info_cell = []
                friends = friendship[counter]
                agent = id_agents[counter]
                info_cell.append(agent)
                for f in friends:
                    info_cell.append(f)
                
                for w in range (n_friends+1):
                    id_map[w,i,j] = info_cell[w]  
                
                counter += 1
    
    return id_map
    
#Finds the information abou the friends of an agent
def agent_and_friends_coords(id_agent, id_map, n_friends):
    coords_agent = np.where(id_map[0] == id_agent)
    coords_agent = [coords_agent[0][0],coords_agent[1][0]]

    id_friends = [int(id_map[i, coords_agent[0], coords_agent[1]]) for i in range(1, n_friends+1)]
    
    coords_friends = [np.where(id_map[0] == i) for i in id_friends]

    
    coords_friends = [[i[0][0], i[1][0]] for i in coords_friends]

    return coords_agent, coords_friends, id_friends

    
    
def neighborhood_coords_search(coords_friends, l,k,p): 
    #this function finds all the coordinates of the neighbors of the friends
    
    #we are going to return all those coordinates in a list
    #empty and not empty spots, because the agents move one at a time
    #that means that if one moves and leaves an empty spot that spot could be neighbor of a friend of the 
    #next agent that moves...
    
    l_side = l
    w = int((p-1)/2)
    neighbor_coords = []
    for coords in coords_friends:
        i = coords[0]
        j = coords[1]

        for k in list(range(i-w, i+w+1)): #change of coordinates 
                k_hat = coord_change(k,l_side)
                for l in list(range(j-w, j+w+1)):
                    l_hat = coord_change(l,l_side)
                    append_condition =  [i,j] != [k_hat,l_hat] and not [k_hat,l_hat] in neighbor_coords
                    #we don't want to count the center cell [i,j]
                    if append_condition: neighbor_coords.append([k_hat, l_hat])
    
    return neighbor_coords




