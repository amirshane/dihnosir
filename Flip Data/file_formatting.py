"""
File Formatting for Flip Data
"""

# Author: Amir Shanehsazzadeh <amirshanehsazzadeh@college.harvard.edu>

import pickle
import itertools

import numpy as np

def dist_matrix_creator(distanceFile, dumpFile):
    """Create and save distance matrix given file of n^2 distance measures.
    
    Parameters
    ----------
    distanceFile : txt file containing n^2 distance measures
         File of distance measures.
         
    dumpFile : pickle file 
         File where dist_matrix is dumped.
    
    Returns
    -------
    dist_matrix : array, shape = [n, n]
         n x n matrix of distance measures.
    
    """
    f = open(distanceFile, 'r')
    distances = f.readlines()
    size = int(np.sqrt(len(distances)))
    dist_matrix = np.asarray(distances).reshape(size, size).astype(np.float)
    f.close()

    pickle_out = open(dumpFile, "wb")
    pickle.dump(dist_matrix, pickle_out)
    pickle_out.close()
    
    return dist_matrix


def max_phipsi_separation(rama_data, x, y):
    """Calculate max angular separation between datums x and y.
    
    Parameters
    ----------
    rama_data : array, shape = [n]
         Array representing the flip data.
    
    x, y : int, int
         Integers representing datums in the data set.
    
    Returns
    -------
    max_separation : float
         Maximum angular separation between datums x and y.
    
    """
    rama_data = np.asarray(rama_data)
    max_separation = 0
    
    for i in range(4):
        x_string = rama_data[4*x+i].split()
        x_phi, x_psi = float(x_string[3]), float(x_string[4])
        y_string = rama_data[4*y+i].split()
        y_phi, y_psi = float(y_string[3]), float(y_string[4])
        d_phi = min(abs(x_phi-y_phi), 360-abs(x_phi-y_phi))
        d_psi = min(abs(x_psi-y_psi), 360-abs(x_psi-y_psi))
        d = max(d_phi, d_psi)
        max_separation = max(max_separation, d)
    
    return max_separation


def separation_matrix_creator(ramaFile, pickleFile):
    """Creates and saves separation matrix given flip data file.
    
    Parameters
    ----------
    ramaFile : txt file
        File representing the flip data.
        
    dumpFile : pickle file 
         File where separation_matrix is dumped.
    
    Returns
    -------
    separation_matrix : array, shape = [n, n]
         n x n matrix of maximum angular separation values.
    
    """
    f = open(ramaFile, 'r')
    lines = f.readlines()[1:]
    size = len(lines)//4 
    separation_matrix = np.asarray([0.0 for i in range(size**2)]).reshape(size, size)
    pairs = itertools.combinations([i for i in range(size)], r = 2)
    
    for pair in pairs:
        x, y = pair[0], pair[1]
        separation = max_phipsi_separation(lines, x, y)
        separation_matrix[x][y] += separation
        separation_matrix[y][x] += separation
    
    f.close()
    
    pickle_out = open(pickleFile, "wb")
    pickle.dump(separation_matrix, pickle_out)
    pickle_out.close()
    return separation_matrix


# Commands to format files
dist_matrix_creator('flip_dist.txt', 'flip_dist.pickle')
dist_matrix_creator('flip_maxdist.txt', 'flip_maxdist.pickle')
separation_matrix_creator('flip_plot.txt', 'flip_separation.pickle')
