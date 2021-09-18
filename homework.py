import numpy as np
import math
from queue import PriorityQueue
import heapq
import os
from collections import deque
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
    actions = graph[node]
    actions= actions.split()

    for x in actions:

        canVisit = calcDistances(movements[x],node)
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

#USE A STACK
def calculateShortestPathv2(startingNode,endNode,previousNodeDict):
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
def calculateShortestPath(startingNode,endNode,previousNodeDict):
    #shortestPath = list()
    shortestPath = deque()
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

    #shortestPath.reverse()
    cost = len(shortestPath)-1 
    length = len(shortestPath)

    return shortestPath, cost, length
def calculateShortestPathUCS(startingNode,endNode,previousNodeDict, localCost):
    shortestPath = list()
    costOfNode = str(localCost[endNode])
    shortestPath.append(endNode + " " + costOfNode)
    starNode = endNode

    while starNode != startingNode:
        costOfNode = str(localCost[previousNodeDict[starNode]])
        shortestPath.append(previousNodeDict[starNode] + " " +  costOfNode)
        starNode = previousNodeDict[starNode]

    shortestPath.reverse()
    length = len(shortestPath)
    length = str(length)
    return length, shortestPath

def constructFile(bfsData):

    with open('output.txt', mode='wt', encoding='utf-8') as output_file:
        if bfsData != 'FAILED':
            output_file.write(str(bfsData[1]) + "\n")
            output_file.write(str(bfsData[2]) + "\n")
            while len(bfsData[0])>0:
                if len(bfsData[0])>1:
                    output_file.write(bfsData[0].pop() +"\n")
                else: 
                    output_file.write(bfsData[0].pop())
        else: 
            output_file.write("FAIL")
def constructFileUCS(data):

    with open('output.txt', mode='wt', encoding='utf-8') as output_file:
        if data != 'FAILED':
            output_file.write(str(data[0]) + "\n")
            output_file.write(str(data[1][0]) + "\n")
            output_file.write('\n'.join(data[1][1]))

        else: 
            output_file.write("FAIL")



def neighborCheck(neighbors, explored, previousNodeDict):
    for j in neighbors:
        for i in explored:
            if j == i: 
                previousNodeDict.update({i:j})
    

def bfs(graph, startingNode, endNode, movements, graphDimensions):
    frontier = deque()
    previousNodeDict = dict()

    # Add first stuff to lists
    frontier.append(startingNode)
    explored = dict()

    while len(frontier)>0:
        node = frontier.popleft()
        value = checkBounds(node, graphDimensions)
        if value == "fail":
            continue

        #explored.append(node) 
        explored[node]= '' 
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
                    #print("WOOOF")
                    shortestRoute =calculateShortestPath(startingNode, endNode, previousNodeDict)
                    return shortestRoute
                frontier.append(x)
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

    graphDictionary = dict()

    for item in Lines[5:]:
        nodeLocation= ' '.join(item.split()[:3])
        nodeMoves= ' '.join(item.split()[3:])
        graphDictionary[nodeLocation] = nodeMoves

    return graphDictionary,inputDict





 
def updateFrontierCost(node, frontierTracker, cost):
    potentialCost = int(node[0])+ cost
    if potentialCost < int(frontierTracker[node[1]]):
        newCost = {node[1]: potentialCost}
        frontierTracker.update(newCost)

def updateCost (node, frontierTracker, cost, shallowCost):

    newCost = int(shallowCost) + cost #Add existing cost to new cost
    entry = {node:newCost}
    frontierTracker.update(entry)
        

def checkInFrontier(node, frontierQueue):
    value= any((node) in item for item in frontierQueue)
    return value
def checkTupleInExplored(node, explored):
    value =  [ y for x, y in explored if y  ==  node ]
    return value


def findIndexofHeapQ(heapq,value):
    for x in range(0,len(heapq)):
        if heapq[x][1] == value:
            return x
    return 0 
def calculateOutput(startingNode,endNode,frontierTracker,parentNode, localCost):
    cumulativeCost = frontierTracker[endNode]
    shortestPath = calculateShortestPathUCS(startingNode,endNode,parentNode, localCost)
    data = cumulativeCost, shortestPath
    constructFileUCS(data)

def UCSv4(graph, startingNode, endNode, movements, graphDimensions):
    frontierTracker = dict()
    localCost= dict()
    parentNode= dict()

    frontier_ucs_heapq = []
    heapq.heappush(frontier_ucs_heapq, (0, startingNode))

    frontierTracker[startingNode] = 0
    localCost[startingNode] =0
    parentNode[startingNode] ='0'

    explored = dict()

    while len(frontier_ucs_heapq)>0:
        node = heapq.heappop(frontier_ucs_heapq)
        value = checkBounds(node[1], graphDimensions)
        if value == "fail":
            continue

        if node[1] == endNode: 
            calculateOutput(startingNode,endNode,frontierTracker,parentNode, localCost)
            return

        #explored.append(node[1])
        explored[node[1]]= ''

        neighbors = findNeighborsUCS(node, movements, graph)
    
        for x in neighbors:
            # previous parent node cost + neighbor cost
            neighborCost = int(x[0])+ int(frontierTracker[node[1]])

            #if not any (x[1] == b for a, b in frontier_ucs_heapq) and x[1] not in explored:
            if not any (x[1] == b for a, b in frontier_ucs_heapq) and  x[1] not in explored:
          
                heapq.heappush(frontier_ucs_heapq, (neighborCost, x[1]))
                frontierTracker[x[1]] = neighborCost
                localCost[x[1]] = int(x[0])
                parentNode[x[1]] = node[1]
                
            elif  any (x[1] == b for a, b in frontier_ucs_heapq):
                if neighborCost < int(frontierTracker[x[1]]):   
                    newCost = {x[1]: neighborCost}
                    frontierTracker.update(newCost)
                    localCost[x[1]] = int(x[0])
                    parentNode[x[1]] = node[1]

                    index = findIndexofHeapQ(frontier_ucs_heapq,x[1])
                    if index == 0: 
                        break
                    else:
                        frontier_ucs_heapq[index] = frontier_ucs_heapq[-1]
                        frontier_ucs_heapq.pop()
                        heapq.heappush(frontier_ucs_heapq, (neighborCost, x[1]))
                        heapq.heapify(frontier_ucs_heapq)
                    
    constructFile("FAILED")  

