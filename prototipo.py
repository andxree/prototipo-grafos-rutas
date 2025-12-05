import networkx as nx
import matplotlib.pyplot as plt


#   PROTOTIPO OFICIAL - OPTIMIZACIÓN DE RUTAS CON GRAFOS
#   ÁREA: Alrededores de la Universidad Científica del Sur


# 1. CREACIÓN DEL GRAFO (Zona Aramburú)
G = nx.Graph()

G.add_weighted_edges_from([
    ("Av Aramburú", "Los Halcones", 2),
    ("Los Halcones", "Ricardo Angulo", 3),
    ("Ricardo Angulo", "Av Guardia Civil", 2),
    ("Av Guardia Civil", "Calle 50", 3),
    ("Av Aramburú", "Calle 3 Sur", 4),
    ("Calle 3 Sur", "Av Guardia Civil", 2),
    ("Av Aramburú", "Las Codornices", 5),
    ("Las Codornices", "Parque Llimatambo", 2),
    ("Parque Llimatambo", "Av Recavarren", 3),
    ("Av Recavarren", "Av Domingo Orué", 4),
])

# 2. OBJETIVO 1: ANÁLISIS BÁSICO DEL GRAFO

print("\n===== OBJETIVO 1: ANÁLISIS DEL GRAFO =====")
print("Número de nodos:", len(G.nodes))
print("Número de conexiones (aristas):", len(G.edges))
print("Nodos:", list(G.nodes))
print("Conexiones:", list(G.edges))
print("-" * 50)


# 3. OBJETIVO 2: DIVISIÓN EN ZONAS

print("\n===== OBJETIVO 2: DIVISIÓN EN ZONAS =====")

zona1 = G.subgraph(["Av Aramburú", "Los Halcones", "Ricardo Angulo"])
zona2 = G.subgraph(["Av Guardia Civil", "Calle 50", "Calle 3 Sur"])

print("Zona 1 nodos:", list(zona1.nodes))
print("Zona 2 nodos:", list(zona2.nodes))
print("-" * 50)


# 4. OBJETIVO 3: CAMBIOS DE TRÁFICO (Modificar pesos)
print("\n===== OBJETIVO 3: SIMULACIÓN DE TRÁFICO =====")

def aplicar_trafico(calle, multiplicador):
    """Aumenta o reduce el peso de una calle por efectos del tráfico."""
    u, v = calle
    G[u][v]["weight"] *= multiplicador
    print(f"Nuevo peso de {u} ↔ {v}: {G[u][v]['weight']}")

# Ejemplo: aumentar tráfico en Av Aramburú ↔ Calle 3 Sur (50% más)
aplicar_trafico(("Av Aramburú", "Calle 3 Sur"), 1.5)

print("-" * 50)


# 5. OBJETIVO 4: CLASIFICACIÓN DE VÍAS
print("\n===== OBJETIVO 4: CLASIFICACIÓN DE VÍAS =====")

tipo_via = {
    "Av Aramburú": "avenida",
    "Av Guardia Civil": "avenida",
    "Ricardo Angulo": "arterial",
    "Calle 3 Sur": "local",
}

print("Clasificación de vías:", tipo_via)
print("-" * 50)


# 6. VISUALIZACIÓN DEL GRAFO (Mapa Simplificado)

plt.figure(figsize=(11, 8))
pos = nx.spring_layout(G, seed=42)

nx.draw_networkx_nodes(G, pos, node_size=1200, node_color="lightblue")
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=9)

labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Grafo Simplificado - Alrededores de la Universidad Científica del Sur")
plt.axis("off")
plt.show()


# 7. CÁLCULO DE RUTA MÁS CORTA

print("\n===== CÁLCULO DE RUTA =====")
print("Nodos disponibles:", list(G.nodes))

origen = input("Origen: ")
destino = input("Destino: ")

if origen in G.nodes and destino in G.nodes:
    ruta = nx.shortest_path(G, origen, destino, weight="weight")
    costo = nx.shortest_path_length(G, origen, destino, weight="weight")

    print("\nRuta óptima:", " → ".join(ruta))
    print("Costo total:", costo)
else:
    print("Error: nodo no encontrado.")
