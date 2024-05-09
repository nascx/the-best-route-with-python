from Vertex import arad, zerind, oradea, sibiu, timisoara, lugoj, mehadia, dobreta, craiova, rimnicu, fagaras, pitesti, bucharest, giurgiu, urzioeni, neamt, iasi, vaslui, hirasova, eforie


class Adjacent:
  def __init__(self, vertex, cost):
    self.vertex = vertex
    self.cost = cost

# Arad
arad.add_adjacent(Adjacent(zerind, 75))
arad.add_adjacent(Adjacent(sibiu, 140))
arad.add_adjacent(Adjacent(timisoara, 118))

# Zerind
zerind.add_adjacent(Adjacent(oradea, 71))
zerind.add_adjacent(Adjacent(arad, 75))

# Oradea
oradea.add_adjacent(Adjacent(zerind, 71)) 
oradea.add_adjacent(Adjacent(sibiu, 151))

# Sibiu
sibiu.add_adjacent(Adjacent(oradea, 151)) 
sibiu.add_adjacent(Adjacent(arad, 140))
sibiu.add_adjacent(Adjacent(fagaras, 99))
sibiu.add_adjacent(Adjacent(rimnicu, 80))

# Timisoara
timisoara.add_adjacent(Adjacent(arad, 118))
timisoara.add_adjacent(Adjacent(lugoj, 111))

# Lugoj
lugoj.add_adjacent(Adjacent(timisoara, 111))
lugoj.add_adjacent(Adjacent(mehadia, 70))

# Mehadia
mehadia.add_adjacent(Adjacent(lugoj, 70))
mehadia.add_adjacent(Adjacent(dobreta, 75))

# Dobreta
dobreta.add_adjacent(Adjacent(mehadia, 75))
dobreta.add_adjacent(Adjacent(craiova, 120))

# Craiova
craiova.add_adjacent(Adjacent(dobreta, 120))
craiova.add_adjacent(Adjacent(pitesti, 138))
craiova.add_adjacent(Adjacent(rimnicu, 146))

# Rimnicu
rimnicu.add_adjacent(Adjacent(craiova, 146))
rimnicu.add_adjacent(Adjacent(sibiu, 80))
rimnicu.add_adjacent(Adjacent(pitesti, 97))

# Fagaras
fagaras.add_adjacent(Adjacent(sibiu, 99))
fagaras.add_adjacent(Adjacent(bucharest, 211))

# Pitest
pitesti.add_adjacent(Adjacent(rimnicu, 97))
pitesti.add_adjacent(Adjacent(craiova, 138))
pitesti.add_adjacent(Adjacent(bucharest, 101))

# Bucharest
bucharest.add_adjacent(Adjacent(fagaras, 211))
bucharest.add_adjacent(Adjacent(pitesti, 101))
bucharest.add_adjacent(Adjacent(giurgiu, 90))
bucharest.add_adjacent(Adjacent(urzioeni, 85))

# Giurgiu
giurgiu.add_adjacent(Adjacent(bucharest, 90))

# Neamt
neamt.add_adjacent(Adjacent(iasi, 87))

# Iasi
iasi.add_adjacent(Adjacent(neamt, 87))
iasi.add_adjacent(Adjacent(vaslui, 92))

# Vaslui
vaslui.add_adjacent(Adjacent(iasi, 92))
vaslui.add_adjacent(Adjacent(urzioeni, 142))

# Urzioeni
urzioeni.add_adjacent(Adjacent(hirasova, 98))
urzioeni.add_adjacent(Adjacent(vaslui, 142))
urzioeni.add_adjacent(Adjacent(bucharest, 85))

# Hirasova
hirasova.add_adjacent(Adjacent(urzioeni, 98))
hirasova.add_adjacent(Adjacent(eforie, 86))

# Eforie
eforie.add_adjacent(Adjacent(hirasova, 86))

