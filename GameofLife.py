import numpy as np
import argparse
from matplotlib import pyplot as plt
from matplotlib import animation
from SeedDict import seeds


def initialize_world(seed = None, dimensions = (100, 100)):
    '''
    Places a Seed at the center of a world of 0s. Else, randomly initialize with 0s and 1s.

    Parameters
    ----------
    seed (str): Should match the names of Seeds in SeedDict.
    dimensions (tuple): World size.

    Output
    ------
    world (array)
    '''
    #Seed desired world if we have the seed and it's position.
    if (seed is not None):
        #World of zeros.
        world = np.zeros(dimensions)
        #Place seed at center of world. First calculate bounds.
        worl_x, worl_y = np.shape(world)
        seed_x, seed_y = np.shape(seed)
        upper_bound = int(np.ceil((worl_y / 2) + (seed_y / 2)))
        lower_bound = int(np.ceil((worl_y / 2) - (seed_y / 2)))
        right_bound = int(np.ceil((worl_x / 2) + (seed_x / 2)))
        lefts_bound = int(np.ceil((worl_x / 2) - (seed_x / 2)))
        #Within bounds, place seed.
        world[lefts_bound:right_bound, lower_bound:upper_bound] = seed
        return world
    #Random seeding when seed is undefined.
    elif (seed is None):
        world = np.random.randint(2, size = dimensions)
        return world

def game_logic(i, j, world, num_neighbour):
    '''
    Performs game logic when we have the neighbours of a given cell.

    Parameters
    ----------
    i (int): x co-ordinate of matrix.
    j (int): y co-ordinate of matrix
    world (array): World.
    num_neighbours (int): Neighbours of cell in World.

    Output
    ------
    0 or 1 (int): Dead or Alive cell depending on game logic.
    '''
    #A live cell that has 2 or 3 neighbours, lives.
    if ((num_neighbour == 2) | (num_neighbour == 3)) & (world[i][j] == 1):
        return 1
    #Otherwise, the live cell dies.
    elif ((num_neighbour != 2) | (num_neighbour != 3)) & (world[i][j] == 1):
        return 0
    #A dead cell that has 3 live neighbours lives.
    elif (num_neighbour == 3) & (world[i][j] == 0):
        return 1
    #Otherwise, the dead cell remains dead. 
    else:
        return 0

def next_state(array):
    '''
    Computes the next state of the World.

    Parameters
    ----------
    array (array): Current World state.

    Output
    ------
    nxt_stp (array): Next World state.
    '''
    #Prepare arrays.
    fil = np.ones((3, 3))
    pad = np.pad(array, (1, 1), mode = 'wrap')
    #Dimensions of result.
    res_x, res_y = np.shape(array)
    #Perform convolution.
    nxt_stp = np.zeros((res_x, res_y))
    for i in range(res_x):
        for j in range(res_y):
            #Subtract by 1 when value is 1. We shouldn't count the cell in question.
            nxt_stp[i][j] = np.sum(pad[i:i + 3, j:j + 3] * fil) - array[i][j]
            #Perform game logic.
            nxt_stp[i][j] = game_logic(i, j, array, nxt_stp[i][j])
    return nxt_stp

def states_of_game(world, generations):
    '''
    Creates a list of World states.

    Parameters
    ----------
    world (array): Initial state of World.
    generations (int): Number of states to compute.

    Output
    ------
    states (list): List of World states at each 'step'.
    '''
    #Array to save states. We include the initial state.
    states = [world]
    #Iteratively create states.
    for i in range(generations):
        world = next_state(world)
        states.append(world)
    return states

def animate(states):
    '''
    Creates a matplotlib animation from the list of World states.

    Parameters
    ----------
    states (list): List of World states at each 'step'.

    Output
    ------
    img_ani (matplotlib animation object)
    '''
    #Set object.
    fig = plt.figure(dpi = 100)
    plt.axis('off')
    #Create plot for each state.
    img_arr = []
    for state in states:
        img_arr.append((plt.imshow(state), ))
    #Animate.
    img_ani = animation.ArtistAnimation(fig, img_arr, interval = 300, repeat_delay = 3000, blit = True, repeat = True)
    return img_ani

def parse_var():
    '''
    Command line interface to obtain size, seed and generations to compute.

    Outputs
    -------
    size (tuple): World size. Default (100,100).
    stat (int): States of World to compute. Default 100.
    seed (str): Seed for World. Default 'Default'. Default maps to None in SeedDicts.py
    '''
    #Arguments.
    parser = argparse.ArgumentParser(description = 'Displays 100 generations of a randomly initialized 100 by 100 world.')
    parser.add_argument('-size', type = str, default = '100,100', help = 'World dimesion passed as a tuple.')
    parser.add_argument('-generations', type = int, default = 100, help = 'Generations of world.')
    parser.add_argument('-seed', type = str, default = 'Default', help = 'Seed to place in world.')
    args = parser.parse_args()
    #Parse arguments.
    size = (int(args.size.split(',')[0]), int(args.size.split(',')[1]))
    stat = args.generations
    seed = seeds[args.seed]
    return size, stat, seed


if __name__ == '__main__':
    #Generate variables.
    size, stat, seed = parse_var()
    #Compute states and animate.
    world = initialize_world(seed, size)
    states = states_of_game(world, stat)
    state_gif = animate(states)
    #Display
    plt.show()
