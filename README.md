# DNA Alignment Visualizer

This repository contains a Python script that visualizes the alignment of two DNA sequences from a FASTA file by marking identical bases with a pipe symbol (`|`) and differences with a space (` `). This allows easier inspection of matching regions in sequence alignments.

## 🔧 Usage

```bash
python align_viewer.py <FASTA file>
```

##  Example Case

Input:
```bash
>seq1
ATGCAAGTCGAGCGGATGAAGGGAGCTTGCTCCTGGATTCAGCGGCGGAC
>seq2
ATGCAAGTCGAGCGGCAGCACAGAGGAACCTTGGGTGGCGAGCGGCGGAC
```

Output:
```bash
ATGCAAGTCGAGCGGATGAAGGG
|||||||||||||||  | |  |
ATGCAAGTCGAGCGGCAGCACAG
```
