import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

countries = ['AUS','BRA','CAN','CHN','DEU','ESP','FRA','GBR','HKG','ITA','JPN','KOR','MEX','MYS','NLD','SGP','USA']
for pais in countries:
    if pais == 'CHN':
        G.add_node(pais, demand=-1259200)
    elif pais == 'USA':
        G.add_node(pais, demand=1259200)
    else:
        G.add_node(pais)

"""
ARISTAS DE EXPORTACIONES CHINENSES
"""
G.add_edge('CHN','AUS', capacity = 47100, weight = 4)
G.add_edge('CHN','BRA', capacity = 27100, weight = 10)
G.add_edge('CHN','CAN', capacity = 50100, weight = 6)
G.add_edge('CHN','DEU', capacity = 109200, weight = 4)
G.add_edge('CHN','ESP', capacity = 28600, weight = 5)
G.add_edge('CHN','FRA', capacity = 53000, weight = 5)
G.add_edge('CHN','GBR', capacity = 59000, weight = 5)
G.add_edge('CHN','HKG', capacity = 255900, weight = 1)
G.add_edge('CHN','ITA', capacity = 31900, weight = 5)
G.add_edge('CHN','JPN', capacity = 157100, weight = 2)
G.add_edge('CHN','KOR', capacity = 98200, weight = 1)
G.add_edge('CHN','MEX', capacity = 52100, weight = 7)
G.add_edge('CHN','MYS', capacity = 38100, weight = 2)
G.add_edge('CHN','NLD', capacity = 43900, weight = 4)
G.add_edge('CHN','SGP', capacity = 42700, weight = 2)
G.add_edge('CHN','USA', capacity = 476900, weight = 7)

"""
ARISTAS DE IMPORTACION ESTADOUNIDENSE
"""
G.add_edge('AUS','USA', capacity = 8600, weight = 9)
G.add_edge('BRA','USA', capacity = 25100, weight = 4)
G.add_edge('CAN','USA', capacity = 274900, weight = 2)
G.add_edge('DEU','USA', capacity = 112000, weight = 7)
G.add_edge('ESP','USA', capacity = 14200, weight = 5)
G.add_edge('FRA','USA', capacity = 36100, weight = 5)
G.add_edge('GBR','USA', capacity = 45300, weight = 5)
G.add_edge('HKG','USA', capacity = 4100, weight = 4)
G.add_edge('ITA','USA', capacity = 45000, weight = 7)
G.add_edge('JPN','USA', capacity = 125300, weight = 5)
G.add_edge('KOR','USA', capacity = 69400, weight = 6)
G.add_edge('MEX','USA', capacity = 307200, weight = 6)
G.add_edge('MYS','USA', capacity = 33100, weight = 1)
G.add_edge('NLD','USA', capacity = 16400, weight = 9)
G.add_edge('SGP','USA', capacity = 16700, weight = 4)


"""
ORIGEN EN AUSTRALIA(AUS)
"""
G.add_edge('AUS','BRA', capacity = 1400, weight=9)
G.add_edge('AUS','CAN', capacity = 1400, weight=8)
G.add_edge('AUS','DEU', capacity = 2500, weight=8)
G.add_edge('AUS','ESP', capacity = 700, weight=9)
G.add_edge('AUS','FRA', capacity = 1300, weight=9)
G.add_edge('AUS','GBR', capacity = 4800, weight=9)
G.add_edge('AUS','HKG', capacity = 14300, weight=3)
G.add_edge('AUS','ITA', capacity = 700, weight=8)
G.add_edge('AUS','JPN', capacity = 34700, weight=4)
G.add_edge('AUS','KOR', capacity = 18000, weight=4)
G.add_edge('AUS','MEX', capacity = 400, weight=8)
G.add_edge('AUS','MYS', capacity = 4700, weight=3)
G.add_edge('AUS','NLD', capacity = 1300, weight=9)
G.add_edge('AUS','SGP', capacity = 3900, weight=3)

