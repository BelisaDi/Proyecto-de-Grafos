import matplotlib.pyplot as plt
import networkx as nx

countries = ['AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'ESP', 'FRA', 'GBR', 'HKG', 'ITA', 'JPN', 'KOR', 'MEX', 'MYS', 'NLD', 'SGP', 'USA']

G= nx.DiGraph()
for pais in countries:
    G.add_node(pais)

"""
ARISTAS DE EXPORTACIONES CHINENSES
"""
G.add_edge('CHN','AUS', capacity = 47021)
G.add_edge('CHN','BRA', capacity = 27023)
G.add_edge('CHN','CAN', capacity = 50002)
G.add_edge('CHN','DEU', capacity = 109148)
G.add_edge('CHN','ESP', capacity = 28569)
G.add_edge('CHN','FRA', capacity = 52931)
G.add_edge('CHN','GBR', capacity = 58909)
G.add_edge('CHN','HKG', capacity = 255880)
G.add_edge('CHN','ITA', capacity = 31848)
G.add_edge('CHN','JPN', capacity = 157034)
G.add_edge('CHN','KOR', capacity = 98144)
G.add_edge('CHN','MEX', capacity = 52072)
G.add_edge('CHN','MYS', capacity = 38072)
G.add_edge('CHN','NLD', capacity = 43896)
G.add_edge('CHN','SGP', capacity = 42648)

"""
ARISTAS DE IMPORTACION ESTADOUNIDENSE
"""
G.add_edge('USA','AUS', capacity = 8572)
G.add_edge('USA','BRA', capacity = 25053)
G.add_edge('USA','CAN', capacity = 274883)
G.add_edge('USA','DEU', capacity = 111960)
G.add_edge('USA','ESP', capacity = 14156)
G.add_edge('USA','FRA', capacity = 36041)
G.add_edge('USA','GBR', capacity = 45221)
G.add_edge('USA','HKG', capacity = 4082)
G.add_edge('USA','ITA', capacity = 44957)
G.add_edge('USA','JPN', capacity = 125227)
G.add_edge('USA','KOR', capacity = 69360)
G.add_edge('USA','MEX', capacity = 307186)
G.add_edge('USA','MYS', capacity = 33071)
G.add_edge('USA','NLD', capacity = 16390)
G.add_edge('USA','SGP', capacity = 16636)

"""
RELACIONES ENTRE AUS, BRA, CAN, DEU, ESP, FRA, GBR
"""

"""
ORIGEN EN AUSTRALIA(AUS)
"""
G.add_edge('AUS','BRA', capacity = 1400)
G.add_edge('AUS','CAN', capacity = 1400)
G.add_edge('AUS','DEU', capacity = 2500)
G.add_edge('AUS','ESP', capacity = 700)
G.add_edge('AUS','FRA', capacity = 1300)
G.add_edge('AUS','GBR', capacity = 4800)

"""
DESTINO A AUSTRALIA(AUS)
"""
G.add_edge('BRA','AUS', capacity = 600)
G.add_edge('CAN','AUS', capacity = 1400)
G.add_edge('DEU','AUS', capacity = 9300)
G.add_edge('ESP','AUS', capacity = 1700)
G.add_edge('FRA','AUS', capacity = 3100)
G.add_edge('GBR','AUS', capacity = 5000)

"""
ORIGEN EN BRAZIL(BRA)
"""
G.add_edge('BRA','CAN', capacity = 2700)
G.add_edge('BRA','DEU', capacity = 6200)
G.add_edge('BRA','ESP', capacity = 4200)
G.add_edge('BRA','FRA', capacity = 2800)
G.add_edge('BRA','GBR', capacity = 3100)

"""
DESTINO A BRAZIL(BRA)
"""
G.add_edge('CAN','BRA', capacity = 1400)
G.add_edge('DEU','BRA', capacity = 9300)
G.add_edge('ESP','BRA', capacity = 2900)
G.add_edge('FRA','BRA', capacity = 3700)
G.add_edge('GBR','BRA', capacity = 2400)

"""
ORIGEN EN CANADA(CAN)
"""
G.add_edge('CAN','DEU', capacity = 3800)
G.add_edge('CAN','ESP', capacity = 1800)
G.add_edge('CAN','FRA', capacity = 3100)
G.add_edge('CAN','GBR', capacity = 7500)

"""
DESTINO A CANADA(CAN)
"""
G.add_edge('DEU','CAN', capacity = 12400)
G.add_edge('ESP','CAN', capacity = 1900)
G.add_edge('FRA','CAN', capacity = 4200)
G.add_edge('GBR','CAN', capacity = 6200)

"""
ORIGEN EN ALEMANIA(DEU)
"""
G.add_edge('DEU','ESP', capacity = 43600)
G.add_edge('DEU','FRA', capacity = 104000)
G.add_edge('DEU','GBR', capacity = 90300)

"""
DESTINO A ALEMANIA(DEU)
"""
G.add_edge('ESP','DEU', capacity = 34000)
G.add_edge('FRA','DEU', capacity = 69200)
G.add_edge('GBR','DEU', capacity = 38600)

"""
ORIGEN EN ESPAÑA(ESP)
"""
G.add_edge('ESP','FRA', capacity = 40500)
G.add_edge('ESP','GBR', capacity = 37700)

"""
DESTINO A ESPAÑA(ESP)
"""
G.add_edge('FRA','ESP', capacity = 37700)
G.add_edge('GBR','ESP', capacity = 12900)

"""
ORIGEN EN FRANCIA(FRA)
"""
G.add_edge('FRA','GBR', capacity = 36000)

"""
DESTINO A FRANCIA(FRA)
"""
G.add_edge('GBR','FRA', capacity = 24800)








nx.draw(G)
plt.show()
