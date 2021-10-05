'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''___________MAIN_PROGRAM___________'''

from grid import grid
from plot_maps import plot_map
from metrics_plot import iteration_verbose, agent_empty_counter, iter_plot
import numpy as np


#Instructions: This is the script of the main program that runs the Schelling's Segregation Model.
#Section 1: To define the parameters of the model.
      #l: length L of the L x L Grid.
      #k: Happiness threshold.
      #q: Number of empty spots that are randomly selected by policy 1.
      #n_friends: Number of friends of an agent used in policy 2.
      #p_friends: the size of the neighborhood that the friends explore in policy 2.
#Section 2: Runs the main loop and calculates the average results. You can select also select the policy.
      #n_runs: The number of runs of the same model.
      #n_iterations: The number of epochs of each run.
      #Policy Selection: Line 77. Possible policies:
          #grid.segregation_update_policy1()
          #grid.segregation_update_policy2()
          #User defined Policies:
              #grid.segregation_update_policy3_chapa() --> Almudena Chapa : Diverse Communities.
              #grid.segregation_update_policy3_lazaro() --> Daniel Lazaro : Same class Social Network.
                  #This policy requires a different initialization for the id map (map of the id's of the agents)
                  #Activate line 67, deactivate line 66.
              #grid.segregation_update_policy3_martin() --> Jon Ander Martin : Selfish Social Network.
#Section 3: Plots the final Segregation and Happiness of the last run and plots the average curve of results.
      #Meaning of the Colors:
          #Segregation map:
              # White -> Empty (0)
              # Blue -> Blue Class (1)
              # Red -> Red Class (2)
          #Happiness map:
              # White -> Empty (0)
              # Yellow -> Happy Agent (1)
              # Black -> Unhappy Agent (-1)
      
          
'''Section 1'''
#Parameters of the Segreagation Model:
grid = grid()
grid.l = 40
grid.k = 3
#policy 1:
grid.q = 100
#policy 2:
grid.n_friends = 5
grid.p_friends = 3


if round(grid.l**2*7/8)%2 == 0:
    grid.n_agents = round(grid.l**2*7/8)
else: grid.n_agents = round(grid.l**2*7/8) - 1
#if you want a different polpulation activate the line below and set the number that you desire.
#grid.n_agents =

'''Section 2'''
n_runs = 2
n_iterations = 20
results =np.zeros((n_runs, n_iterations+1)) #variable that stores the results of every run and epoch

for j in range(n_runs):
    grid.init_maps()
    #grid.init_maps_policy_lazaro() #if you are using policy3_lazaro activate this line and deactivate the previous one

    print(f'RUN: {j}')
    print(f'Creating {grid.n_agents} agents and {grid.l**2 - grid.n_agents} empty spots ')

    run_results = []
    run_results = iteration_verbose(grid.happiness_map, run_results, 0, n_iterations)
    
    for i in range(1,n_iterations+1):

        grid.segregation_update_policy1()
        run_results = iteration_verbose(grid.happiness_map, run_results, i, n_iterations)
        
    results[j] = np.reshape(np.array(run_results), (n_iterations+1,))
    
mean_results = results.mean(axis = 0) 
std_results = results.std(axis = 0)   

'''Section 3'''
plot_map(grid.segregation_intmap,'Agents', 'Final Distribution of the Agents',i)
plot_map(grid.happiness_map, 'Happiness', 'Final Happiness Map',i)

agent_empty_counter(grid.segregation_intmap) #just to check for errors
iter_plot(mean_results, std_results, '') 






