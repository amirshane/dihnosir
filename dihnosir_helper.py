"""
Helper Functions for DIHNOSIR: Density Independent High Noise Optimized \ 
Sorting by Iterative Reduction
"""

# Author: Amir Shanehsazzadeh <amirshanehsazzadeh@college.harvard.edu>
#
# License: GNU GPL

import itertools

import numpy as np
import networkx as nx
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_samples


def cluster_constraint(labels):
    """Determine whether a cluster is merged or not.
    
    Returns True if cluster is unmerged, else False. User must define how to 
    determine whether or not a cluster is merged or not. Additional parameters 
    should be added as needed.
    
    Parameters
    ----------
    labels : array, shape = [n_samples]
         Predicted labels for each sample.
    
    Returns
    -------
    unmerged : True if unmerged, False if merged. 
        
    """
    unmerged = True
    
    # Write merge detection code.
    
    return unmerged


def scores(X, labels, metric):
    """Compute average of silhouette sample scores for clusters given labels.
    
    Returns list containing value -1 given one cluster.
    Returns empty list if zero clusters are given.
    
    Parameters
    ----------
    X : array or sparse (CSR) matrix of shape (n_samples, n_features), or \
            array of shape (n_samples, n_samples)
        A feature array, or array of distances between samples if
        ``metric='precomputed'``.
    
    labels : array, shape = [n_samples]
         Predicted labels for each sample.
         
    metric : string, or callable
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        allowed by sklearn. If X is the distance array itself, use \ 
        ``metric="precomputed"``.
    
    Returns
    -------
    scores : array, shape = [n_clusters]
         Average of silhouette sample scores for each cluster.
         
    """
    scores = np.asarray([])
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    
    if (2 <= n_clusters <= len(X)-1):
        samples = silhouette_samples(X, labels, metric = metric)
    elif (n_clusters == 1):
        return [-1]
    else:
        return []
        
    for i in range(n_clusters):
        indices = [k for k, val in enumerate(labels) if val==i]
        score = np.sum(samples[np.asarray(indices)])/len(indices)
        scores = np.append(scores, np.asarray([score]))
            
    return scores


def ssi(clus1, clus2):
    """Calculate Simpson's similarity betwen two clusters.
    
    Parameters
    ----------
    clus1 : array, shape = [n]
         Subset of data of size n.
         
    clus2 : array, shape = [m]
         Subset of data of size m.
    
    Returns
    -------
    ssi : float
         Simpson's similarity between clus1 and clus 2.     
    
    """
    ssi = len(set(clus1).intersection(set(clus2)))/min(len(clus1), len(clus2))
    
    return ssi

def unique(subclusters):
    """Determine unique subclusters.
    
    Parameters
    ----------
    subclusters : array, shape = [n_subclusters]
         Set of n_subclusters subsets of the data.
    
    Returns
    -------
    unique_sub : array, shape = [n_unique_subclusters]
         Set of n_unique_subclusters subsets of the data.   
    
    """
    unique_sub = [np.asarray(y) for y in set(tuple(x) for x in subclusters)]
    
    return unique_sub


