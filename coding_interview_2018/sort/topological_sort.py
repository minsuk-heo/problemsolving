"""
In Directed Acyclic Graph (DAG), when A->B, A must comes before B in the ordering.
Implement topology sort to visit all vertice in the graph

a ---> d ---> e <--- c
       ^
       |
       b

"""

from collections import defaultdict

# store edge information in adjacency list
adjacency_list = defaultdict()
adjacency_list['a'] = ['d']
adjacency_list['b'] = ['d']
adjacency_list['c'] = ['e']
adjacency_list['d'] = ['e']
adjacency_list['e'] = []

# store visited vertex information in visited_list
visited_list = defaultdict()
visited_list['a'] = False
visited_list['b'] = False
visited_list['c'] = False
visited_list['d'] = False
visited_list['e'] = False

output_stack = []

'''
once visit vertex, change visited_list value to True so we don't revisit it again.
recursively run topology sort to the neighbors in adjacency list.
once all the neighbors are visited, put the current vertex in the output stack.
'''


def topology_sort(vertex):
    if not visited_list[vertex]:
        visited_list[vertex] = True
        for neighbor in adjacency_list[vertex]:
            topology_sort(neighbor)
        output_stack.insert(0, vertex)

for vertex in visited_list:
    topology_sort(vertex)

print(output_stack)