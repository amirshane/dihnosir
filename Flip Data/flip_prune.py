"""
Prune Commands for Flip Data
"""

# Author: Amir Shanehsazzadeh <amirshanehsazzadeh@college.harvard.edu>

# Prune results using Strong DIHNOSIR and dist metric

f = open('unpruned_strong_flip_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_strong_flip_dist.txt', 'w')
for l_ in x:
    if int(l_) in [7, 11, 12, 13, 14, 15, 16, 17, 23]:
        f.write(str(-1))
        f.write(' ')
    elif int(l_) in [6]:
        f.write(str(4))
        f.write(' ')
    elif int(l_) in [8]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [10]:
        f.write(str(7))
        f.write(' ')
    elif int(l_) in [9]:
        f.write(str(6))
        f.write(' ')
    elif int(l_) in [18]:
        f.write(str(1))
        f.write(' ')
    else:
        f.write(l_)
        f.write(' ')
f.close()

f = open('pruned_strong_flip_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_strong_flip_dist.txt', 'w')
for l_ in x:
    for i in range(4):
        f.write(l_)
        f.write(' ')
f.close()

# Prune results using Strong DIHNOSIR and maxdist metric
f = open('unpruned_strong_flip_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_strong_flip_maxdist.txt', 'w')
for l_ in x:
    if int(l_) in [6, 11, 12, 14, 15, 17, 18, 19, 20, 23]:
        f.write(str(-1))
        f.write(' ')
    elif int(l_) in [8]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [7, 13, 21]:
        f.write(str(4))
        f.write(' ')
    elif int(l_) in [10]:
        f.write(str(1))
        f.write(' ')
    elif int(l_) in [16]:
        f.write(str(6))
        f.write(' ')
    elif int(l_) in [9]:
        f.write(str(7))
        f.write(' ')
    else:
        f.write(l_)
        f.write(' ')
f.close()

f = open('pruned_strong_flip_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_strong_flip_maxdist.txt', 'w')
for l_ in x:
    for i in range(4):
        f.write(l_)
        f.write(' ')
f.close()

# Prune results using Weak DIHNOSIR and dist metric
f = open('unpruned_weak_flip_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_weak_flip_dist.txt', 'w')
for l_ in x:
    if int(l_) in [6]:
        f.write(str(4))
        f.write(' ')
    elif int(l_) in [8]:
        f.write(str(6))
        f.write(' ')
    elif int(l_) in [3, 7, 14]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [2]:
        f.write(str(3))
        f.write(' ')
    elif int(l_) in [9, 10, 17]:
        f.write(str(-1))
        f.write(' ')
    else:
        f.write(l_)
        f.write(' ')
f.close()

f = open('pruned_weak_flip_dist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_weak_flip_dist.txt', 'w')
for l_ in x:
    for i in range(4):
        f.write(l_)
        f.write(' ')
f.close()

# Prune results using Weak DIHNOSIR and maxdist metric
f = open('unpruned_weak_flip_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('pruned_weak_flip_maxdist.txt', 'w')
for l_ in x:
    if int(l_) in [8]:
        f.write(str(-1))
        f.write(' ')
    elif int(l_) in [2]:
        f.write(str(3))
        f.write(' ')
    elif int(l_) in [3]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [7]:
        f.write(str(4))
        f.write(' ')
    else:
        f.write(l_)
        f.write(' ')
f.close()

f = open('pruned_weak_flip_maxdist.txt', 'r')
x = f.readlines()[0].split()
f.close()

f = open('plot_weak_flip_maxdist.txt', 'w')
for l_ in x:
    for i in range(4):
        f.write(l_)
        f.write(' ')
f.close()