"""
DESTINO A AUSTRALIA(AUS)
"""
G.add_edge('BRA','AUS', capacity = 600, weight=9)
G.add_edge('CAN','AUS', capacity = 1400, weight=8)
G.add_edge('DEU','AUS', capacity = 9300, weight=8)
G.add_edge('ESP','AUS', capacity = 1700, weight=9)
G.add_edge('FRA','AUS', capacity = 3100, weight=9)
G.add_edge('GBR','AUS', capacity = 5000, weight=9)
G.add_edge('HKG','AUS', capacity = 600, weight=3)
G.add_edge('ITA','AUS', capacity = 4200, weight=8)
G.add_edge('JPN','AUS', capacity = 16400, weight=4)
G.add_edge('KOR','AUS', capacity = 18700, weight=4)
G.add_edge('MEX','AUS', capacity = 1900, weight=8)
G.add_edge('MYS','AUS', capacity = 8000, weight=3)
G.add_edge('NLD','AUS', capacity = 1800, weight=9)
G.add_edge('SGP','AUS', capacity = 6500, weight=3)

"""
ORIGEN EN BRAZIL(BRA)
"""
G.add_edge('BRA','CAN', capacity = 2700, weight=5)
G.add_edge('BRA','DEU', capacity = 6200, weight=6)
G.add_edge('BRA','ESP', capacity = 4200, weight=5)
G.add_edge('BRA','FRA', capacity = 2800, weight=5)
G.add_edge('BRA','GBR', capacity = 3100, weight=5)
G.add_edge('BRA','HKG', capacity = 2700, weight=10)
G.add_edge('BRA','ITA', capacity = 3700, weight=5)
G.add_edge('BRA','JPN', capacity = 5800, weight=10)
G.add_edge('BRA','KOR', capacity = 3300, weight=10)
G.add_edge('BRA','MEX', capacity = 4900, weight=4)
G.add_edge('BRA','MYS', capacity = 2600, weight=10)
G.add_edge('BRA','NLD', capacity = 7600, weight=5)
G.add_edge('BRA','SGP', capacity = 1600, weight=10)

"""
DESTINO A BRAZIL(BRA)
"""
G.add_edge('CAN','BRA', capacity = 1400, weight=5)
G.add_edge('DEU','BRA', capacity = 9300, weight=6)
G.add_edge('ESP','BRA', capacity = 2900, weight=5)
G.add_edge('FRA','BRA', capacity = 3700, weight=5)
G.add_edge('GBR','BRA', capacity = 2400, weight=5)
G.add_edge('HKG','BRA', capacity = 900, weight=10)
G.add_edge('ITA','BRA', capacity = 4100, weight=5)
G.add_edge('JPN','BRA', capacity = 3500, weight=10)
G.add_edge('KOR','BRA', capacity = 5400, weight=10)
G.add_edge('MEX','BRA', capacity = 4000, weight=4)
G.add_edge('MYS','BRA', capacity = 1400, weight=10)
G.add_edge('NLD','BRA', capacity = 2000, weight=5)
G.add_edge('SGP','BRA', capacity = 900, weight=10)


"""
ORIGEN EN CANADA(CAN)
"""
G.add_edge('CAN','DEU', capacity = 3800, weight=4)
G.add_edge('CAN','ESP', capacity = 1800, weight=4)
G.add_edge('CAN','FRA', capacity = 3100, weight=4)
G.add_edge('CAN','GBR', capacity = 7500, weight=4)
G.add_edge('CAN','HKG', capacity = 1700, weight=6)
G.add_edge('CAN','ITA', capacity = 1700, weight=4)
G.add_edge('CAN','JPN', capacity = 9700, weight=5)
G.add_edge('CAN','KOR', capacity = 4700, weight=5)
G.add_edge('CAN','MEX', capacity = 8100, weight=2)
G.add_edge('CAN','MYS', capacity = 700, weight=7)
G.add_edge('CAN','NLD', capacity = 2200, weight=4)
G.add_edge('CAN','SGP', capacity = 1100, weight=8)

