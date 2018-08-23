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
    if int(l_) in [7, 10, 11, 12, 13, 14, 15]:
        f.write(str(-1))
        f.write(' ')
    elif int(l_) in [6, 16, 17]:
        f.write(str(4))
        f.write(' ')
    elif int(l_) in [18]:
        f.write(str(1))
        f.write(' ')
    elif int(l_) in [8]:
        f.write(str(6))
        f.write(' ')
    elif int(l_) in [9]:
        f.write(str(7))
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
    if int(l_) in [8, 11, 12, 13, 14, 16, 17, 18, 20, 21]:
        f.write(str(-1))
        f.write(' ')
    elif int(l_) in [19]:
        f.write(str(0))
        f.write(' ')
    elif int(l_) in [7]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [9]:
        f.write(str(8))
        f.write(' ')
    elif int(l_) in [10]:
        f.write(str(7))
        f.write(' ')
    elif int(l_) in [19]:
        f.write(str(0))
        f.write(' ')
    elif int(l_) in [6, 15]:
        f.write(str(4))
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
        f.write(str(5))
        f.write(' ')
    elif int(l_) in [5]:
        f.write(str(4))
        f.write(' ')
    elif int(l_) in [7]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [8]:
        f.write(str(6))
        f.write(' ')
    elif int(l_) in [9]:
        f.write(str(7))
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
    if int(l_) in [9, 11, 12]:
        f.write(str(-1))
        f.write(' ')
    elif int(l_) in [2]:
        f.write(str(3))
        f.write(' ')
    elif int(l_) in [3]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [10, 13]:
        f.write(str(6))
        f.write(' ')
    elif int(l_) in [6]:
        f.write(str(4))
        f.write(' ')
    elif int(l_) in [7]:
        f.write(str(2))
        f.write(' ')
    elif int(l_) in [8]:
        f.write(str(7))
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