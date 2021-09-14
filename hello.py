import numpy as np
import math
from queue import PriorityQueue
import heapq

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

def findNeighborsUCS(node, movements, graph):

    neighbors = list()
    location = node[1]
 
    actions = graph[location].split()

    for x in actions:

        canVisit = calcDistances(movements[x],location)
        if int(x) <= 6: 
            cost = 10
        else:
             cost = 14
        new_tuple = (cost,canVisit)
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

def updateCostPt2(neighbors, frontierTracker, node):
    for x in neighbors:
        prevCost = int(frontierTracker[node])
        newCost = int(x[0]) + prevCost 
        entry = {x[1]:newCost}
        frontierTracker.update(entry)



def updateUcsDictionary(frontierTracker, neighbors, cost):
    for x in neighbors:
        if x[1] in frontierTracker.keys():
            if int(x[0]) + cost < int(frontierTracker[x[1]]):
                entry = {x[1]: x[0]}
                frontierTracker.update(entry)
        else:
            #brand new
            tempCost = cost + int(x[0])
            #frontierTracker[x[1]] = int(x[0]
            frontierTracker[x[1]] = tempCost
    
def updateFrontierCost(node, frontierTracker, cost):
    potentialCost = int(node[0])+ cost
    if potentialCost < int(frontierTracker[node[1]]):
        newCost = {node[1]: potentialCost}
        frontierTracker.update(newCost)

def updateCost (node, frontierTracker, cost, shallowCost):

    newCost = int(shallowCost) + cost #Add existing cost to new cost
    entry = {node:newCost}
    frontierTracker.update(entry)
        
def UCS(graph, startingNode, endNode, movements, graphDimensions):
    frontierTracker = dict()
    frontier_ucs = PriorityQueue()

    frontier_ucs.put(startingNode)
    frontierTracker[startingNode] =0
    explored = list()
    shortestRoute =list()
    cost = 0 
    tempDict = dict()

    while frontier_ucs.qsize()>0:
        node = frontier_ucs.get()

        if node == endNode: 
            return "SOLUTION FOUND"

        explored.append(node)
        #cost = updateCost(node, frontierTracker, cost, tempDict)
        tempDict.clear()

        shortestRoute.append(node)

        neighbors = findNeighborsUCS(node, movements, graph)
        #newCost = updateUcsDictionary(frontierTracker,neighbors, cost)

        updateCostPt2(neighbors, frontierTracker, node)

        for x in neighbors:
            potentialCost = int(x[0])+ cost

            if x[1] not in frontier_ucs.queue and x[1] not in explored:
                if x[1] == endNode:
                    shortestRoute.append(x[1])
                    return "IN HERE SOLUTION"
                frontier_ucs.put(x[1])
                tempDict[x[1]] = x[0]
                #updateCost(node, frontierTracker, cost, x[0])
                
                
            elif  x[1] in frontier_ucs.queue:
                if potentialCost < int(frontierTracker[x[1]]):
                    newCost = {x[1]: potentialCost}
                    frontierTracker.update(newCost)
            
def checkInFrontier(node, frontierQueue):
    value= any((node) in item for item in frontierQueue)
    return value
def checkTupleInExplored(node, explored):
    value =  [ y for x, y in explored if y  ==  node ]
    return value

def UCSv2(graph, startingNode, endNode, movements, graphDimensions):
    frontierTracker = dict()
    frontier_ucs = PriorityQueue()

    frontier_ucs.put((0, startingNode))

    frontierTracker[startingNode] = 0

    explored = list()

    while frontier_ucs.qsize()>0:
        node = frontier_ucs.get()

        if node[1] == endNode: 
            return "SOLUTION FOUND"

        explored.append(node)

        neighbors = findNeighborsUCS(node, movements, graph)
    
        for x in neighbors:
            xyz_coordinate = x[1]
            neighborCost = int(x[0])+ int(frontierTracker[node[1]])
            tuple = (neighborCost, x[1])
            #if checkInFrontier(x[1], frontier_ucs.queue) == False and checkTupleInExplored(x[1],explored) ==False :
            if any((x[1]) in item for item in frontier_ucs.queue) == False:
                if [ y for z, y in explored if y  == xyz_coordinate] == False:

            #[ (x,y) for x, y in explored if x  == 0 ]
            #[ y for x, y in explored if y  == '7 0 1' ]
                    frontier_ucs.put(tuple)
                #updateCost(node, frontierTracker, cost, x[0])
                
            elif  checkInFrontier(x[1], frontier_ucs.queue):
                if neighborCost < int(frontierTracker[x[1]]):
                    newCost = {x[1]: neighborCost}
                    frontierTracker.update(newCost)
def findIndexofHeapQ(heapq,value):
    for x in range(0,len(heapq)):
        if heapq[x][1] == value:
            return x
    return 0 

def UCSv4(graph, startingNode, endNode, movements, graphDimensions):
    frontierTracker = dict()

    frontier_ucs_heapq = []
    heapq.heappush(frontier_ucs_heapq, (0, startingNode))

    frontierTracker[startingNode] = 0

    explored = list()

    while len(frontier_ucs_heapq)>0:
        node = heapq.heappop(frontier_ucs_heapq)

        if node[1] == endNode: 
            return "SOLUTION FOUND"

        explored.append(node[1])

        neighbors = findNeighborsUCS(node, movements, graph)
    
        for x in neighbors:
            # previous parent node cost + neighbor cost
            neighborCost = int(x[0])+ int(frontierTracker[node[1]])

            if not any (x[1] == b for a, b in frontier_ucs_heapq) and x[1] not in explored:
          
                heapq.heappush(frontier_ucs_heapq, (neighborCost, x[1]))
                frontierTracker[x[1]] = neighborCost
                
            elif  any (x[1] == b for a, b in frontier_ucs_heapq):
                if True:
                #if neighborCost < int(frontierTracker[x[1]]):
                    newCost = {x[1]: neighborCost}
                    frontierTracker.update(newCost)
                    index = findIndexofHeapQ(frontier_ucs_heapq,x[1])
                    if index == 0: 
                        break
                    else:
                        frontier_ucs_heapq[index] = frontier_ucs_heapq[-1]
                        frontier_ucs_heapq.pop()
                        heapq.heappush(frontier_ucs_heapq, (neighborCost, x[1]))
                        heapq.heapify(frontier_ucs_heapq)
                    
          
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

    bfsData = initiateGraph("/home/dianaoh/aihw1/bfs_input.txt")
    bfsPath = bfs(bfsData[0],bfsData[1]["start"],bfsData[1]["end"], movements, bfsData[1]["graphDimensions"])
    outputFileContent = constructFile (bfsPath)

    ucsData = initiateGraph("/home/dianaoh/aihw1/usc_input.txt")
    bfsPath = UCSv4(ucsData[0],ucsData[1]["start"],ucsData[1]["end"], movements, ucsData[1]["graphDimensions"])

    blue = initiateGraph("/home/dianaoh/aihw1/ucs_input.txt")

