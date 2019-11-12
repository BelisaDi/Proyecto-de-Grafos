import matplotlib.pyplot as plt
import networkx as nx

countries = ['AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'ESP', 'FRA', 'GBR', 'HKG', 'ITA', 'JPN', 'KOR', 'MEX', 'MYS', 'NLD', 'SGP', 'USA']

G= nx.DiGraph()
for pais in countries:
    G.add_node(pais)

"""
ARISTAS DE RED RESIDUAL DE FLUJO MÁXIMO
"""
G.add_edge('AUS', 'USA')
G.add_edge('AUS', 'CAN')
G.add_edge('AUS', 'MEX')

G.add_edge('BRA', 'USA')
G.add_edge('BRA', 'CAN')
G.add_edge('BRA', 'MEX')

G.add_edge('CAN', 'USA')

G.add_edge('CHN', 'AUS')
G.add_edge('CHN', 'BRA')
G.add_edge('CHN', 'CAN')
G.add_edge('CHN', 'DEU')
G.add_edge('CHN', 'ESP')
G.add_edge('CHN', 'FRA')
G.add_edge('CHN', 'GBR')
G.add_edge('CHN', 'HKG')
G.add_edge('CHN', 'ITA')
G.add_edge('CHN', 'JPN')
G.add_edge('CHN', 'KOR')
G.add_edge('CHN', 'MEX')
G.add_edge('CHN', 'MYS')
G.add_edge('CHN', 'NLD')
G.add_edge('CHN', 'SGP')

G.add_edge('DEU', 'USA')
G.add_edge('DEU', 'CAN')
G.add_edge('DEU', 'MEX')

G.add_edge('ESP', 'USA')
G.add_edge('ESP', 'CAN')
G.add_edge('ESP', 'DEU')
G.add_edge('ESP', 'MEX')

G.add_edge('FRA', 'USA')
G.add_edge('FRA', 'BRA')
G.add_edge('FRA', 'CAN')
G.add_edge('FRA', 'ITA')
G.add_edge('FRA', 'MEX')

G.add_edge('GBR', 'USA')
G.add_edge('GBR', 'BRA')
G.add_edge('GBR', 'CAN')
G.add_edge('GBR', 'ITA')
G.add_edge('GBR', 'MEX')

G.add_edge('HKG', 'USA')
G.add_edge('HKG', 'CAN')
G.add_edge('HKG', 'DEU')
G.add_edge('HKG', 'ITA')
G.add_edge('HKG', 'KOR')
G.add_edge('HKG', 'MEX')

G.add_edge('ITA', 'USA')
G.add_edge('ITA', 'CAN')
G.add_edge('ITA', 'MEX')

G.add_edge('JPN', 'USA')
G.add_edge('JPN', 'CAN')
G.add_edge('JPN', 'DEU')
G.add_edge('JPN', 'MEX')

G.add_edge('KOR', 'USA')
G.add_edge('KOR', 'CAN')
G.add_edge('KOR', 'DEU')
G.add_edge('KOR', 'ITA')
G.add_edge('KOR', 'MEX')

G.add_edge('MEX', 'USA')
G.add_edge('MEX', 'CAN')

G.add_edge('MYS', 'USA')
G.add_edge('MYS', 'CAN')
G.add_edge('MYS', 'MEX')

G.add_edge('NLD', 'USA')
G.add_edge('NLD', 'CAN')
G.add_edge('NLD', 'DEU')
G.add_edge('NLD', 'ITA')
G.add_edge('NLD', 'MEX')

G.add_edge('SGP', 'USA')
G.add_edge('SGP', 'CAN')
G.add_edge('SGP', 'MEX')


"""
COMANDO DIBUJO
"""
nx.draw(G, with_labels=True, node_size=500, font_size=10)
plt.show()
