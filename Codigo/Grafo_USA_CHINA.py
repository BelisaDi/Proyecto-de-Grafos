import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

countries = ['AUS','BRA','CAN','CHN','DEU','ESP','FRA','GBR','HKG','ITA','JPN','KOR','MEX','MYS','NLD','SGP','USA']
for pais in countries:
    G.add_node(pais)

"""
ARISTAS DE EXPORTACIONES ESTADOUNIDENSES
"""

G.add_edge('USA','AUS', capacity = 20600)
G.add_edge('USA','BRA', capacity = 20500)
G.add_edge('USA','CAN', capacity = 149700)
G.add_edge('USA','DEU', capacity = 61600)
G.add_edge('USA','ESP', capacity = 14900)
G.add_edge('USA','FRA', capacity = 37400)
G.add_edge('USA','GBR', capacity = 46700)
G.add_edge('USA','HKG', capacity = 30500)
G.add_edge('USA','ITA', capacity = 16700)
G.add_edge('USA','JPN', capacity = 67000)
G.add_edge('USA','KOR', capacity = 48800)
G.add_edge('USA','MEX', capacity = 181700)
G.add_edge('USA','MYS', capacity = 14700)
G.add_edge('USA','NLD', capacity = 35200)
G.add_edge('USA','SGP', capacity = 24400)

"""
ARISTAS DE IMPORTACIONES CHINENSES
"""

G.add_edge('AUS','CHN', capacity = 85000)
G.add_edge('BRA','CHN', capacity = 48000)
G.add_edge('CAN','CHN', capacity = 18500)
G.add_edge('DEU','CHN', capacity = 95100)
G.add_edge('ESP','CHN', capacity = 7500)
G.add_edge('FRA','CHN', capacity = 22200)
G.add_edge('GBR','CHN', capacity = 22000)
G.add_edge('HKG','CHN', capacity = 16400)
G.add_edge('ITA','CHN', capacity = 16400)
G.add_edge('JPN','CHN', capacity = 136100)
G.add_edge('KOR','CHN', capacity = 149900)
G.add_edge('MEX','CHN', capacity = 9000)
G.add_edge('MYS','CHN', capacity = 42600)
G.add_edge('NLD','CHN', capacity = 12000)
G.add_edge('SGP','CHN', capacity = 50400)

"""
RELACIONES ENTRE HKG, ITA, JPN, KOR, MEX, MYS, NLD, SGP.
"""

"""
ORIGEN EN HONG KONG (HKG)
"""

G.add_edge('HKG','ITA', capacity = 400)
G.add_edge('HKG','JPN', capacity = 1500)
G.add_edge('HKG','KOR', capacity = 2100)
G.add_edge('HKG','MEX', capacity = 300)
G.add_edge('HKG','MYS', capacity = 3300)
G.add_edge('HKG','NLD', capacity = 6200)
G.add_edge('HKG','SGP', capacity = 3700)

"""
DESTINO EN HONG KONG (HKG)
"""

G.add_edge('ITA','HKG', capacity = 6400)
G.add_edge('JPN','HKG', capacity = 32200)
G.add_edge('KOR','HKG', capacity = 34900)
G.add_edge('MEX','HKG', capacity = 900)
G.add_edge('MYS','HKG', capacity = 13700)
G.add_edge('NLD','HKG', capacity = 2700)
G.add_edge('SGP','HKG', capacity = 60900)

"""
ORIGEN EN ITALIA (ITA)
"""

G.add_edge('ITA','JPN', capacity = 8400)
G.add_edge('ITA','KOR', capacity = 5500)
G.add_edge('ITA','MEX', capacity = 5500)
G.add_edge('ITA','MYS', capacity = 1600)
G.add_edge('ITA','NLD', capacity = 11600)
G.add_edge('ITA','SGP', capacity = 3100)

"""
DESTINO EN ITALIA (ITA)
"""

G.add_edge('JPN','ITA', capacity = 4800)
G.add_edge('KOR','ITA', capacity = 3900)
G.add_edge('MEX','ITA', capacity = 1200)
G.add_edge('MYS','ITA', capacity = 1200)
G.add_edge('NLD','ITA', capacity = 24800)
G.add_edge('SGP','ITA', capacity = 500)

"""
ORIGEN EN JAPÓN (JPN)
"""

G.add_edge('JPN','KOR', capacity = 54200)
G.add_edge('JPN','MEX', capacity = 14900)
G.add_edge('JPN','MYS', capacity = 13400)
G.add_edge('JPN','NLD', capacity = 9700)
G.add_edge('JPN','SGP', capacity = 17600)

"""
DESTINO EN JAPÓN (JPN)
"""

G.add_edge('KOR','JPN', capacity = 26900)
G.add_edge('MEX','JPN', capacity = 5600)
G.add_edge('MYS','JPN', capacity = 17800)
G.add_edge('NLD','JPN', capacity = 3000)
G.add_edge('SGP','JPN', capacity = 12200)

"""
ORIGEN EN COREA DEL SUR (KOR)
"""

G.add_edge('KOR','MEX', capacity = 11000)
G.add_edge('KOR','MYS', capacity = 8200)
G.add_edge('KOR','NLD', capacity = 4300)
G.add_edge('KOR','SGP', capacity = 18300)

"""
DESTINO EN COREA DEL SUR (KOR)
"""

G.add_edge('MEX','KOR', capacity = 4200)
G.add_edge('MYS','KOR', capacity = 8000)
G.add_edge('NLD','KOR', capacity = 6400)
G.add_edge('SGP','KOR', capacity = 14300)

"""
ORIGEN EN MÉXICO (MEX)
"""

G.add_edge('MEX','MYS', capacity = 900)
G.add_edge('MEX','NLD', capacity = 2100)
G.add_edge('MEX','SGP', capacity = 1400)

"""
DESTINO EN MÉXICO (MEX)
"""

G.add_edge('MYS','MEX', capacity = 3300)
G.add_edge('NLD','MEX', capacity = 2400)
G.add_edge('SGP','MEX', capacity = 1300)

"""
ORIGEN EN MALASIA (MYS)
"""

G.add_edge('MYS','NLD', capacity = 7500)
G.add_edge('MYS','SGP', capacity = 35800)

"""
DESTINO EN MALASIA (MYS)
"""

G.add_edge('NLD','MYS', capacity = 1800)
G.add_edge('SGP','MYS', capacity = 28500)

"""
ORIGEN EN PAISES BAJOS (NLD)
"""

G.add_edge('NLD','SGP', capacity = 5200)

"""
DESTINO EN PAISES BAJOS (NLD)
"""

G.add_edge('SGP','NLD', capacity = 5600)

nx.draw(G)
plt.show()
