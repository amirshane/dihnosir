"""
Prune Commands for Antibody Data
"""

# Author: Amir Shanehsazzadeh <amirshanehsazzadeh@college.harvard.edu>

# Prune results using Strong DIHNOSIR and dist metric
f = open('unpruned_strong_antibody_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_strong_antibody_dist.txt', 'w')
for l_ in x:
    if int(l_) in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
        f.write(str(-1))
        f.write(' ')
    elif int(l_) in [5]:
        f.write(str(6))
        f.write(' ')
    elif int(l_) in [6]:
        f.write(str(5))
        f.write(' ')
    else:
        f.write(l_)
        f.write(' ')
f.close()

f = open('pruned_strong_antibody_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_strong_antibody_dist.txt', 'w')
for l_ in x:
    for i in range(11):
        f.write(l_)
        f.write(' ')
f.close()

# Prune results using Strong DIHNOSIR and maxdist metric
f = open('unpruned_strong_antibody_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_strong_antibody_maxdist.txt', 'w')
for l_ in x:
    if int(l_) in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
        f.write(str(-1))
        f.write(' ')
    else:
        f.write(l_)
        f.write(' ')
f.close()

f = open('pruned_strong_antibody_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_strong_antibody_maxdist.txt', 'w')
for l_ in x:
    for i in range(11):
        f.write(l_)
        f.write(' ')
f.close()

# Prune results using Weak DIHNOSIR and dist metric
f = open('unpruned_weak_antibody_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_weak_antibody_dist.txt', 'w')
for l_ in x:
    if int(l_) in [5, 10, 11, 12, 17]:
        f.write(str(4))
        f.write(' ')
    else:
        f.write(l_)
        f.write(' ')
f.close()

f = open('pruned_weak_antibody_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_weak_antibody_dist.txt', 'w')
for l_ in x:
    for i in range(11):
        f.write(l_)
        f.write(' ')
f.close()

# Prune results using Weak DIHNOSIR and maxdist metric
f = open('unpruned_weak_antibody_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_weak_antibody_maxdist.txt', 'w')
for l_ in x:
    f.write(l_)
    f.write(' ')
f.close()

f = open('pruned_weak_antibody_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_weak_antibody_maxdist.txt', 'w')
for l_ in x:
    for i in range(11):
        f.write(l_)
        f.write(' ')
f.close()