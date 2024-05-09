class Vertex:
  def __init__(self, label):
    self.label = label
    self.visiting = False
    self.adjacents = []

  def add_adjacent(self, adjacent):
    self.adjacents.append(adjacent)

  def show_adjacents(self):
    for i in self.adjacents:
      print(i.vertex.label, i.cost)

# Criando os vértices
arad = Vertex('Arad') 
zerind = Vertex('Zerind') 
oradea = Vertex('Oradea') 
sibiu = Vertex('Sibiu') 
timisoara = Vertex('Timisoara') 
lugoj = Vertex('Lugoj') 
mehadia = Vertex('Mehadia') 
dobreta = Vertex('Dobreta')
craiova = Vertex('Craiova')
rimnicu = Vertex('Rimnicu')
fagaras = Vertex('Fagaras')
pitesti = Vertex('Pitesti')
bucharest = Vertex('Bucharest')
giurgiu = Vertex('Giurgiu')
urzioeni = Vertex('Urzioeni')
neamt = Vertex('Neamt')
iasi = Vertex('Iasi')
vaslui = Vertex('Vaslui')
hirasova = Vertex('Hirasova')
eforie = Vertex('Eforie')