"""
DESTINO A CANADA(CAN)
"""
G.add_edge('DEU','CAN', capacity = 12400, weight=4)
G.add_edge('ESP','CAN', capacity = 1900, weight=4)
G.add_edge('FRA','CAN', capacity = 4200, weight=4)
G.add_edge('GBR','CAN', capacity = 6200, weight=4)
G.add_edge('HKG','CAN', capacity = 1000, weight=6)
G.add_edge('ITA','CAN', capacity = 5600, weight=4)
G.add_edge('JPN','CAN', capacity = 11700, weight=5)
G.add_edge('KOR','CAN', capacity = 6100, weight=5)
G.add_edge('MEX','CAN', capacity = 22000, weight=2)
G.add_edge('MYS','CAN', capacity = 1600, weight=7)
G.add_edge('NLD','CAN', capacity = 3100, weight=4)
G.add_edge('SGP','CAN', capacity = 800, weight=8)

"""
ORIGEN EN ALEMANIA(DEU)
"""
G.add_edge('DEU','ESP', capacity = 43600, weight=1)
G.add_edge('DEU','FRA', capacity = 104000, weight=1)
G.add_edge('DEU','GBR', capacity = 90300, weight=1)
G.add_edge('DEU','HKG', capacity = 7800, weight=5)
G.add_edge('DEU','ITA', capacity = 72300, weight=1)
G.add_edge('DEU','JPN', capacity = 22500, weight=5)
G.add_edge('DEU','KOR', capacity = 19700, weight=5)
G.add_edge('DEU','MEX', capacity = 14900, weight=6)
G.add_edge('DEU','MYS', capacity = 5800, weight=6)
G.add_edge('DEU','NLD', capacity = 84600, weight=1)
G.add_edge('DEU','SGP', capacity = 7800, weight=6)

"""
DESTINO A ALEMANIA(DEU)
"""
G.add_edge('ESP','DEU', capacity = 34000, weight=1)
G.add_edge('FRA','DEU', capacity = 69200, weight=1)
G.add_edge('GBR','DEU', capacity = 38600, weight=1)
G.add_edge('HKG','DEU', capacity = 1600, weight=5)
G.add_edge('ITA','DEU', capacity = 58600, weight=1)
G.add_edge('JPN','DEU', capacity = 24500, weight=5)
G.add_edge('KOR','DEU', capacity = 12000, weight=5)
G.add_edge('MEX','DEU', capacity = 8900, weight=6)
G.add_edge('MYS','DEU', capacity = 9300, weight=6)
G.add_edge('NLD','DEU', capacity = 90000, weight=1)
G.add_edge('SGP','DEU', capacity = 8700, weight=6)

"""
ORIGEN EN ESPAÑA(ESP)
"""
G.add_edge('ESP','FRA', capacity = 40500, weight=1)
G.add_edge('ESP','GBR', capacity = 20700, weight=1)
G.add_edge('ESP','HKG', capacity = 1200, weight=6)
G.add_edge('ESP','ITA', capacity = 22700, weight=1)
G.add_edge('ESP','JPN', capacity = 3300, weight=6)
G.add_edge('ESP','KOR', capacity = 2100, weight=6)
G.add_edge('ESP','MEX', capacity = 5100, weight=5)
G.add_edge('ESP','MYS', capacity = 800, weight=7)
G.add_edge('ESP','NLD', capacity = 9500, weight=1)
G.add_edge('ESP','SGP', capacity = 800, weight=6)

"""
DESTINO A ESPAÑA(ESP)
"""
G.add_edge('FRA','ESP', capacity = 37700, weight=1)
G.add_edge('GBR','ESP', capacity = 12900, weight=1)
G.add_edge('HKG','ESP', capacity = 300, weight=6)
G.add_edge('ITA','ESP', capacity = 23400, weight=1)
G.add_edge('JPN','ESP', capacity = 4300, weight=6)
G.add_edge('KOR','ESP', capacity = 3800, weight=6)
G.add_edge('MEX','ESP', capacity = 4600, weight=5)
G.add_edge('MYS','ESP', capacity = 900, weight=7)
G.add_edge('NLD','ESP', capacity = 14200, weight=1)
G.add_edge('SGP','ESP', capacity = 400, weight=6)

