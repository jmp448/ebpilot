# SplitGPM Analysis for Embryoid Body Pilot Project
- Pseudotime inference and lineage subsetting is performed in `analysis/lineages.ipynb`  
- Pseudobulk aggregation - cells from the same (individual, bin), (batch, bin) or (batch & individual, bin) have their counts summed together to generate pseudobulk samples. Bins are pseudotime quantile bins, and the default number of bins is 5. This is done in `analysis/pseudobulk.ipynb`  
- SplitGPM analysis is used to cluster individuals, batches, or batch/individuals by the similarity of their progression through differentiation, as measured by pseudotime. It also cluster genes into modules which behave similarly during differentiation. For more information about splitGPM, see Strober, Elorbany, and Rhodes et al. 2019 *Dynamic genetic regulation of gene expression during cellular differentiation*. The analysis is done in `analysis/splitGPM.ipynb`

Rhodes, K., Barr, K. A., Popp, J. M., Strober, B. J., Battle, A., & Gilad, Y. (2021). Human embryoid bodies as a novel system for genomic studies of functionally diverse cell types. *bioRxiv*. doi: https://doi.org/10.1101/2021.06.16.448714
