DIHNOSIR: Density-Independent High Noise Optimized Sorting by Iterative Refinement
==================================================================================

DIHNOSIR is a clustering algorithm contained in a Python module built using scikit-learn and NetworkX and distributed under the GNU GPLv3.0 license. The project was started in 2017 by Amir Shanehsazzadeh and Dr. Roland L. Dunbrack Jr. at the Dunbrack Lab at Fox Chase Cancer Center. 

DIHNOSIR was originally intended to cluster protein structural conformations in the form of Ramachandran plots, however it has been generalized to work with any data set that has a corresponding distance metric. DIHNOSIR works by running numerous iterations of the famous DBSCAN algorithm (scikit-learn implementation), removing merged clusters, and combining the unmerged clusters using a graph-theoretic approach (NetworkX implementations).The module consists of two algorithms, Strong DIHNOSIR and Weak DIHNOSIR, which differ in regards to how they remove merged clusters. Strong DIHNOSIR requires the user to define a Boolean constraint function that returns True whenever a cluster is unmerged and False whenever a cluster is merged. Weak DIHNOSIR does not require the user to define this, function, instead it uses a graph-theoretic approach (NetworkX implementations) to remove merged clusters. For more on DIHNOSIR read our paper: (currently in publishing process).

Installation
------------

Dependencies
~~~~~~~~~~~~
DIHNOSIR requires:

- Python (>= 3.4)
- Scikit-learn (>= 0.19.2)
- NetworkX (>= 2.1)
- NumPy (>= 1.8.2)
~~~~~~~~~~~~~~~~~~~~~~~~~
User installation and use
~~~~~~~~~~~~~~~~~~~~~~~~~
To install DIHNOSIR simply download the 'dihnosir.py' and 'dihnosir_helper.py' files and store them in the same directory. DIHNOSIR's documentation is contained in these two files.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Demo
----
To see how DIHNOSIR is used download the files in either the "Antibody Data" or "Flip Data" folder. The Python scripts show how to format the files given the data set and the distance values, how a cluster constraint is defined (for this protein dihedral data), and what commands need to be used to compute DIHNOSIR and store the results. (Note that the results in this folder have not been pruned and thus may differ moderately from and published results.

Development
-----------
We encourage users to experiment with and modify DIHNOSIR and would appreciate if said users shared their modifications and discoveries with us.

Communication
-------------
- Developer Emails: amirshanehsazzadeh@college.harvard.edu, roland.dunbrack@fccc.edu
- Developer Website: http://amirshanehsazzadeh.com
- Dunbrack Lab Website: http://dunbrack.fccc.edu

Citation
--------
If you use DIHNOSIR in a scientific publication, we would appreciate citations: (paper in publishing process)
