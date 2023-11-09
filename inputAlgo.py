from pathfinding import *

if __name__ == '__main__':

    jobs = []

    for i in range(3):
        userInput = input("Enter Coordinates of a Fire and Type of Fire")
        jobs.append(userInput)

    print(jobs)

    grid = [['0', '*', '0', 's'],
            ['*', '0', '*', '*'],
            ['0', '*', '*', '*'],
            ['d', '*', '*', '*']]
 
    dist, pathArr = minDistance(grid)
    print(dist)
    print(pathArr)