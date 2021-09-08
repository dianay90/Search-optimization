import numpy as np
import math

#Cite: https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
#hi
movements = dict()
movements= {
'1':'X+', 
'2': 'X-',
'3':'Y+', 
'4': 'Y-',
'5':'Z+', 
'6': 'Z-',
'7':'X+Y+', 
'8': 'X+Y-',
'9':'X-Y+', 
'10': 'X-Y-',
'11':'X+Z+', 
'12': 'X+Z-',
'13':'X-Z+', 
'14': 'X-Z-',
'15':'Y+Z+', 
'16': 'Y+Z-',
'17': 'Y-Z+',
'18': 'Y-Z-',

}

'''
def bfs(graph, startingNode, endNode):
    frontier = list() #the queue
    explored = list() # all things visited
    totalCost = 0 
    totalSteps = 0

    # Add first stuff to lists
    frontier.append(graph[0])
    totalSteps = 1

    while frontier>0:
        node = frontier.pop(0)
        explored.append(node)
        
        #for each neighbor
        for item in graph:
            if item not in explored or frontier:
                frontier.append(item)
''' 

inputDict = dict()
file = open('bfs_input.txt', 'r')
Lines = (file.readlines())


inputDict['graphType'] = Lines[0].strip()
inputDict['graphDimensions'] = Lines[1].strip()
inputDict['start'] = Lines[2].strip()
inputDict['end'] = Lines[3].strip()
inputDict['steps'] = Lines[4].strip()


graph = list()

for item in Lines[5:]:

    graph.append(item.strip())


print("end")


'''
print("hello from python on ubuntu on windows!")

#Cite https://www.codegrepper.com/code-examples/python/numpy+find+distance+between+two+points+in+3d
a = np.array([1.0, 3.5, -6.3])
b = np.array([4.5, 1.6,  1.2])

dist = np.linalg.norm(a-b)
dist = math.floor(dist)

print(dist) 
'''