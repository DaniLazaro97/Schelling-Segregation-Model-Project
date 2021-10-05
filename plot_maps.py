'''Group: Almudena Chapa, Daniel Lazaro, Jon Ander Martin'''

'''Plot Maps'''

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def plot_map(map_to_plot, map_type, title,i):
    dpi = 1000
    n_different_values = how_many_different_values(map_to_plot)
    if map_type == 'Happiness':
        if n_different_values == 3:
            cmap = ListedColormap(['k', 'w', (255/255,200/255,42/255)])
        elif n_different_values == 2:
            cmap = ListedColormap(['w', (255/255,200/255,42/255)])
    elif map_type == 'Agents':
        cmap = ListedColormap(['w', 'b', 'r'])
    else:
        print('Error, choose the map_type: Happiness or Agents')
        
    plt.matshow(map_to_plot, cmap = cmap)
    plt.title(f'{title} - Iter: {i}')

    if map_type == 'Happiness':
        plt.savefig(f'happiness/{i}.png', dpi = dpi)
    elif map_type == 'Agents':
        plt.savefig(f'segregation/{i}.png', dpi = dpi)
        

    plt.show()

def how_many_different_values(map_to_plot):
    diff_list = [] 
    map_to_plot = map_to_plot.reshape(-1,)
    for i in map_to_plot:
        if  not i in diff_list:
            diff_list.append(i)
    count = len(diff_list)
    return count
            