def findEuclideanDistance(currentNode, endNode):
    currentNodeValue = currentNode
    currentNodeValueList = currentNodeValue.split()
    cn_x_coordinate = int(currentNodeValueList[0])
    cn_y_coordinate = int(currentNodeValueList[1])
    cn_z_coordinate = int(currentNodeValueList[2])

    endNodeValue =endNode
    endNodeValueList = endNodeValue.split()
    en_x_coordinate = int(endNodeValueList[0])
    en_y_coordinate = int(endNodeValueList[1])
    en_z_coordinate = int(endNodeValueList[2])

    #Calculate distance 
    x_difference = en_x_coordinate - cn_x_coordinate
    y_difference = en_y_coordinate - cn_y_coordinate
    z_difference = en_z_coordinate - cn_z_coordinate

    x_difference = x_difference**2
    y_difference = y_difference**2
    z_difference = z_difference**2

    sum = x_difference + y_difference + z_difference
    distance = math.sqrt(sum)

    return distance


def Astarsearch(graph, startingNode, endNode, movements, graphDimensions):
    frontierTracker = dict()
    localCost= dict()
    parentNode= dict()

    frontier_ucs_heapq = []
    heapq.heappush(frontier_ucs_heapq, (0, startingNode))

    frontierTracker[startingNode] = 0
    localCost[startingNode] =0
    parentNode[startingNode] ='0'

    explored = dict()

    while len(frontier_ucs_heapq)>0:
        node = heapq.heappop(frontier_ucs_heapq)
        value = checkBounds(node[1], graphDimensions)
        if value == "fail":
            continue

        if node[1] == endNode: 
            calculateOutput(startingNode,endNode,frontierTracker,parentNode, localCost)
            return
        #explored.append(node[1])
        explored[node[1]]= ''

        neighbors = findNeighborsUCS(node, movements, graph)
    
        for x in neighbors:
            # previous parent node cost + neighbor cost
            euclideanDistance = findEuclideanDistance(x[1], endNode)
            neighborCost = int(x[0])+ int(frontierTracker[node[1]]) 
            f_distance = neighborCost + euclideanDistance

            if not any (x[1] == b for a, b in frontier_ucs_heapq) and x[1] not in explored:

                heapq.heappush(frontier_ucs_heapq, (f_distance, x[1]))
                frontierTracker[x[1]] = neighborCost
                localCost[x[1]] = int(x[0])
                parentNode[x[1]] = node[1]
                
            elif  any (x[1] == b for a, b in frontier_ucs_heapq):
                if neighborCost < int(frontierTracker[x[1]]):   
                    newCost = {x[1]: neighborCost}
                    frontierTracker.update(newCost)
                    localCost[x[1]] = int(x[0])
                    parentNode[x[1]] = node[1]

                    index = findIndexofHeapQ(frontier_ucs_heapq,x[1])
                    if index == 0: 
                        break
                    else:
                        frontier_ucs_heapq[index] = frontier_ucs_heapq[-1]
                        frontier_ucs_heapq.pop()
                        heapq.heappush(frontier_ucs_heapq, (f_distance, x[1]))
                        heapq.heapify(frontier_ucs_heapq)
    constructFile("FAILED")          
      
if __name__ == "__main__":
    directory = os.getcwd()
    pathName = os.path.join(directory,"bfs_input.txt")

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
    
    data = initiateGraph(pathName)

    if data[1]["graphType"] == "BFS":
        dataExtracted=   bfs(data[0],data[1]["start"],data[1]["end"], movements, data[1]["graphDimensions"])
        outputFileContent = constructFile (dataExtracted)


    elif data[1]["graphType"] == "UCS":
        dataExtracted =   UCSv4(data[0],data[1]["start"],data[1]["end"], movements, data[1]["graphDimensions"])
    
    elif data[1]["graphType"] == "A*":
        dataExtracted =  Astarsearch(data[0],data[1]["start"],data[1]["end"], movements, data[1]["graphDimensions"])


    
    '''

    bfsData = initiateGraph("/home/dianaoh/aihw1/bfs_input.txt")
    bfsPath = bfs(bfsData[0],bfsData[1]["start"],bfsData[1]["end"], movements, bfsData[1]["graphDimensions"])
    outputFileContent = constructFile (bfsPath)

    
    ucsData = initiateGraph("/home/dianaoh/aihw1/usc_input.txt")
    bfsPath = UCSv4(ucsData[0],ucsData[1]["start"],ucsData[1]["end"], movements, ucsData[1]["graphDimensions"])


    astarData=  initiateGraph("/home/dianaoh/aihw1/astar_input.txt")
    astarPath =  Astarsearch(astarData[0],astarData[1]["start"],astarData[1]["end"], movements, astarData[1]["graphDimensions"])
    print('test')
    '''