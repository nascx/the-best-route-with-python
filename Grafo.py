# Importando os vértices
from Vertice import arad, zerind, oradea, sibiu, timisoara, lugoj, mehadia, dobreta, craiova, rimnicu, fagaras, pitesti, bucharest, giurgiu, urzioeni, neamt, iasi, vaslui, hirasova, eforie

# Importando o módulo sys
import sys

class Grafo:
  # instanciando a Classe de Grafos com os vétices do exercício
  def __init__(self) -> None:
    self.vertices = [ 
          arad, zerind, oradea, sibiu, timisoara, 
          lugoj, mehadia, dobreta, craiova, rimnicu, 
          fagaras, pitesti, bucharest, giurgiu, urzioeni, 
          neamt, iasi, vaslui, hirasova, eforie 
    ] 
  
  # criando algortimo de dijkstra para saber o caminho mais curto
  def algoritmo_de_dijkstra(self, origem):
    distancias = {vertice: sys.maxsize for vertice in self.vertices}
    
    distancias[origem] = 0
    
    antecessores = {vertice: None for vertice in self.vertices} 

    visitado = set()

    while len(visitado) < len(self.vertices):
      distancia_minima = None
      for vertice in self.vertices:
        if vertice not in visitado and (distancia_minima is None or distancias[vertice] < distancias[distancia_minima]):
          distancia_minima = vertice
      visitado.add(distancia_minima)
      for adjacente in distancia_minima.adjacentes:
        nova_distancia = distancias[distancia_minima] + adjacente.peso
        if nova_distancia < distancias[adjacente.vertice]:
          distancias[adjacente.vertice] = nova_distancia
          antecessores[adjacente.vertice] = distancia_minima
    return distancias, antecessores
  
  # função para encontrar o melhor caminho entre determinados vértices
  def melhor_caminho(self, origem, destino, antecessores, distancia):
    caminho = []
    vertice_atual = destino
    while vertice_atual is not None:
      caminho.insert(0, vertice_atual)
      vertice_atual = antecessores[vertice_atual]
    
    if caminho[0] != origem:
      return None
    
    origemStr = origem.label if hasattr(origem, 'label') else str(origem)
    
    destinoStr = destino.label if hasattr(destino, 'label') else str(destino)
    
    caminhoStr = ' ---> '.join(vertice.label for vertice in caminho)

    return f"Percorrendo a ditância de {distancia}m. O melhor caminho de {origemStr} até {destinoStr} é: {caminhoStr}"

# Instânciando um grafo
grafo = Grafo()


