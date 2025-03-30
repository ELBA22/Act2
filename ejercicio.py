import pandas as pd 
import networkx as nx 

#Definimos la base de conocimientos en un DataFrame.

datos = {
    'Desde' : ['A', 'A', 'B', 'C', 'D', 'E'],
    'Hasta' : ['B', 'C', 'D', 'E', 'F', 'F'],
    'Costo' : [5, 3, 8, 7, 6, 2]
}

df = pd.DataFrame(datos)

#Creamos el grafo con NetWorkX
G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row['Desde'], row['Hasta'], weight=row['Costo'])
    
    def bestRoute(desde, hasta): 
        try:
            ruta = nx.shortest_path(G, source=desde, target=hasta, weight='weight')
            costo = nx.shortest_path_length(G, source=desde, target=hasta, weight='weight')
            return ruta, costo
        except nx.NetworkXNoPath:
            return None, float('inf')
        
            #USO
inicio = 'A'
fin = 'F'
ruta_optima, costo_optimo = bestRoute(inicio, fin)
if ruta_optima:
    print(f"La ruta optima desde {inicio} hasta {fin} es: {ruta_optima}")
    print(f"El costo total es: {costo_optimo}")
    
else:
    print(f"No hay ruta disponible desde {inicio} hasta {fin}")