"""
ORIGEN EN FRANCIA(FRA)
"""
G.add_edge('FRA','GBR', capacity = 36000, weight=1)
G.add_edge('FRA','HKG', capacity = 6600, weight=6)
G.add_edge('FRA','ITA', capacity = 39700, weight=1)
G.add_edge('FRA','JPN', capacity = 9400, weight=6)
G.add_edge('FRA','KOR', capacity = 6400, weight=6)
G.add_edge('FRA','MEX', capacity = 4000, weight=5)
G.add_edge('FRA','MYS', capacity = 2600, weight=6)
G.add_edge('FRA','NLD', capacity = 18400, weight=1)
G.add_edge('FRA','SGP', capacity = 7600, weight=6)

"""
DESTINO A FRANCIA(FRA)
"""
G.add_edge('GBR','FRA', capacity = 24800, weight=1)
G.add_edge('HKG','FRA', capacity = 800, weight=6)
G.add_edge('ITA','FRA', capacity = 48100, weight=1)
G.add_edge('JPN','FRA', capacity = 10600, weight=6)
G.add_edge('KOR','FRA', capacity = 3800, weight=6)
G.add_edge('MEX','FRA', capacity = 3100, weight=5)
G.add_edge('MYS','FRA', capacity = 2400, weight=6)
G.add_edge('NLD','FRA', capacity = 29800, weight=1)
G.add_edge('SGP','FRA', capacity = 2900, weight=6)

"""
ORIGEN EN REINO UNIDO(GBR)
"""
G.add_edge('GBR','HKG', capacity = 8400, weight=6)
G.add_edge('GBR','ITA', capacity = 12600, weight=1)
G.add_edge('GBR','JPN', capacity = 7100, weight=5)
G.add_edge('GBR','KOR', capacity = 6600, weight=5)
G.add_edge('GBR','MEX', capacity = 2100, weight=5)
G.add_edge('GBR','MYS', capacity = 1800, weight=6)
G.add_edge('GBR','NLD', capacity = 24900, weight=1)
G.add_edge('GBR','SGP', capacity = 4100, weight=6)

"""
DESTINO A REINO UNIDO(GBR)
"""
G.add_edge('HKG','GBR', capacity = 8800, weight=6)
G.add_edge('ITA','GBR', capacity = 24900, weight=1)
G.add_edge('JPN','GBR', capacity = 14600, weight=5)
G.add_edge('KOR','GBR', capacity = 9300, weight=5)
G.add_edge('MEX','GBR', capacity = 3300, weight=5)
G.add_edge('MYS','GBR', capacity = 2400, weight=6)
G.add_edge('NLD','GBR', capacity = 47000, weight=1)
G.add_edge('SGP','GBR', capacity = 2600, weight=6)

"""
ORIGEN EN HONG KONG (HKG)
"""

G.add_edge('HKG','ITA', capacity = 400, weight=5)
G.add_edge('HKG','JPN', capacity = 1500, weight=2)
G.add_edge('HKG','KOR', capacity = 2100, weight=1)
G.add_edge('HKG','MEX', capacity = 300, weight=8)
G.add_edge('HKG','MYS', capacity = 3300, weight=2)
G.add_edge('HKG','NLD', capacity = 6200, weight=5)
G.add_edge('HKG','SGP', capacity = 3700, weight=2)

"""
DESTINO EN HONG KONG (HKG)
"""

G.add_edge('ITA','HKG', capacity = 6400, weight=5)
G.add_edge('JPN','HKG', capacity = 32200, weight=2)
G.add_edge('KOR','HKG', capacity = 34900, weight=1)
G.add_edge('MEX','HKG', capacity = 900, weight=8)
G.add_edge('MYS','HKG', capacity = 13700, weight=2)
G.add_edge('NLD','HKG', capacity = 2700, weight=5)
G.add_edge('SGP','HKG', capacity = 60900, weight=2)

"""
ORIGEN EN ITALIA (ITA)
"""

G.add_edge('ITA','JPN', capacity = 8400, weight=6)
G.add_edge('ITA','KOR', capacity = 5500, weight=5)
G.add_edge('ITA','MEX', capacity = 5500, weight=6)
G.add_edge('ITA','MYS', capacity = 1600, weight=6)
G.add_edge('ITA','NLD', capacity = 11600, weight=1)
G.add_edge('ITA','SGP', capacity = 3100, weight=6)

"""
DESTINO EN ITALIA (ITA)
"""

