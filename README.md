# TopGO
## This is a small tutorial. This script gets you a significantly expressed list of go terms and genes.

In order to run this script you must first obtain a GAF file from the link below for you desired dataset. 

https://www.ebi.ac.uk/GOA/proteomes

**36261.T_guttata.goa.txt.gz** and **Zebra_Finch.txt** is an example GAF file. It must be unzipped before use (gunzip 36261.T_guttata.goa.txt.gz).

You will then run the command below to generate a mapping file
**python3 GAF_To_GO_Map.py file_name**
 
###Example

**python3 GAF_To_GO_Map.py 36261.T_guttata.goa.txt**

You will then follow either **TopGO_Script.R** or **TopGO_Scrpt.pdf** which has the steps and comments to walk you through it.
