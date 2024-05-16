from Vertice import arad, zerind, oradea, sibiu, timisoara, lugoj, mehadia, dobreta, craiova, rimnicu, fagaras, pitesti, bucharest, giurgiu, urzioeni, neamt, iasi, vaslui, hirasova, eforie


class Adjacente:
  def __init__(self, vertice, peso):
    self.vertice = vertice
    self.peso = peso

# Arad
arad.adicionar_adjacente(Adjacente(zerind, 75))
arad.adicionar_adjacente(Adjacente(sibiu, 140))
arad.adicionar_adjacente(Adjacente(timisoara, 118))

# Zerind
zerind.adicionar_adjacente(Adjacente(oradea, 71))
zerind.adicionar_adjacente(Adjacente(zerind, 71)) 
oradea.adicionar_adjacente(Adjacente(sibiu, 151))

# Sibiu
sibiu.adicionar_adjacente(Adjacente(oradea, 151)) 
sibiu.adicionar_adjacente(Adjacente(arad, 140))
sibiu.adicionar_adjacente(Adjacente(fagaras, 99))
sibiu.adicionar_adjacente(Adjacente(rimnicu, 80))

# Timisoara
timisoara.adicionar_adjacente(Adjacente(arad, 118))
timisoara.adicionar_adjacente(Adjacente(lugoj, 111))

# Lugoj
lugoj.adicionar_adjacente(Adjacente(timisoara, 111))
lugoj.adicionar_adjacente(Adjacente(mehadia, 70))

# Mehadia
mehadia.adicionar_adjacente(Adjacente(lugoj, 70))
mehadia.adicionar_adjacente(Adjacente(dobreta, 75))

# Dobreta
dobreta.adicionar_adjacente(Adjacente(mehadia, 75))
dobreta.adicionar_adjacente(Adjacente(craiova, 120))

# Craiova
craiova.adicionar_adjacente(Adjacente(dobreta, 120))
craiova.adicionar_adjacente(Adjacente(pitesti, 138))
craiova.adicionar_adjacente(Adjacente(rimnicu, 146))

# Rimnicu
rimnicu.adiconar_adjacente(Adjacente(craiova, 146))
rimnicu.adicionar_adjacente(Adjacente(sibiu, 80))
rimnicu.adicionar_adjacente(Adjacente(pitesti, 97))

# Fagaras
fagaras.adicionar_adjacente(Adjacente(sibiu, 99))
fagaras.adicionar_adjacente(Adjacente(bucharest, 211))

# Pitest
pitesti.adicionar_adjacente(Adjacente(rimnicu, 97))
pitesti.adicionar_adjacente(Adjacente(craiova, 138))
pitesti.adicionar_adjacente(Adjacente(bucharest, 101))

# Bucharest
bucharest.adicionar_adjacente(Adjacente(fagaras, 211))
bucharest.adicionar_adjacente(Adjacente(pitesti, 101))
bucharest.adicionar_adjacente(Adjacente(giurgiu, 90))
bucharest.adicionar_adjacente(Adjacente(urzioeni, 85))

# Giurgiu
giurgiu.adicionar_adjacente(Adjacente(bucharest, 90))

# Neamt
neamt.adicionar_adjacente(Adjacente(iasi, 87))

# Iasi
iasi.adicionar_adjacente(Adjacente(neamt, 87))
iasi.adicionar_adjacente(Adjacente(vaslui, 92))

# Vaslui
vaslui.adicionar_adjacente(Adjacente(iasi, 92))
vaslui.adicionar_adjacente(Adjacente(urzioeni, 142))

# Urzioeni
urzioeni.adicionar_adjacente(Adjacente(hirasova, 98))
urzioeni.adicionar_adjacente(Adjacente(vaslui, 142))
urzioeni.adicionar_adjacente(Adjacente(bucharest, 85))

# Hirasova
hirasova.adicionar_adjacente(Adjacente(urzioeni, 98))
hirasova.adicionar_adjacente(Adjacente(eforie, 86))

# Eforie
eforie.adicionar_adjacente(Adjacente(hirasova, 86))

