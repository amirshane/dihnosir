"""
DIHNOSIR: Density Independent High Noise Optimized Sorting by Iterative \
Reduction
"""

# Author: Amir Shanehsazzadeh <amirshanehsazzadeh@college.harvard.edu>
#
# License: GNU GPL

import dihnosir_helper as dh

def strong_dihnosir(X, n = 100, minPts_min = 3, silhouette_threshold = 0.75, 
                    ssi_threshold = 1, metric = 'precomputed'):
    """Perform Strong DIHNOSIR clustering from vector array or distance matrix.
      
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
         
    ssi_threshold : float
         Minimum Simpson's similarity between two subclusters for edge drawing.
         
    metric : string, or callable
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        allowed by sklearn. If X is the distance array itself, use \ 
        ``metric="precomputed"`.
        
    Returns
    -------
    labels : array, shape = [n_samples]
         Predicted labels for each sample.
    
    """
    if (not type(n) == int and not n > 0):
        raise ValueError("n must be a positive integer.")
    
    if (not type(minPts_min) == int and not minPts_min > 0):
        raise ValueError("minPts_min must be a positive integer.")
        
    if (silhouette_threshold < -1 or silhouette_threshold > 1):
        raise ValueError("silhouette_treshold must be between -1 and 1.")
    
    if (ssi_threshold < 0 or ssi_threshold > 1):
        raise ValueError("ssi_treshold must be between 0 and 1.")
        
    subclusters_ = dh.subclusters(X, n, minPts_min, silhouette_threshold, 
                                  metric)
    unmerged_subclusters = dh.strong_unmerge(subclusters_)
    similarity_matrix_ = dh.similarity_matrix(unmerged_subclusters)
    graphs_ = dh.graphs(similarity_matrix_, ssi_threshold)
    labels = dh.clusters(X, unmerged_subclusters, graphs_)
    
    return labels


def weak_dihnosir(X, n = 100, minPts_min = 3, metric = 'precomputed', 
                  silhouette_threshold = 0.75, ssi_threshold = 1):
    """Perform Weak DIHNOSIR clustering from vector array or distance matrix.
      
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
         
    ssi_threshold : float
         Minimum Simpson's similarity between two subclusters for edge drawing.
         
    metric : string, or callable
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        allowed by sklearn. If X is the distance array itself, use \ 
        ``metric="precomputed"`.
        
    Returns
    -------
    labels : array, shape = [n_samples]
         Predicted labels for each sample.
    
    """
    if (not type(n) == int and not n > 0):
        raise ValueError("n must be a positive integer.")
    
    if (not type(minPts_min) == int and not minPts_min > 0):
        raise ValueError("minPts_min must be a positive integer.")
        
    if (silhouette_threshold < -1 or silhouette_threshold > 1):
        raise ValueError("silhouette_treshold must be between -1 and 1.")
    
    if (ssi_threshold < 0 or ssi_threshold > 1):
        raise ValueError("ssi_treshold must be between 0 and 1.")
        
    subclusters_ = dh.subclusters(X, n, minPts_min, silhouette_threshold, 
                                  metric)
    unmerged_subclusters = dh.weak_unmerge(subclusters_, ssi_threshold)
    similarity_matrix_ = dh.similarity_matrix(unmerged_subclusters)
    graphs_ = dh.graphs(similarity_matrix_, ssi_threshold)
    labels = dh.clusters(X, unmerged_subclusters, graphs_)
    
    return labels


class DIHNOSIR:
    """Perform DIHNOSIR clustering from vector array or distance matrix.
      
    Parameters
    ----------
    X : array or sparse (CSR) matrix of shape (n_samples, n_features), or \
            array of shape (n_samples, n_samples)
        A feature array, or array of distances between samples if
        ``metric='precomputed'``.
    
    unmerge : string
         Use 'strong' for strong unmerge and 'weak' for weak unmerge.
    
    n : int
         Number of iterations done between minimum and maximum eps values.
         
    minPts_min : int
         Smallest value of minPts (min_samples) considered.
    
    silhouette_threshold : float
         Minimum average of silhouette_sample scores for cluster retention.
         
    ssi_threshold : float
         Minimum Simpson's similarity between two subclusters for edge drawing.
         
    metric : string, or callable
        The metric to use when calculating distance between instances in a
        feature array. If metric is a string, it must be one of the options
        allowed by sklearn. If X is the distance array itself, use \ 
        ``metric="precomputed"`.
        
    Returns
    -------
    labels : array, shape = [n_samples]
         Predicted labels for each sample.
    
    """
    
    
    def __init__(self, n = 100, minPts_min = 3, metric = 'precomputed', 
                 silhouette_threshold = 0.75, ssi_threshold = 1):
        self.n = n
        self.minPts_min = minPts_min
        self.metric = metric
        self.silhouette_threshold = silhouette_threshold
        self.ssi_threshold = ssi_threshold
        
    
    def fit(self, X, unmerge):
        """Perform DIHNOSIR clustering from vector array or distance matrix.
          
        Parameters
        ----------
        X : array or sparse (CSR) matrix of shape (n_samples, n_features), or \
                array of shape (n_samples, n_samples)
            A feature array, or array of distances between samples if
            ``metric='precomputed'``.
                
        unmerge : string
             Use 'strong' for strong unmerge and 'weak' for weak unmerge.
        
        """
        
        if unmerge == 'strong':
            clus = strong_dihnosir(X, **self.get_params())
        
        elif unmerge == 'weak':
            clus = weak_dihnosir(X, **self.get_params())
            
        else:
            raise ValueError("unmerge must be either 'strong' or 'weak'.")
        
        self.labels_ = clus
        
        return self