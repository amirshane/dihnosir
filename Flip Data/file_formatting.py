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
    
    x_angles, y_angles = rama_data[x], rama_data[y]
    for i in range(8):
        d = abs(x_angles[i] - y_angles[i])
        d = min(d, 360-d)
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
    size = len(lines)
    separation_matrix = np.asarray([0.0 for i in range(size**2)]).reshape(size, size)
    pairs = itertools.combinations([i for i in range(size)], r = 2)
    
    formatted_lines = []
    for i in range(size):
        line = lines[i].split()
        line = line[::-1][4:12]
        line = [float(line[j]) for j in range(8)]
        formatted_lines.append(line)
    
    for pair in pairs:
        x, y = pair[0], pair[1]
        separation = max_phipsi_separation(formatted_lines, x, y)
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
separation_matrix_creator('flip_out.txt', 'flip_separation.pickle')