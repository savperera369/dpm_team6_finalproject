# Written by Saviru
from pathfinding import *

def createPath(arrJobs):
    grid = []

    #give the grid some structure before we modify it to reflect the client specifications
    for i in range(4):
        grid.append(['*', '*', '*', '*'])

    #mark coordinates in the grid with fires to correspond to the coordinates input by user
    #mark them with 'd' to mirror the source to destination structure specified by the pathfinding algorithm
    for job in jobs:
        (x,y,fireType) = job
        grid[int(x)][int(y)] = 'd'
 
    #set the initial source location for the grid at coordinates 0,0
    grid[0][0] = 's'
    
    for row in grid:
        print(row)
        print("\n")

    #following variables initialize the final path, and create 
    #variables to keep track of the dynamically changing source variable
    finalPath = []
    sourceX = 0
    sourceY = 0
    for i in range(3):
        #call minDistance, which is the pathfinding algorithm three times for each fire
        pathArr = minDistance(grid)
        if pathArr != []:
            #mark the fire put out in this current interation as '0' so the algorithm knows to avoid it in next iterations
            xCord = pathArr[len(pathArr)-1][0]
            yCord = pathArr[len(pathArr)-1][1]
            grid[xCord][yCord] = '0'
            #update current source location as a square now available for traversal
            grid[sourceX][sourceY] = '*'
            #set the coordinates of the location in the path directly before the fire as the new source location
            newSourceX = pathArr[len(pathArr)-2][0]
            newSourceY = pathArr[len(pathArr)-2][1]
            grid[newSourceX][newSourceY] = 's'
            sourceX = newSourceX
            sourceY = newSourceY
            #add the path from the current source to current fire to the overall path varianle
            for node in pathArr:
                finalPath.append(node)
        else:
            print("No path")
            break
    
    #construct a path from the last fire back to the origin which is the original source location
    #and append this path to the overall/complete path variable finalPath
    grid[0][0] = 'd'
    lastPath = minDistance(grid)
    for element in lastPath:
        finalPath.append(element)

    return finalPath

if __name__ == '__main__':

    jobs = []

    #prompt user for input in the form of a 9 tuple
    userInput = input("Enter Coordinates of Fires and Types of Fires: ")
    fires = userInput.split(",")
    
    #parse the jobs as three seperate three tuples
    i = 0
    while i<9:
        tupleInput = (fires[i], fires[i+1], fires[i+2])
        jobs.append(tupleInput)
        i = i + 3
    
    listOfCoordinates = createPath(jobs)

    print("Final Path: \n")
    print(listOfCoordinates)
    print("\n")
    