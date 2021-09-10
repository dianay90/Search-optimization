import numpy as np
import math

def checkBounds (node, graphDimensions):
    value = node
    value_list = value.split()
    graphDimensions_list = graphDimensions.split()

    x_coordinate = int(value_list[0])
    y_coordinate = int(value_list[1])
    z_coordinate = int(value_list[2])
    
    x_max= int(graphDimensions_list[0])
    y_max= int(graphDimensions_list[1])
    z_max= int(graphDimensions_list[2])

    if x_coordinate >= x_max or x_coordinate < 0:
        return "fail"
    elif y_coordinate >= y_max or y_coordinate <0:
        return "fail"
    elif z_coordinate >= z_max or z_coordinate < 0: 
        return "fail"
def findNeighbors(node, movements, graph):

    neighbors = list()
    location = node
    actions = graph[location].split()

    for x in actions:

        canVisit = calcDistances(movements[x],location)
        new_tuple = (canVisit)
        neighbors.append(new_tuple) 

    return neighbors
    #return neighbors
def calcDistances (direction,startingPoint):
    x_coordinate = int(startingPoint.split()[0])
    y_coordinate = int(startingPoint.split()[1])
    z_coordinate = int(startingPoint.split()[2])

    #1
    if direction == "X+":
        x_coordinate = x_coordinate + 1
    #2
    elif direction == "X-":
        x_coordinate = x_coordinate - 1
    #3

    elif direction == "Y+":
        y_coordinate = y_coordinate + 1
    
    #4
    elif direction == "Y-":
        y_coordinate = y_coordinate - 1
    
    #5
    elif direction == "Z+":
        z_coordinate = z_coordinate + 1
    
    #6
    elif direction == "Z-":
        z_coordinate = z_coordinate - 1

    #7
    elif direction == "X+Y+":
        x_coordinate = x_coordinate + 1
        y_coordinate = y_coordinate + 1

    #8
    elif direction == "X+Y-":
        x_coordinate = x_coordinate + 1
        y_coordinate = y_coordinate - 1
    #9
    elif direction == "X-Y+":
        x_coordinate = x_coordinate - 1
        y_coordinate = y_coordinate + 1

    #10
    elif direction == "X-Y-":
        x_coordinate = x_coordinate - 1
        y_coordinate = y_coordinate - 1
    
    #11
    elif direction == "X+Z+":
        x_coordinate = x_coordinate + 1
        z_coordinate = z_coordinate + 1

    #12
    elif direction == "X+Z-":
        x_coordinate = x_coordinate + 1
        z_coordinate = z_coordinate - 1
    #13
    elif direction == "X-Z+":
        x_coordinate = x_coordinate - 1
        z_coordinate = z_coordinate + 1
    #14
    elif direction == "X-Z-":
        x_coordinate = x_coordinate - 1
        z_coordinate = z_coordinate - 1
    #15
    elif direction == "Y+Z+":
        y_coordinate = y_coordinate + 1
        z_coordinate = z_coordinate + 1
    #16
    elif direction == "Y+Z-":
        y_coordinate = y_coordinate + 1
        z_coordinate = z_coordinate - 1
    #17
    elif direction == "Y-Z+":
        y_coordinate = y_coordinate - 1
        z_coordinate = z_coordinate + 1
    #18
    elif direction == "Y-Z-":
        y_coordinate = y_coordinate - 1
        z_coordinate = z_coordinate - 1
        
    x_coordinate = str(x_coordinate)
    y_coordinate = str(y_coordinate)
    z_coordinate = str(z_coordinate)
    finalCoordinate = x_coordinate + " " + y_coordinate + " " + z_coordinate


    return finalCoordinate






def returnPathOptions(node):
    startingPoint = node[0]
    newDistanceList =list()
    i = 1
    while i < len(node):
        newDistanceList.append(i)

def calculateShortestPath(startingNode,endNode,previousNodeDict):
    shortestPath = list()
    shortestPath.append(endNode + " 1")
    backwardsNode = endNode
    while backwardsNode != startingNode:
        for i in previousNodeDict:
            if backwardsNode in previousNodeDict[i]:
                if i != startingNode:
                    shortestPath.append(i + " 1")
                else:
                    shortestPath.append(i + " 0")
                backwardsNode = i

    shortestPath.reverse()
    cost = len(shortestPath)-1 
    length = len(shortestPath)

    return shortestPath, cost, length

def constructFile(bfsData):

    with open('bfs_output.txt', mode='wt', encoding='utf-8') as output_file:
        if bfsData != 'FAILED':
            output_file.write(str(bfsData[1]) + "\n")
            output_file.write(str(bfsData[2]) + "\n")
            output_file.write('\n'.join(bfsData[0]))
        else: 
            output_file.write("FAIL")



def neighborCheck(neighbors, explored, previousNodeDict):
    for j in neighbors:
        for i in explored:
            if j == i: 
                previousNodeDict.update({i:j})
    

def bfs(graph, startingNode, endNode, movements, graphDimensions):
    frontier = list() #the queue
    previousNodeDict = dict()

        
    # Add first stuff to lists
    frontier.append(startingNode)
    explored = list() # all things visited
    
    while len(frontier)>0:
        node = frontier.pop(0)
        value = checkBounds(node, graphDimensions)
        if value == "fail":
            continue

        explored.append(node)  
        previousNodeDict[node] = list()
         
        # find neighbors
        neighbors = findNeighbors(node, movements, graph)

        # this is return just a neighbor....
        # Add neighbors to frontier
        for x in neighbors: 
            #check previous nodes 
            if x not in frontier and x not in explored:
                previousNodeDict[node].append(x)
                 
                if x == endNode: #clean up output files
                    shortestRoute =calculateShortestPath(startingNode, endNode, previousNodeDict)
                    return shortestRoute
                frontier.append(x)
    print("woof")
    return "FAILED"


def initiateGraph(filename):
    inputDict = dict()
    file = open(filename, 'r')
    Lines = (file.readlines())


    inputDict['graphType'] = Lines[0].strip()
    inputDict['graphDimensions'] = Lines[1].strip()
    inputDict['start'] = Lines[2].strip()
    inputDict['end'] = Lines[3].strip()
    inputDict['steps'] = Lines[4].strip()


    graph = list()

    for item in Lines[5:]:

        graph.append(item.strip())


    graphDictionary = dict()
    for item in graph:
        nodeLocation= ' '.join(item.split()[:3])
        nodeMoves= ' '.join(item.split()[3:])
        graphDictionary[nodeLocation] = nodeMoves
    
    return graphDictionary,inputDict




#bfs(graphDictionary, inputDict['start'],inputDict['end'])


'''
print("hello from python on ubuntu on windows!")

#Cite https://www.codegrepper.com/code-examples/python/numpy+find+distance+between+two+points+in+3d
a = np.array([1.0, 3.5, -6.3])
b = np.array([4.5, 1.6,  1.2])

dist = np.linalg.norm(a-b)
dist = math.floor(dist)

print(dist) 
'''

if __name__ == "__main__":

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

    bfsData = initiateGraph("bfs_input.txt")
    bfsPath = bfs(bfsData[0],bfsData[1]["start"],bfsData[1]["end"], movements, bfsData[1]["graphDimensions"])
    outputFileContent = constructFile (bfsPath)

    blue = initiateGraph("usc_input.txt")

