"""
DIHNOSIR Commands for Antibody Data
"""

# Author: Amir Shanehsazzadeh <amirshanehsazzadeh@college.harvard.edu>

import pickle

import dihnosir

X = pickle.load(open('antibody_dist.pickle', 'rb'))
Y = pickle.load(open('antibody_maxdist.pickle', 'rb'))

# Compute DIHNOSIR
strong_dist_clustering = dihnosir.DIHNOSIR(silhouette_threshold = 0).fit(X, unmerge = "strong")
strong_dist_labels = strong_dist_clustering.labels_
# Write result to a txt file
f = open('unpruned_strong_antibody_dist.txt', 'w')
for l_ in strong_dist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()

strong_maxdist_clustering = dihnosir.DIHNOSIR(silhouette_threshold = 0).fit(Y, unmerge = "strong")
strong_maxdist_labels = strong_maxdist_clustering.labels_
f = open('unpruned_strong_antibody_maxdist.txt', 'w')
for l_ in strong_maxdist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()

weak_dist_clustering = dihnosir.DIHNOSIR(silhouette_threshold = 0.7825).fit(X, unmerge = "weak")
weak_dist_labels = weak_dist_clustering.labels_
f = open('unpruned_weak_antibody_dist.txt', 'w')
for l_ in weak_dist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()

weak_maxdist_clustering = dihnosir.DIHNOSIR(silhouette_threshold = 0.7825).fit(Y, unmerge = "weak")
weak_maxdist_labels = weak_maxdist_clustering.labels_
f = open('unpruned_weak_antibody_maxdist.txt', 'w')
for l_ in weak_maxdist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()