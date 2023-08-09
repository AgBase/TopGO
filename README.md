# TopGO
##This is a small tutorial. This script gets you a significantly differentially expressed list of go terms and genes

**36261.T_guttata.goa.txt.gz** and **Zebra_Finch.txt** is an example GAF file. It must be unzipped before use (gunzip 36261.T_guttata.goa.txt.gz).

In order to run this script you must first obtain a GAF file from the link below for you desired dataset.

https://www.ebi.ac.uk/GOA/proteomes

You will then run the command below to generate a mapping file
**python3 GAF_To_GO_Map.py file_name**

###Example

**python3 GAF_To_GO_Map.py 36261.T_guttata.goa.txt**

This will produce a file called Gene2Term.txt which will be the input file for the R script below.

You will also need a file resembling Zebra_Finch.txt containing your expermiental differential expression data.

You will then follow either **TopGO_Script.R** or **TopGO_Scrpt.pdf** which has the steps and comments to walk you through it.

The final product of this script will be an array called go2Gene that contains the GO:ID, number of annotated genes and a list of the gene symbols
and a graph of the three most significant nodes and their parents.

