'''Happiness% - Iteration Plot'''

'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

import numpy as np
import matplotlib.pyplot as plt

def iteration_verbose(happiness_map, metric, i, iterations):
    n_happy = len(list(np.where(happiness_map == 1))[1])
    metric.append(n_happy)
    if i%5 == 0:
        print(f'\nIteration:{i}')
        print(f'N Happy: {n_happy}\n')
    else:
        pass

    return metric

def agent_empty_counter(segregation_intmap):
    print('\nTo check if we mistakenly lost empty spots during the iterations:')
    n_blues= len(list(np.where(segregation_intmap == 1))[1])
    n_reds = len(list(np.where(segregation_intmap == 2))[1])
    n_huecos = len(list(np.where(segregation_intmap == 0))[1])
    
    print(f'n_blues: {n_blues}')
    print(f'n_reds: {n_reds}')
    print(f'n_huecos: {n_huecos}')
    
def iter_plot(metric, std_results, title):
    dpi = 1200
    n_iter = len(metric)
    iterations = [i for i in range(n_iter)]
    n_happy = []
    for iteration in metric:
        n_happy.append(iteration)
    plt.errorbar(iterations, n_happy, std_results, ecolor='r', elinewidth=0.6, fmt = 'none')    
    plt.plot(iterations, n_happy, color = 'grey', linewidth = 0.75, marker='.', markersize = 0.2)
    plt.title(title)
    plt.xlabel('Iter')
    plt.ylabel('N Happies ')
    plt.xticks(iterations, fontsize = 7)

    plt.savefig(f'results/ {title}.png', dpi = dpi)
    plt.show()
    
    
        
    