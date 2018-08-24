# Plot Function for Flip Data 
# Author: Amir Shanehsazzadeh <amirshaneshazzadeh@college.harvard.edu>
# Residues run from bottom to top, Clusters run left to right

library('lattice')

plot <- function(clusFile, dataFile) {
  clus <- scan(clusFile)
  data <- read.table(dataFile, header=T)
  xyplot(psi ~ phi | (clus)*str_res, data=data, aspect=1, pch=19, cex=0.15,auto.key=T,strip=F)
}

#plot('plot_weak_flip_dist.txt', 'flip_plot.txt')
#plot('plot_weak_flip_maxdist.txt', 'flip_plot.txt')
#plot('plot_weak_flip_dist.txt', 'flip_plot.txt')
#plot('plot_weak_flip_maxdist.txt', 'flip_plot.txt')