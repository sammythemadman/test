#!/usr/bin/python
import math
import numpy

#graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}
#graph = {'A': ['B', 'C', 'D'], 'B' : [], 'C' : [], 'D' : []}
#graph = {'A': ['B', 'D'], 'B' : ['C'], 'C' : [], 'D' : []}
#graph = {'A': [], 'B' : ['A'], 'C' : ['A'], 'D' : ['A']}
#graph = {'A': ['B'], 'B' : ['C'], 'C' : ['D'], 'D' : []}
#graph = {'A': ['B'], 'B' : ['C'], 'C' : ['D', 'E'], 'D' : [], 'E' : []}
#graph = {'A': [], 'B' : [], 'C' : ['D'], 'D' : ['E'], 'E' : ['C']}
#graph = {'A': ['B', 'C']}

alpha = 1
#def class graph_weights(graph, alpha):
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
                    
    return paths 

b = []
for i in graph.keys():
    for j in graph.keys():
        if i != j:
            if find_all_paths(graph,i,j):
                b.append(find_all_paths(graph, i , j))
print b

maxlen = 0


for i in range(len(b)):
    for j in range(len(b[i])):
        if len(b[i][j]) >= maxlen:
            maxlen = len(b[i][j])
            
print maxlen

powers_of_alpha = numpy.zeros(maxlen)

for i in range(maxlen):
    if i == 0:
        powers_of_alpha[i] = 1
    else:
        powers_of_alpha[i] = powers_of_alpha[i-1] + pow(alpha,i)
        
#print powers_of_alpha


nodes_in_paths = {}

for i in range(len(b)):
    for j in range(len(b[i])):
        for k in range(len(b[i][j])):
            if not nodes_in_paths.has_key(b[i][j][k]):
                nodes_in_paths[b[i][j][k]] = 0
            if k != len(b[i][j])-1:
                nodes_in_paths[b[i][j][k]] = nodes_in_paths[b[i][j][k]] + (pow(alpha, (len(b[i][j])-k))/powers_of_alpha[len(b[i][j])-1])

        
print nodes_in_paths