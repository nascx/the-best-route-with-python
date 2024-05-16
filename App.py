from Grafo import grafo

from Adjacente import Adjacente

from Vertice import arad, zerind, oradea, sibiu, timisoara, lugoj, mehadia, dobreta, craiova, rimnicu, fagaras, pitesti, bucharest, giurgiu, urzioeni, neamt, iasi, vaslui, hirasova, eforie


arad.mostrar_adjacentes()
zerind.mostrar_adjacentes()
oradea.mostrar_adjacentes()
sibiu.mostrar_adjacentes()
timisoara.mostrar_adjacentes()
lugoj.mostrar_adjacentes()
mehadia.mostrar_adjacentes()
dobreta.mostrar_adjacentes()
craiova.mostrar_adjacentes()
rimnicu.mostrar_adjacentes()
fagaras.mostrar_adjacentes()
pitesti.mostrar_adjacentes()
bucharest.mostrar_adjacentes()
giurgiu.mostrar_adjacentes()
urzioeni.mostrar_adjacentes()
neamt.mostrar_adjacentes()
iasi.mostrar_adjacentes()
vaslui.mostrar_adjacentes()
hirasova.mostrar_adjacentes()
eforie.mostrar_adjacentes()

distancias, caminho = grafo.algoritmo_de_dijkstra(arad)

melhor_caminho_de_arad_ate_bucherest = grafo.melhor_caminho(arad, bucharest, caminho, distancias[bucharest])

print(melhor_caminho_de_arad_ate_bucherest)