# CML-MultiOmics-Resistance-Analysis
An integrated computational pipeline to identify BCR-ABL independent resistance mechanisms in Chronic Myeloid Leukemia using Multi-omics data (Transcriptomics + Genomics).

## Features
* **Transcriptomic Profiling:** Differential Expression Analysis (DESeq2/EdgeR) to identify non-canonical pathways.
* **Genomic Variant Calling:** NGS pipeline for somatic mutation detection in resistance-associated genes.
* **Integrative Analysis:** Correlation of expression levels with mutational burden using AI/ML (Random Forest/SVM).
* **Clinical Visualization:** Interactive dashboard for prognostic marker identification.

## Tech Stack
* **Languages:** Python (Pandas, Scikit-learn), R (Bioconductor)
* **Tools:** FastQC, BWA-MEM, GATK4, VEP (Variant Effect Predictor)
