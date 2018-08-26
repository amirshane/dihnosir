"""
DIHNOSIR Commands for Flip Data
"""

# Author: Amir Shanehsazzadeh <amirshanehsazzadeh@college.harvard.edu>

import pickle

import dihnosir

X = pickle.load(open('flip_dist.pickle', 'rb'))
Y = pickle.load(open('flip_maxdist.pickle', 'rb'))

# Compute DIHNOSIR
strong_dist_clustering = dihnosir.DIHNOSIR(n = 250, silhouette_threshold = 0).fit(X, unmerge = "strong")
strong_dist_labels = strong_dist_clustering.labels_
# Write result to a text file
f = open('unpruned_strong_flip_dist.txt', 'w')
for l_ in strong_dist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()

strong_maxdist_clustering = dihnosir.DIHNOSIR(n = 250, silhouette_threshold = 0).fit(Y, unmerge = "strong")
strong_maxdist_labels = strong_maxdist_clustering.labels_
f = open('unpruned_strong_flip_maxdist.txt', 'w')
for l_ in strong_maxdist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()

weak_dist_clustering = dihnosir.DIHNOSIR(n = 250, minPts_min = 4, silhouette_threshold = 0.6).fit(X, unmerge = "weak")
weak_dist_labels = weak_dist_clustering.labels_
f = open('unpruned_weak_flip_dist.txt', 'w')
for l_ in weak_dist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()

weak_maxdist_clustering = dihnosir.DIHNOSIR(n = 250, silhouette_threshold = 0.6).fit(Y, unmerge = "weak")
weak_maxdist_labels = weak_maxdist_clustering.labels_
f = open('unpruned_weak_flip_maxdist.txt', 'w')
for l_ in weak_maxdist_labels:
    f.write(str(l_))
    f.write(' ')
f.close()
