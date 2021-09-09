import numpy as np
import math


def findNeighbors(node, movements):

    neighbors = list()
    print("inhere")
    location = node[0]
    i=1
    for x in node[1:]:
        #calcANeigbor(node,)
        canVisit = calcDistances(movements[x],location)
        print("x")

    
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
    finalCoordinate = {x_coordinate + " " + y_coordinate + " " + z_coordinate}

    print("end")

    return finalCoordinate






def returnPathOptions(node):
    startingPoint = node[0]
    newDistanceList =list()
    i = 1
    while i < len(node):
        newDistanceList.append(i)




    

def bfs(graph, startingNode, endNode, movements):
    frontier = list() #the queue
    explored = list() # all things visited
    totalCost = 0 
    totalSteps = 0
    cleanListWithCost = list()

    # Add first stuff to lists
    frontier.append(next(iter((graph.items())) ))

    cleanListWithCost.append(startingNode + " 0")

    while len(frontier)>0:
        node = frontier.pop(0)
        explored.append(node[0])   
        cleanListWithCost.append(node[0] + " 1")
        
        # find neighbors
        neighbors = findNeighbors(node, movements)
        '''
        for 
        if item not in explored or frontier:
            if 
            frontier.append(item)
            '''

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


    print("end")

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
    bfs(bfsData[0],bfsData[1]["start"],bfsData[1]["end"], movements)


    blue = initiateGraph("usc_input.txt")

    print("end")