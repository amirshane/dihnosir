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

User Installation and Demonstration
-----------------------------------
- To install DIHNOSIR simply download the 'dihnosir.py' and 'dihnosir_helper.py' files and store them in the same directory.
- To see how DIHNOSIR is used download the files in either the 'Flip Data' or 'Antibody Data' folder. The scripts show how to format the files given the data set and the distance values, how a cluster constraint is defined (for this protein dihedral data), and what commands need to be used to compute DIHNOSIR and store the results.
  - The original, unprocessed data is contained in the files 'flip_out.txt' and 'antibody_out.txt'. The flip data folder also has the file 'flip_plot.txt', which is used for plotting. The calculated distance values are in the files 'flip_dist.txt', 'flip_maxdist.txt', 'antibody_dist.txt', and 'antibody_maxdist.txt'.
  - First, run 'file_formatting.py'. This will create and store distance matrices in the following pickle files: 'flip_dist.pickle', 'flip_maxdist.pickle', 'antibody_dist.pickle', and 'antibody_maxdist.pickle'. It will also create the angular separation matrices and store them in 'flip_separation.pickle' and 'antibody_separation.pickle'.
  - The files 'dihnosir.py' and 'dihnosir_helper.py' do not need to be opened unless you would like to modify the cluster constraint, which can be found in 'dihnosir_helper.py'. 
  - Next, run 'flip_commands.py' or 'antibody_commands.py'. This will calculate DIHNOSIR on the data sets using both distance metrics and both Strong and Weak DIHNOSIR. The unpruned results will be stored to the txt files starting with 'unpruned...'.
  - Running 'flip_prune.py' and 'antibody_prune.py' will prune the results and store them in the txt files starting with 'pruned...'. This will also create the txt files starting with 'plot...', which are used for plotting the results. 
  - To plot the results load the plot() function from either 'plot_flip.r' or 'plot_antibody.r'. Then run the plot() function with a corresponding plot file and either the file 'flip_plot.txt' or 'antibody_out.txt'. The commands using the formatted files included in either the 'Flip Data' or 'Antibody Data' folder are included in the R scripts, but are commented out.
  
Development
-----------
We encourage users to experiment with and modify DIHNOSIR and would appreciate if said users shared their modifications and discoveries with us.

Communication
-------------
- Developer Emails: amir.p.shanehsazzadeh@gmail.com, roland.dunbrack@fccc.edu
- Developer Website: https://amirpouya.us
- Dunbrack Lab Website: http://dunbrack.fccc.edu

Citation
--------
If you use DIHNOSIR in a scientific publication, we would appreciate citations: (paper in publishing process)
