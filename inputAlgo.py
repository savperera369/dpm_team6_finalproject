from pathfinding import *

if __name__ == '__main__':

    jobs = []

    userInput = input("Enter Coordinates of a Fire and Type of Fire: ")
    fires = userInput.split(",")
    
    i = 0
    while i<9:
        tupleInput = (fires[i], fires[i+1], fires[i+2])
        jobs.append(tupleInput)
        i = i + 3
    
    print(jobs)

    grid = []

    for i in range(4):
        grid.append(['*', '*', '*', '*'])

    for job in jobs:
        (x,y,fireType) = job
        grid[int(x)][int(y)] = 'd'
 
    grid[0][0] = 's'
    
    print(grid)
    finalPath = []
    sourceX = 0
    sourceY = 0
    for i in range(3):
        pathArr = minDistance(grid)
        if pathArr != []:
            xCord = pathArr[len(pathArr)-1][0]
            yCord = pathArr[len(pathArr)-1][1]
            grid[xCord][yCord] = '0'
            grid[sourceX][sourceY] = '*'
            newSourceX = pathArr[len(pathArr)-2][0]
            newSourceY = pathArr[len(pathArr)-2][1]
            grid[newSourceX][newSourceY] = 's'
            sourceX = newSourceX
            sourceY = newSourceY
            for node in pathArr:
                finalPath.append(node)
        else:
            print("No path")
            break
    
    grid[0][0] = 'd'
    lastPath = minDistance(grid)
    for element in lastPath:
        finalPath.append(element)

    print(finalPath)

    