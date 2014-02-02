#!/usr/bin/python
import math
import numpy

from all_paths import graph_weights

#graph = {'A': ['B', 'C'], 'B': ['C', 'D'], 'C': ['D'], 'D': ['C'], 'E': ['F'], 'F': ['C']}
graph = {'A': ['B', 'C', 'D'], 'B' : [], 'C' : [], 'D' : []}
#graph = {'A': [], 'B' : ['A'], 'C' : ['A'], 'D' : ['A']}
#graph = {'A': ['B'], 'B' : ['C'], 'C' : ['D'], 'D' : []}
#graph = {'A': ['B'], 'B' : ['C'], 'C' : ['D', 'E'], 'D' : [], 'E' : []}
#graph = {'A': [], 'B' : [], 'C' : ['D'], 'D' : ['E'], 'E' : ['C']}
#graph = {'A': ['B', 'C']}

alpha = 1