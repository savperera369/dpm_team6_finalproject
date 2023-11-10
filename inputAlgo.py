from pathfinding import *

if __name__ == '__main__':

    jobs = []

    for i in range(3):
        userInput = input("Enter Coordinates of a Fire and Type of Fire: ")
        fires = userInput.split(",")
        tupleInput = (fires[0], fires[1], fires[2])
        jobs.append(tupleInput)

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
        dist, pathArr = minDistance(grid)
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
            print(pathArr)
        else:
            print("No path")
            break

    print(finalPath)