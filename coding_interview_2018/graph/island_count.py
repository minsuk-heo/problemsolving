"""

0 0 0 0 1
1 1 0 0 1
1 1 0 1 0
0 0 1 1 0
0 0 0 0 1

total 4 islands

1 0 0
0 1 0
0 1 1

total 2 islands

"""

def adjacency_land(i,j, map):
    if i >= 0 and i < len(map) and j >= 0 and j < len(map[0]):
        if map[i][j] == 1:
            map[i][j] = 0
            adjacency_land(i - 1, j, map)
            adjacency_land(i + 1, j, map)
            adjacency_land(i, j - 1, map)
            adjacency_land(i, j + 1, map)

def island_count(map):
    cnt = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                cnt += 1
                map[i][j] = 0
                adjacency_land(i-1, j, map)
                adjacency_land(i+1, j, map)
                adjacency_land(i, j-1, map)
                adjacency_land(i, j+1, map)
    return cnt


map = [ [0,0,0,0,1],[1,1,0,0,1], [1,1,0,1,0], [0,0,1,1,0], [0,0,0,0,1]]
print(island_count(map))

map = [ [1,0,0],[0,1,0], [0,1,1]]
print(island_count(map))