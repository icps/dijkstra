#!/usr/bin/env python
# coding: utf-8

import heapq

#### Graph transformation

def even(vertex):
    return vertex * 10 + 2
    
def odd(vertex):
    return vertex * 10 + 1


def _add_edge(graph, v1, v2, w):
    if v1 not in graph.keys():
        graph[v1] = {}
        
    graph[v1][v2] = w

    
def add_edge(graph, v1, v2, w):
    _add_edge(graph, even(v1), odd(v2), w)
    _add_edge(graph, odd(v1), even(v2), w)
    
    _add_edge(graph, even(v2), odd(v1), w)
    _add_edge(graph, odd(v2), even(v1), w)
    

    
#### Dijkstra Algorithm
def dijkstra(graph, source, destination):
    
    queue = []
    dist  = {k: 20000 for k in graph.keys()}   ### initialize each node distance
    
    heapq.heappush(queue, (0, source))
    dist[source] = 0
    
    while queue:
        mdist, node = heapq.heappop(queue)
        
        for edge in graph[node].items():
            neighbor = edge[0]
            cweight  = edge[1]
            
            if(dist[node] + cweight < dist[neighbor]):
                dist[neighbor] = dist[node] + cweight
                heapq.heappush(queue, (dist[neighbor], neighbor))

    return dist[destination]
            
    
    
def main():

    V, E  = map(int, input().split(" "))

    graph = {}
    
    for _ in range(int(E)):
        
        v1, v2, w = map(int, input().split(" "))

        add_edge(graph, v1, v2, w)
    
    path = dijkstra(graph, 12, odd(V))
    
    if path == 20000:
        print(":(")
    else:
        print(path)
        

if __name__ == "__main__":
    main()