G.add_edge('JPN','ITA', capacity = 4800, weight=6)
G.add_edge('KOR','ITA', capacity = 3900, weight=5)
G.add_edge('MEX','ITA', capacity = 1200, weight=6)
G.add_edge('MYS','ITA', capacity = 1200, weight=6)
G.add_edge('NLD','ITA', capacity = 24800, weight=1)
G.add_edge('SGP','ITA', capacity = 500, weight=6)

"""
ORIGEN EN JAPÓN (JPN)
"""

G.add_edge('JPN','KOR', capacity = 54200, weight=1)
G.add_edge('JPN','MEX', capacity = 14900, weight=6)
G.add_edge('JPN','MYS', capacity = 13400, weight=3)
G.add_edge('JPN','NLD', capacity = 9700, weight=5)
G.add_edge('JPN','SGP', capacity = 17600, weight=3)

"""
DESTINO EN JAPÓN (JPN)
"""

G.add_edge('KOR','JPN', capacity = 26900, weight=1)
G.add_edge('MEX','JPN', capacity = 5600, weight=6)
G.add_edge('MYS','JPN', capacity = 17800, weight=3)
G.add_edge('NLD','JPN', capacity = 3000, weight=5)
G.add_edge('SGP','JPN', capacity = 12200, weight=3)

"""
ORIGEN EN COREA DEL SUR (KOR)
"""

G.add_edge('KOR','MEX', capacity = 11000, weight=7)
G.add_edge('KOR','MYS', capacity = 8200, weight=3)
G.add_edge('KOR','NLD', capacity = 4300, weight=5)
G.add_edge('KOR','SGP', capacity = 18300, weight=3)

"""
DESTINO EN COREA DEL SUR (KOR)
"""

G.add_edge('MEX','KOR', capacity = 4200, weight=7)
G.add_edge('MYS','KOR', capacity = 8000, weight=3)
G.add_edge('NLD','KOR', capacity = 6400, weight=5)
G.add_edge('SGP','KOR', capacity = 14300, weight=3)

"""
ORIGEN EN MÉXICO (MEX)
"""

G.add_edge('MEX','MYS', capacity = 900, weight=9)
G.add_edge('MEX','NLD', capacity = 2100, weight=5)
G.add_edge('MEX','SGP', capacity = 1400, weight=9)

"""
DESTINO EN MÉXICO (MEX)
"""

G.add_edge('MYS','MEX', capacity = 3300, weight=9)
G.add_edge('NLD','MEX', capacity = 2400, weight=5)
G.add_edge('SGP','MEX', capacity = 1300, weight=9)

"""
ORIGEN EN MALASIA (MYS)
"""

G.add_edge('MYS','NLD', capacity = 7500, weight=6)
G.add_edge('MYS','SGP', capacity = 35800, weight=1)

"""
DESTINO EN MALASIA (MYS)
"""

G.add_edge('NLD','MYS', capacity = 1800, weight=6)
G.add_edge('SGP','MYS', capacity = 28500, weight=1)

"""
ORIGEN EN PAISES BAJOS (NLD)
"""

G.add_edge('NLD','SGP', capacity = 5200, weight=6)

"""
DESTINO EN PAISES BAJOS (NLD)
"""

G.add_edge('SGP','NLD', capacity = 5600, weight=6)

"""
COMPROBACIÓN DE ALGORITMOS
"""

max_flujo, flujo = nx.maximum_flow(G, 'CHN', 'USA')
print(max_flujo)
#print(flujo)

min_flow = nx.min_cost_flow(G)
min_flow_value = nx.cost_of_flow(G, min_flow)
#print(min_flow)
print(min_flow_value)

nx.draw(G, with_labels = True, nodelist =['AUS','BRA','CAN','CHN','DEU','ESP','FRA','GBR','HKG','ITA','JPN','KOR','MEX','MYS','NLD','SGP','USA'], node_color = ['#1F78B4', '#1F78B4', '#1F78B4', '#DB1B11', '#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#1F78B4','#24DB11'], node_size = 500, font_size = 10, pos = nx.shell_layout(G,[['AUS','BRA','CAN','DEU','ESP','FRA','GBR','HKG','ITA','JPN','KOR','MEX','MYS','NLD','SGP'],['USA','CHN']]))
plt.show()
