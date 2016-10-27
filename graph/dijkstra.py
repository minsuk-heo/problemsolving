# dijkstra's algorithm
"""
1. Assign to every node a distance value. Set it to zero for our initial node
   and to infinity for all other nodes.

2. Mark all nodes as unvisited. Set initial node as current.

3. For current node, consider all its unvisited neighbors and calculate their
   tentative distance (from the initial node). For example, if current node
   (A) has distance of 6, and an edge connecting it with another node (B)
   is 2, the distance to B through A will be 6+2=8. If this distance is less
   than the previously recorded distance (infinity in the beginning, zero
   for the initial node), overwrite the distance.

4. When we are done considering all neighbors of the current node, mark it as
   visited. A visited node will not be checked ever again; its distance
   recorded now is final and minimal.

5. If all nodes have been visited, finish. Otherwise, set the unvisited node
   with the smallest distance (from the initial node) as the next "current
   node" and continue from step 3.

 - source: wikipedia http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""


class Graph(object):
    """
    A simple undirected, weighted graph
    """

    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    current_node = initial_node
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        cur_wt = visited[min_node]

        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node

    return visited, path


def shortest_path(graph, initial_node, goal_node):
    distances, paths = dijkstra(graph, initial_node)
    route = [goal_node]

    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()
    return route


if __name__ == '__main__':
    g = Graph()
    g.nodes = set(range(1, 7))
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 6, 14)
    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)
    g.add_edge(3, 4, 11)
    g.add_edge(3, 6, 2)
    g.add_edge(4, 5, 6)
    g.add_edge(5, 6, 9)
    assert shortest_path(g, 1, 5) == [1, 3, 6, 5]
    assert shortest_path(g, 5, 1) == [5, 6, 3, 1]
    assert shortest_path(g, 2, 5) == [2, 3, 6, 5]
    assert shortest_path(g, 1, 4) == [1, 3, 4]