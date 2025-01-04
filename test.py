maze = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 1, 2, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 1],
]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]





def bfs():
    '''
    BFS implementation to find path in maze
    Fixed issues:
    1. Removed invalid 'string entry' declaration
    2. Fixed syntax in coordinate unpacking
    3. Fixed queue pop syntax
    4. Corrected maze indexing
    5. Added queue empty check
    6. Fixed path finding logic
    7. Changed wall check condition
    '''
    entry = input("Enter the entry point (x, y): ")

    x, y = map(int, entry.split(","))
    n = len(maze)
    visited = [[False] * n for _ in range(n)]
    parent = {}

    queue = [(x, y)]
    visited[x][y] = True
    parent[(x, y)] = None

    while queue:    
        x, y = queue.pop(0)    
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if maze[nx][ny] == 2:  
                    parent[(nx, ny)] = (x, y)
                    path = []
                    curr = (nx, ny)
                    while curr is not None:
                        path.append(curr)
                        curr = parent[curr]
                        
                    path.reverse()
                    return path

                if maze[nx][ny] == 0:  # Changed from 1 to 0 as 1 represents walls
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    parent[(nx, ny)] = (x, y)
    return "No path found"





def main():
    path = bfs()
    print(path)


if __name__ == "__main__":
    main()