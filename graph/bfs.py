__author__ = 'Minsuk Heo'

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
links = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertices, links)

def bfs(graph, start):
    vertices, links = graph
    blacknodes = []
    graynodes = [start]
    neighbors = [[] for vertex in vertices]

    for link in links:
        neighbors[link[0]].append(link[1])

    while graynodes:
        current = graynodes.pop()
        for neighbor in neighbors[current]:
            if not neighbor in blacknodes + graynodes:
                graynodes.insert(0,neighbor)
        blacknodes.append(current)
    return blacknodes

print(vertices)
print(bfs(graphs, 0))

