import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import pdb

##reading data into dataframe
tetra=pd.read_table("tetrahymena.tsv",sep="\t")
##removing the smallest and largest cell
tetra_filter=tetra[(tetra.diameter>19.2) & (tetra.diameter<26.0)]

##getting mean conc and diameter over technical replicates.
tetra_ag1=tetra_filter.groupby(['culture','glucose'],as_index=False).mean()

##plot1:
plot1=sns.lmplot( x= "conc",y= "diameter", data= tetra_ag1, fit_reg=False, hue='glucose', legend=True,markers=["o", "x"])

plot1.savefig("final_part_A_nonlog_rsr351.pdf")

##this the pdb-python debugger - typing c will complete generating plot in next step.
##pdb.set_trace()

##calculating the log values of conc and diameter
log_conc=np.log(tetra_ag1["conc"])
log_diameter=np.log(tetra_ag1["diameter"])

##adding new column to the dataframe
tetra_ag1['log_conc']=log_conc
tetra_ag1['log_diameter']=log_diameter
tetra_ag1


##plot2 for logconc and logdiameter
##after log transformation it is linear, hence the variables are related by power law
plot2=sns.lmplot( x= "log_conc",y= "log_diameter", data= tetra_ag1, fit_reg=False, hue='glucose', legend=True,markers=["o", "x"])
plot2.savefig("final_part_A_log_rsr351.pdf")