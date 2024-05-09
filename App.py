from Graph import graph

from Adjacent import Adjacent

from Vertex import arad, zerind, oradea, sibiu, timisoara, lugoj, mehadia, dobreta, craiova, rimnicu, fagaras, pitesti, bucharest, giurgiu, urzioeni, neamt, iasi, vaslui, hirasova, eforie


def showGraphAdjacents(graph):
    print('**************************************************************************************************')
    print('Mostrandos os adjacentes de cada vértice do Grafo:')
    print('')
    for vertex in graph.vertices:
        print(f"Adjacentes de {vertex.label}:")
        vertex.show_adjacents()
        print('')
    print('**************************************************************************************************')

showGraphAdjacents(graph)

distances, path = graph.dijkstra(arad)

the_best_route_from_arad_to_bucharest = graph.shortest_path(arad, bucharest, path, distances[bucharest])

print(the_best_route_from_arad_to_bucharest)