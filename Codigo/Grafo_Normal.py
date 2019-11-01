import matplotlib.pyplot as plt
import networkx as nx

countries = ['AUS', 'BRA', 'CAN', 'CHN', 'DEU', 'ESP', 'FRA', 'GBR', 'HKG', 'ITA', 'JPN', 'KOR', 'MEX', 'MYS', 'NLD', 'SGP', 'USA']

G= nx.Graph()
for pais in countries:
    G.add_node(pais)

"""
ARISTAS DEL GRAFO SUBYACENTE
"""
G.add_edge('CHN','AUS')
G.add_edge('CHN','BRA')
G.add_edge('CHN','CAN')
G.add_edge('CHN','DEU')
G.add_edge('CHN','ESP')
G.add_edge('CHN','FRA')
G.add_edge('CHN','GBR')
G.add_edge('CHN','HKG')
G.add_edge('CHN','ITA')
G.add_edge('CHN','JPN')
G.add_edge('CHN','KOR')
G.add_edge('CHN','MEX')
G.add_edge('CHN','MYS')
G.add_edge('CHN','NLD')
G.add_edge('CHN','SGP')

G.add_edge('AUS','USA')
G.add_edge('BRA','USA')
G.add_edge('CAN','USA')
G.add_edge('DEU','USA')
G.add_edge('ESP','USA')
G.add_edge('FRA','USA')
G.add_edge('GBR','USA')
G.add_edge('HKG','USA')
G.add_edge('ITA','USA')
G.add_edge('JPN','USA')
G.add_edge('KOR','USA')
G.add_edge('MEX','USA')
G.add_edge('MYS','USA')
G.add_edge('NLD','USA')
G.add_edge('SGP','USA')

G.add_edge('AUS','BRA')
G.add_edge('AUS','CAN')
G.add_edge('AUS','DEU')
G.add_edge('AUS','ESP')
G.add_edge('AUS','FRA')
G.add_edge('AUS','GBR')
G.add_edge('AUS','HKG')
G.add_edge('AUS','ITA')
G.add_edge('AUS','JPN')
G.add_edge('AUS','KOR')
G.add_edge('AUS','MEX')
G.add_edge('AUS','MYS')
G.add_edge('AUS','NLD')
G.add_edge('AUS','SGP')

G.add_edge('BRA','CAN')
G.add_edge('BRA','DEU')
G.add_edge('BRA','ESP')
G.add_edge('BRA','FRA')
G.add_edge('BRA','GBR')
G.add_edge('BRA','HKG')
G.add_edge('BRA','ITA')
G.add_edge('BRA','JPN')
G.add_edge('BRA','KOR')
G.add_edge('BRA','MEX')
G.add_edge('BRA','MYS')
G.add_edge('BRA','NLD')
G.add_edge('BRA','SGP')

G.add_edge('CAN','DEU')
G.add_edge('CAN','ESP')
G.add_edge('CAN','FRA')
G.add_edge('CAN','GBR')
G.add_edge('CAN','HKG')
G.add_edge('CAN','ITA')
G.add_edge('CAN','JPN')
G.add_edge('CAN','KOR')
G.add_edge('CAN','MEX')
G.add_edge('CAN','MYS')
G.add_edge('CAN','NLD')
G.add_edge('CAN','SGP')

G.add_edge('DEU','ESP')
G.add_edge('DEU','FRA')
G.add_edge('DEU','GBR')
G.add_edge('DEU','HKG')
G.add_edge('DEU','ITA')
G.add_edge('DEU','JPN')
G.add_edge('DEU','KOR')
G.add_edge('DEU','MEX')
G.add_edge('DEU','MYS')
G.add_edge('DEU','NLD')
G.add_edge('DEU','SGP')

G.add_edge('ESP','FRA')
G.add_edge('ESP','GBR')
G.add_edge('ESP','HKG')
G.add_edge('ESP','ITA')
G.add_edge('ESP','JPN')
G.add_edge('ESP','KOR')
G.add_edge('ESP','MEX')
G.add_edge('ESP','MYS')
G.add_edge('ESP','NLD')
G.add_edge('ESP','SGP')

G.add_edge('FRA','GBR')
G.add_edge('FRA','HKG')
G.add_edge('FRA','ITA')
G.add_edge('FRA','JPN')
G.add_edge('FRA','KOR')
G.add_edge('FRA','MEX')
G.add_edge('FRA','MYS')
G.add_edge('FRA','NLD')
G.add_edge('FRA','SGP')

G.add_edge('GBR','HKG')
G.add_edge('GBR','ITA')
G.add_edge('GBR','JPN')
G.add_edge('GBR','KOR')
G.add_edge('GBR','MEX')
G.add_edge('GBR','MYS')
G.add_edge('GBR','NLD')
G.add_edge('GBR','SGP')

G.add_edge('HKG','ITA')
G.add_edge('HKG','JPN')
G.add_edge('HKG','KOR')
G.add_edge('HKG','MEX')
G.add_edge('HKG','MYS')
G.add_edge('HKG','NLD')
G.add_edge('HKG','SGP')

G.add_edge('ITA','JPN')
G.add_edge('ITA','KOR')
G.add_edge('ITA','MEX')
G.add_edge('ITA','MYS')
G.add_edge('ITA','NLD')
G.add_edge('ITA','SGP')

G.add_edge('JPN','KOR')
G.add_edge('JPN','MEX')
G.add_edge('JPN','MYS')
G.add_edge('JPN','NLD')
G.add_edge('JPN','SGP')

G.add_edge('KOR','MEX')
G.add_edge('KOR','MYS')
G.add_edge('KOR','NLD')
G.add_edge('KOR','SGP')

G.add_edge('MEX','MYS')
G.add_edge('MEX','NLD')
G.add_edge('MEX','SGP')

G.add_edge('MYS','NLD')
G.add_edge('MYS','SGP')

G.add_edge('NLD','SGP')

"""
COMANDOS DE ALGORITMOS
"""
print(nx.diameter(G))
print(nx.radius(G))
print(nx.center(G))



"""
COMANDO DIBUJO
"""
nx.draw(G, with_labels=True, node_size=500, font_size=10)
plt.show()
