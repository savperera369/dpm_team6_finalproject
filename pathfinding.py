class QItem:
    def __init__(self, row, col, dist, prev=None):
        self.row = row
        self.col = col
        self.dist = dist
        self.prev = prev  # Added a reference to the previous node

    def __repr__(self):
        return f"QItem({self.row}, {self.col}, {self.dist})"
 
def minDistance(grid):
    source = QItem(0, 0, 0)
 
    # Finding the source to start from
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 's':
                source.row = row
                source.col = col
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
 
        # Destination found
        if (grid[source.row][source.col] == 'd'):
            # Output the precise path
            path = []
            while source is not None:
                path.insert(0, (source.row, source.col))
                source = source.prev
            return path
 
        # Moving up
        if isValid(source.row - 1, source.col, grid, visited):
            next_node = QItem(source.row - 1, source.col, source.dist + 1, source)
            queue.append(next_node)
            visited[source.row - 1][source.col] = True
 
        # Moving down
        if isValid(source.row + 1, source.col, grid, visited):
            next_node = QItem(source.row + 1, source.col, source.dist + 1, source)
            queue.append(next_node)
            visited[source.row + 1][source.col] = True
 
        # Moving left
        if isValid(source.row, source.col - 1, grid, visited):
            next_node = QItem(source.row, source.col - 1, source.dist + 1, source)
            queue.append(next_node)
            visited[source.row][source.col - 1] = True
 
        # Moving right
        if isValid(source.row, source.col + 1, grid, visited):
            next_node = QItem(source.row, source.col + 1, source.dist + 1, source)
            queue.append(next_node)
            visited[source.row][source.col + 1] = True
 
    return -1, []
 
# Checking where move is valid or not
def isValid(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
        (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != '0') and (visited[x][y] == False)):
        return True
    return False
 
 
