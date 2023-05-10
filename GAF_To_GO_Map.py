import re
import pandas as pd
import os
import sys

'''
https://www.ebi.ac.uk/GOA/proteomes

Files come from the above link

How to run?
In command line you will type
python3 GAF_To_GO_Map.py file_name

Example:

python3 GAF_To_GO_Map.py 36261.T_guttata.goa.txt
'''

file = sys.argv[1]
file1 = open(file, 'r')
file2 = open('tmp.txt', 'w')

for line in file1.readlines():
    x = re.findall("^!", line)
    if not x:
        file2.write(line)
file2.close

df= pd.read_csv('tmp.txt', sep = '\t', header = None)

gene = df[2] #change for different naming this is gene ID
go = df[4]

df2 = pd.concat([gene, go], axis = 1)

df2.columns = ['Gene_ID', 'GO_Term']

os.remove('tmp.txt')


df2.to_csv('Gene2Term.txt', sep='\t', index = None)
