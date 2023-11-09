class QItem:
    def __init__(self, row, col, dist, path):
        self.row = row
        self.col = col
        self.dist = dist
        self.path = path
 
    def __repr__(self):
        return f"QItem({self.row}, {self.col}, {self.dist}, {self.path})"
 
def minDistance(grid):
    source = QItem(0, 0, 0, [])
 
    # Finding the source to start from
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 's':
                source.row = row
                source.col = col
                source.path.append((source.row,source.col))
                break
 
    # To maintain location visit status
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]
     
    # applying BFS on matrix cells starting from source
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True
    while len(queue) != 0:
        source = queue.pop(0)
 
        # Destination found;
        if (grid[source.row][source.col] == 'd'):
            return source.dist, source.path
 
        # moving up
        if isValid(source.row - 1, source.col, grid, visited):
            source.path.append([source.row - 1, source.col])
            queue.append(QItem(source.row - 1, source.col, source.dist + 1, source.path))
            visited[source.row - 1][source.col] = True
 
        # moving down
        if isValid(source.row + 1, source.col, grid, visited):
            source.path.append([source.row + 1, source.col])
            queue.append(QItem(source.row + 1, source.col, source.dist + 1, source.path))
            visited[source.row + 1][source.col] = True
 
        # moving left
        if isValid(source.row, source.col - 1, grid, visited):
            source.path.append([source.row, source.col - 1])
            queue.append(QItem(source.row, source.col - 1, source.dist + 1, source.path))
            visited[source.row][source.col - 1] = True
 
        # moving right
        if isValid(source.row, source.col + 1, grid, visited):
            source.path.append([source.row, source.col + 1])
            queue.append(QItem(source.row, source.col + 1, source.dist + 1, source.path))
            visited[source.row][source.col + 1] = True
 
    return -1, []
 
 
# checking where move is valid or not
def isValid(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
        (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != '0') and (visited[x][y] == False)):
        return True
    return False
 