def subclusters(X, n, minPts_min, silhouette_threshold, metric = 'precomputed'):
    """Removes merged clusters using cluster constraint.
    
    Parameters
    ----------
    X : array or sparse (CSR) matrix of shape (n_samples, n_features), or \
            array of shape (n_samples, n_samples)
        A feature array, or array of distances between samples if
        ``metric='precomputed'``.
    
    n : int
         Number of iterations done between minimum and maximum eps values.
         
    minPts_min : int
         Smallest value of minPts (min_samples) considered.
    
    silhouette_threshold : float
         Minimum average of silhouette_sample scores for cluster retention.
         
    metric : string, or callable
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        allowed by sklearn. If X is the distance array itself, use \ 
        ``metric="precomputed"``.
    
    Returns
    -------
    subclusters_ : array, shape = [n_subclusters_]
         Set of n_subclusters_ subsets of the data
    
    """
    subclusters_ = []
    indices = np.asarray([i for i in range(len(X))])

    minPts = minPts_min
    minPts_max = len(X)
    d_minPts = 1
    
    eps_min = min(X.reshape(1, -1)[0])
    eps_max = max(X.reshape(1, -1)[0])
    d_eps = (eps_max - eps_min)/n
    
    db_matrix = [[] for j in range(minPts_max - minPts_min + 1)]
    silhouette_matrix = [[] for j in range(minPts_max - minPts_min + 1)]
    
    break_count = 0
    while(minPts <= minPts_max):
        i = minPts - minPts_min
        eps = eps_min + d_eps
        while(eps <= eps_max):
            db = DBSCAN(eps, minPts, metric = metric).fit(X)
            n_clusters = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
            
            if (n_clusters == 1):
                if (eps == eps_min + d_eps):
                    break_count += 1
                    if (break_count == 10):
                        break_count = 0
                        d_minPts *= 10
                        break
                    else:
                        break
                else:
                    break_count = 0
                    break
            if (break_count == 10):
                d_minPts *= 10
                
            db_matrix[i].append(np.asarray([db.labels_, db.core_sample_indices_]))
            silhouette_matrix[i].append(scores(X, indices, db.labels_))
            
            eps += d_eps
        minPts += d_minPts
    
    db_matrix = np.asarray(db_matrix)
    silhouette_matrix = np.asarray(silhouette_matrix)
    
    for i in range(len(db_matrix)):
        row = db_matrix[i]
        for j in range(len(row)):
            labels, core_sample_indices = row[j][0], row[j][1]
            core_samples_mask = np.zeros_like(labels, dtype=bool)
            core_samples_mask[core_sample_indices] = True
            unique_labels = set(labels)
            for k in zip(unique_labels):
                class_member_mask = (labels == k)
                subcluster = indices[class_member_mask & core_samples_mask]
                if (len(subcluster) > 0):
                   if (silhouette_matrix[i][j][k[0]] >= silhouette_threshold):
                       subclusters_.append(subcluster)

    subclusters_ = unique(subclusters_)
    subclusters_ = sorted(subclusters_, key = len)
    subclusters_ = np.asarray(subclusters_)
    
    return subclusters_


def strong_unmerge(subclusters):
    """Removes merged clusters using cluster constraint.
    
    Parameters
    ----------
    subclusters : array, shape = [n_subclusters]
         Set of n_subclusters subsets of the data.
    
    Returns
    -------
    unmerged_subclusters : array, shape = [n_unmerged_subclusters]
         Subset of subclusters of size n_unmerged_subclusters.
    
    """
    unmerged_subclusters = []
    for subcluster in subclusters:
        if cluster_constraint(subcluster):
            unmerged_subclusters.append(subcluster)
    unmerged_subclusters = np.asarray(unmerged_subclusters)
    
    return unmerged_subclusters


def weak_unmerge(subclusters, ssi_threshold):
    """Removes merged clusters using directed graphs approach.
    
    Parameters
    ----------
    subclusters : array, shape = [n_subclusters]
         Set of n_subclusters subsets of the data.
    
    ssi_threshold : float
         Minimum Simpson's similarity between two subclusters for edge drawing.
         
    Returns
    -------
    unmerged_subclusters : array, shape = [n_unmerged_subclusters]
         Subset of subclusters of size n_unmerged_subclusters.
    
    """
    indices = np.asarray([i for i in range(len(subclusters))])
    di_graph_ = nx.DiGraph()
    di_graph_.add_nodes_from(indices)
    
    chains = []
    while (len(indices) > 0):
        index = indices[0]
        chain = [index]
        indices = indices[1:]
        for i in range(len(indices)):
            if ssi(subclusters[index], subclusters[indices[i]]) >= ssi_threshold:
                chain.append(indices[i])
        chains.append(chain)

    for chain in chains:
        for i in range(len(chain)-1):
            di_graph_.add_edge(chain[0], chain[i+1])

    di_graph_ = nx.transitive_reduction(di_graph_)
    
    potentially_unmerged_subclusters = []
    unmerged_subclusters = []
    merged_subclusters = []
    for i in range(len(subclusters)):
        if di_graph_.in_degree(i) <= 1:
            potentially_unmerged_subclusters.append(list(subclusters[i]))
        elif di_graph_.in_degree(i) > 1:
            merged_subclusters.append(list(subclusters[i]))
        else:
            pass
        
    for subcluster in potentially_unmerged_subclusters:
        for merged_subcluster in merged_subclusters:
            if len(subcluster) >= len(merged_subcluster):
                if ssi(subcluster, merged_subcluster) >= ssi_threshold:
                    break
        else:
            continue
        unmerged_subclusters.append(subcluster)
    
    unmerged_subclusters = unique(unmerged_subclusters)
    unmerged_subclusters = np.asarray(unmerged_subclusters)
    
    return unmerged_subclusters


