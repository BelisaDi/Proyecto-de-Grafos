import matplotlib.pyplot as plt
import networkx as nx

countries = ['AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'ESP', 'FRA', 'GBR', 'HKG', 'ITA', 'JPN', 'KOR', 'MEX', 'MYS', 'NLD', 'SGP', 'USA']

G= nx.DiGraph()
for pais in countries:
    G.add_node(pais)

"""
ARISTAS DE RED RESIDUAL DE FLUJO MÁXIMO
"""
G.add_edge('AUS', 'CHN')

G.add_edge('BRA', 'CHN')

G.add_edge('CAN', 'CHN')
G.add_edge('CAN', 'AUS')
G.add_edge('CAN', 'BRA')
G.add_edge('CAN', 'DEU')
G.add_edge('CAN', 'ESP')
G.add_edge('CAN', 'FRA')
G.add_edge('CAN', 'GBR')
G.add_edge('CAN', 'HKG')
G.add_edge('CAN', 'ITA')
G.add_edge('CAN', 'JPN')
G.add_edge('CAN', 'KOR')
G.add_edge('CAN', 'MYS')
G.add_edge('CAN', 'NLD')
G.add_edge('CAN', 'SGP')

G.add_edge('DEU', 'CHN')
G.add_edge('DEU', 'JPN')
G.add_edge('DEU', 'KOR')

G.add_edge('ESP', 'CHN')
G.add_edge('ESP', 'DEU')
G.add_edge('ESP', 'KOR')

G.add_edge('FRA', 'CHN')
G.add_edge('FRA', 'DEU')
G.add_edge('FRA', 'JPN')
G.add_edge('FRA', 'KOR')
G.add_edge('FRA', 'MYS')

G.add_edge('GBR', 'CHN')
G.add_edge('GBR', 'DEU')
G.add_edge('GBR', 'JPN')
G.add_edge('GBR', 'KOR')

G.add_edge('HKG', 'CHN')
G.add_edge('HKG', 'AUS')
G.add_edge('HKG', 'DEU')
G.add_edge('HKG', 'ITA')
G.add_edge('HKG', 'JPN')
G.add_edge('HKG', 'KOR')
G.add_edge('HKG', 'MYS')
G.add_edge('HKG', 'NLD')
G.add_edge('HKG', 'SGP')

G.add_edge('ITA', 'CHN')
G.add_edge('ITA', 'KOR')

G.add_edge('JPN', 'CHN')

G.add_edge('KOR', 'CHN')

G.add_edge('MEX', 'CHN')
G.add_edge('MEX', 'AUS')
G.add_edge('MEX', 'BRA')
G.add_edge('MEX', 'DEU')
G.add_edge('MEX', 'ESP')
G.add_edge('MEX', 'FRA')
G.add_edge('MEX', 'GBR')
G.add_edge('MEX', 'HKG')
G.add_edge('MEX', 'ITA')
G.add_edge('MEX', 'JPN')
G.add_edge('MEX', 'KOR')
G.add_edge('MEX', 'MYS')
G.add_edge('MEX', 'NLD')
G.add_edge('MEX', 'SGP')

G.add_edge('MYS', 'CHN')

G.add_edge('NLD', 'CHN')
G.add_edge('NLD', 'DEU')
G.add_edge('NLD', 'ITA')
G.add_edge('NLD', 'JPN')
G.add_edge('NLD', 'KOR')

G.add_edge('SGP', 'CHN')

G.add_edge('USA', 'AUS')
G.add_edge('USA', 'BRA')
G.add_edge('USA', 'CAN')
G.add_edge('USA', 'DEU')
G.add_edge('USA', 'ESP')
G.add_edge('USA', 'FRA')
G.add_edge('USA', 'GBR')
G.add_edge('USA', 'HKG')
G.add_edge('USA', 'ITA')
G.add_edge('USA', 'JPN')
G.add_edge('USA', 'KOR')
G.add_edge('USA', 'MEX')
G.add_edge('USA', 'MYS')
G.add_edge('USA', 'NLD')
G.add_edge('USA', 'SGP')


"""
COMANDO DIBUJO
"""
nx.draw(G, with_labels=True, node_size=500, font_size=10)
plt.show()
