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

    dist, pathArr = minDistance(grid)
    print(dist)
    print(pathArr)