def similarity_matrix(subclusters):
    """Create matrix of Simpson's similarity scores between subclusters.
    
    Parameters
    ----------
    subclusters : array, shape = [n]
         Set of n subsets of the data.
    
    Returns
    -------
    similarity_matrix : array, shape = [n_subclusters, n_subclusters]
         Matrix of Simpson's similarity scores between subclusters.
        
    """
    n_subclusters = len(subclusters)
    sim_matrix = np.asarray([0.0 for i in range(n_subclusters**2)])
    sim_matrix = np.reshape(sim_matrix, (n_subclusters, n_subclusters))
    print(len(sim_matrix))
    cluster_pairs = itertools.combinations(subclusters, r = 2)
    for cluster_pair in cluster_pairs:
        x, y = cluster_pair[0], cluster_pair[1]
        x_index, y_index = list(subclusters).index(x), list(subclusters).index(y)
        x_set, y_set = set(x), set(y)
        similarity = ssi(x_set, y_set)
        sim_matrix[x_index][y_index] += similarity
        sim_matrix[y_index][x_index] += similarity

    return sim_matrix


def graphs(similarity_matrix, ssi_threshold):
    """Create graph of subclusters and determine connected components.
    
    Parameters
    ----------
    similarity_matrix : array, shape = [n_subclusters, n_subclusters]
         Matrix of Simpson's similarity scores between subclusters.
         
    ssi_threshold : float
         Minimum Simpson's similarity between two subclusters for edge drawing.
    
    Returns
    -------
    subcluster_connected_components : array, shape = [n]
         Array of n connected components with nodes being subclusters.
    
    """
    indices = [i for i in range(len(similarity_matrix))]
    cluster_graph = nx.Graph()
    cluster_graph.add_nodes_from(indices)
    
    subcluster_pairs = itertools.combinations(indices, r = 2)
    for subcluster_pair in subcluster_pairs:    
        x_index, y_index = subcluster_pair[0], subcluster_pair[1]
        similarity = similarity_matrix[x_index][y_index]
        if similarity >= ssi_threshold:
            cluster_graph.add_edge(x_index, y_index,)

    subcluster_connected_components = nx.connected_component_subgraphs(cluster_graph)
    
    return subcluster_connected_components


def clusters(X, unmerged_subclusters, subcluster_connected_components):
    """Create graph of subclusters and determine connected components.
    
    Parameters
    ----------
    X : array or sparse (CSR) matrix of shape (n_samples, n_features), or \
            array of shape (n_samples, n_samples)
        A feature array, or array of distances between samples if
        ``metric='precomputed'``.
    
    unmerged_subclusters : array, shape = [n_unmerged_subclusters]
         Subset of subclusters of size n_unmerged_subclusters.
         
    subcluster_connected_components : array, shape = [n]
         Array of n connected components with nodes being subclusters.
         
    Returns
    -------
    labels : array, shape = [n_samples]
         Predicted labels for each sample.
    
    """ 
    labels = np.asarray([-1 for i in range(len(X))])
    indices = [i for i in range(len(X))]
    clusters_ = []
    for graph in subcluster_connected_components:
        cluster = []
        for node in graph.nodes():
            cluster.append(unmerged_subclusters[node])
        cluster = set().union(*cluster)
        clusters_.append(cluster)
    
    noise = set(indices).difference(set().union(*clusters_))
    clusters_ = sorted(clusters_, key = 1)[::-1]
    clusters_.append(noise)
    clusters_ = clusters_[::-1]
    
    for i in range(len(clusters_)):
        cluster = clusters_[i]
        labels[list(cluster)] += i
    
    return labels
