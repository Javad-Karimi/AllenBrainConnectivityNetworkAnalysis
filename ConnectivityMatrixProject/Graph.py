__author__ = 'mmlab'

import networkx as nx
import csv
import json
import matplotlib.pyplot as plt
#######################################################################################################################
SuppTable3 = []
regions = []
ConnMat = {}
SuppTable1 = []


f =  open('supplementary table 3.csv', 'r')
reader = csv.reader(f)

# copies "supplementary table 3.csv" file to SuppTable3 as a list
for row in reader:
    SuppTable3.append(row)

# omites the empty cell (first cell) of supplementary table 3.csv file
for i in SuppTable3[0]:
    if not(i == '') :
        regions.append(i)

# creates the connectivity matrix as the dictionary ConnMat
for i in range(1,len(regions)):
    ConnMat[SuppTable3[i][0]] = dict(zip(regions, SuppTable3[i][1:]))

#ConnMatJson = json.dumps( ConnMat, indent = 4 )

########################################################################################################################
############################################## Graph Formation #########################################################
########################################################################################################################
G = nx.Graph()
G.add_nodes_from(regions)

for i in ConnMat:
    for j in ConnMat[i]:
        # Omits edges with zero weights
        if float(ConnMat[i][j]) != 0:
            G.add_edge(i,j,weight = float(ConnMat[i][j]))

#nx.write_gml(G,'AllenGraph.gml')
#print ConnMat['ACAd']['AAA']
#print G.edge['ACAd']['AAA']
#nx.draw(G)
#plt.show()
########################################################################################################################
############################################ Network Analysis ##########################################################
########################################################################################################################
pagerank = nx.pagerank(G,alpha=0.9)
pr_numpy = nx.pagerank_numpy(G,alpha=0.9)
pr_scipy = nx.pagerank_scipy(G,alpha=0.9)
sc = nx.communicability_centrality(G)


########################################################################################################################
###################################### Establishing results in a csv file ##############################################
########################################################################################################################
ofile  = open('results_csv.csv', "wb")
results_csv = csv.writer(ofile, dialect='excel')
# Headings of the results_csv file
results_csv.writerow([
  'ID',
  'Ontology order',
  'Acronym',
  'Name',
  'Major Region',
  'Voxel Count',
  'Structure Hit with rAAV?',
  'Primary Inj Site',
  'Secondary Inj Site',
  'Represented in Linear Model Matrix',
  '',
  '',
  '',
  '',
  "Page rank"])
g =  open('C:\Users\mmlab\Desktop\supplementary table 1.csv', 'r')
reader1 = csv.reader(g)

# copies "supplementary table 1.csv" file to SuppTable1 as a list
for row in reader1:
    SuppTable1.append(row)

# creates rows of "results_csv.csv" file by selecting the rows of "supplementary table 1.csv" file which contain the information about every graph nodes
for index in range(1, len(SuppTable1)):
    for item in regions:
        if SuppTable1[index][2] == item:
            SuppTable1[index].append(pagerank[item])
            results_csv.writerow(SuppTable1[index])

ofile.close()