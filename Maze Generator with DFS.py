import random

def generate_maze(n, m):
    maze = [["#" for _ in range(m)] for _ in range(n)]

    def dfs(x, y):
        maze[x][y] = " "
        directions = [(0,2),(0,-2),(2,0),(-2,0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 < nx < n-1 and 0 < ny < m-1 and maze[nx][ny] == "#":
                maze[x+dx//2][y+dy//2] = " "
                dfs(nx, ny)

    dfs(1,1)
    return maze

maze = generate_maze(15, 25)
for row in maze:
    print("".join(row))
