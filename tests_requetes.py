import networkx as nx
import requetes

G = nx.Graph()
G.add_edge("Acteur A", "Acteur B")
G.add_edge("Acteur A", "Acteur C")
G.add_edge("Acteur B", "Acteur C")
G.add_edge("Acteur B", "Acteur D")
G.add_edge("Acteur C", "Acteur D")
G.add_edge("Acteur D", "Acteur E")

def test_collaborateurs_communs():

    assert requetes.collaborateurs_communs(G, "Acteur A", "Acteur B") == {"Acteur C"}

    assert requetes.collaborateurs_communs(G, "Acteur A", "Acteur E") == set()

    G.add_node("Acteur F")
    assert requetes.collaborateurs_communs(G, "Acteur A", "Acteur F") == set()

    G.add_nodes_from(["Acteur G", "Acteur H"])
    assert requetes.collaborateurs_communs(G, "Acteur G", "Acteur H") == set()