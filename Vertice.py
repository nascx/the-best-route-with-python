class Vertice:
  def __init__(self, label):
    self.label = label
    self.vitados = False
    self.adjacentes = []

  def adicionar_adjacente(self, adjacente):
    self.adjacentes.append(adjacente)

  def mostrar_adjacentes(self):
    for i in self.adjacentes:
      print("***************************")
      print("Vertices de ", self.label)
      print(i.vertice.label, i.peso)
      print("***************************")

# Criando os vértices
arad = Vertice('Arad') 
zerind = Vertice('Zerind') 
oradea = Vertice('Oradea') 
sibiu = Vertice('Sibiu') 
timisoara = Vertice('Timisoara') 
lugoj = Vertice('Lugoj') 
mehadia = Vertice('Mehadia') 
dobreta = Vertice('Dobreta')
craiova = Vertice('Craiova')
rimnicu = Vertice('Rimnicu')
fagaras = Vertice('Fagaras')
pitesti = Vertice('Pitesti')
bucharest = Vertice('Bucharest')
giurgiu = Vertice('Giurgiu')
urzioeni = Vertice('Urzioeni')
neamt = Vertice('Neamt')
iasi = Vertice('Iasi')
vaslui = Vertice('Vaslui')
hirasova = Vertice('Hirasova')
eforie = Vertice('Eforie')