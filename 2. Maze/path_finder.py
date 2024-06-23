def dfs(visited, curcord, maze, path, end):
    if not (0 <= curcord[0] < len(maze) and 0 <= curcord[1] < len(maze[0])) or maze[curcord[0]][curcord[1]] == 0:
        return False

    if curcord == end:
        return True

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for direction in directions:
        newCord = (curcord[0] + direction[0], curcord[1] + direction[1])
        if not (0 <= newCord[0] < len(maze) and 0 <= newCord[1] < len(maze[0])):
            continue
        if not visited[newCord[0]][newCord[1]]:
            visited[newCord[0]][newCord[1]] = True
            if dfs(visited, newCord, maze, path, end):
                path.append(newCord)
                return True
            else:
                visited[newCord[0]][newCord[1]] = False
                
    return False

def find_path(maze, start, end):
    path = []
    vis = [[False for _ in range(len(maze))] for _ in range(len(maze))]
    vis[start[0]][start[1]] = True
    if dfs(vis, start, maze, path, end):
        path.append(start)
        path.reverse()
        return path
    return []
