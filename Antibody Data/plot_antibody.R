# Plot Function for Antibody Data 
# Author: Amir Shanehsazzadeh <amirshaneshazzadeh@college.harvard.edu>
# Residues run from bottom to top, Clusters run left to right
# n*(clus) used for published results (Residues run from left to right, Clusters run from bottom to top)

library('lattice')

plot <- function(clusFile, dataFile) {
  clus <- scan(clusFile)
  data <- read.table(dataFile, header=T)
  xyplot(psi ~ phi | (clus)*n, data=data, aspect=1, pch=19, cex=0.15,auto.key=T,strip=F)
}

#plot('plot_weak_antibody_dist.txt', 'antibody_out')
#plot('plot_weak_antibody_maxdist.txt', 'antibody_out.txt')
#plot('plot_weak_antibody_dist.txt', 'antibody_out.txt')
#plot('plot_weak_antibody_maxdist.txt', 'antibody.txt')