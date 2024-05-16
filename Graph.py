# Importando os vértices
from Vertice import arad, zerind, oradea, sibiu, timisoara, lugoj, mehadia, dobreta, craiova, rimnicu, fagaras, pitesti, bucharest, giurgiu, urzioeni, neamt, iasi, vaslui, hirasova, eforie

# Importando o módulo sys
import sys

class Graph:
  # instanciando a Classe de Grafos com os vétices do exercício
  def __init__(self) -> None:
    self.vertices = [ 
          arad, zerind, oradea, sibiu, timisoara, 
          lugoj, mehadia, dobreta, craiova, rimnicu, 
          fagaras, pitesti, bucharest, giurgiu, urzioeni, 
          neamt, iasi, vaslui, hirasova, eforie 
    ] 
  
  # criando algortimo de dijkstra para saber o caminho mais curto
  def dijkstra(self, origin):
    
    distances = {vertex: sys.maxsize for vertex in self.vertices}
    distances[origin] = 0
    
    predecessors = {vertex: None for vertex in self.vertices}  # Corrected line

    visited = set()

    while len(visited) < len(self.vertices):
      min_distance = None
      for vertex in self.vertices:
        if vertex not in visited and (min_distance is None or distances[vertex] < distances[min_distance]):
          min_distance = vertex
      visited.add(min_distance)
      for adjacente in min_distance.adjacents:
        new_distance = distances[min_distance] + adjacente.cost
        if new_distance < distances[adjacente.vertex]:
          distances[adjacente.vertex] = new_distance
          predecessors[adjacente.vertex] = min_distance
    return distances, predecessors
  
  # função para encontrar o melhor caminho entre determinados vértices
  def shortest_path(self, start, end, predecessors, m):
    path = []
    current_vertex = end
    while current_vertex is not None:
      path.insert(0, current_vertex)
      current_vertex = predecessors[current_vertex]
    
    if path[0] != start:
      return None
    
    start_label = start.label if hasattr(start, 'label') else str(start)
    
    end_label = end.label if hasattr(end, 'label') else str(end)
    
    path_labels = ' -> '.join(vertex.label for vertex in path)

    return f"O melhor caminho de {start_label} até {end_label} é: {path_labels}, percorrendo: {m}m"

# Instânciando um grafo
graph = Graph()


