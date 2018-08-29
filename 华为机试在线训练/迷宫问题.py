def min_path_search(i, j, min_path, temp_path, N, M, maze):
    maze[i][j] = 1
    temp_path.append([i, j])
    if i == N - 1 and j == M - 1:
        if len(min_path) == 0 or len(temp_path) < len(min_path):
            del min_path[:]
            min_path.extend(temp_path)
    if i - 1 >= 0 and maze[i - 1][j] == 0:
        min_path_search(i - 1, j, min_path, temp_path, N, M, maze)
    if i + 1 < N and maze[i + 1][j] == 0:
        min_path_search(i + 1, j, min_path, temp_path, N, M, maze)
    if j - 1 >= 0 and maze[i][j - 1] == 0:
        min_path_search(i, j - 1, min_path, temp_path, N, M, maze)
    if j + 1 < M and maze[i][j + 1] == 0:
        min_path_search(i, j + 1, min_path, temp_path, N, M, maze)
    maze[i][j] = 0
    temp_path.pop()


while True:
    try:
        N, M = map(int, input().split())
        maze = []
        for i in range(N):
            maze.append(list(map(int, input().split())))
        min_path = []
        temp_path = []
        min_path_search(0, 0, min_path, temp_path, N, M, maze)
        for i in min_path:
            print('(%d,%d)' % (i[0], i[1]))
    except:
        break
