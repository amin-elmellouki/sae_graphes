import networkx as nx
import requetes

G = nx.Graph()
G.add_edge("Acteur A", "Acteur B")
G.add_edge("Acteur A", "Acteur C")
G.add_edge("Acteur B", "Acteur C")
G.add_edge("Acteur B", "Acteur D")
G.add_edge("Acteur C", "Acteur D")
G.add_edge("Acteur D", "Acteur E")
G.add_node("Acteur F")
G.add_node("Acteur G")
G.add_node("Acteur H")

# Test de la fonction collaborateurs_communs
def test_collaborateurs_communs():
    assert requetes.collaborateurs_communs(G, "Acteur A", "Acteur B") == {"Acteur C"}
    assert requetes.collaborateurs_communs(G, "Acteur A", "Acteur E") == set()
    assert requetes.collaborateurs_communs(G, "Acteur A", "Acteur F") == set()
    assert requetes.collaborateurs_communs(G, "Acteur G", "Acteur H") == set()

# Test de la fonction collaborateurs_proches
def test_collaborateurs_proches():
    assert requetes.collaborateurs_proches(G, "Acteur A", 1) == {"Acteur A", "Acteur B", "Acteur C"}
    assert requetes.collaborateurs_proches(G, "Acteur B", 2) == {"Acteur A", "Acteur C", "Acteur D", "Acteur B", "Acteur E"}
    assert requetes.collaborateurs_proches(G, "Acteur E", 1) == {"Acteur E", "Acteur D"}
    assert requetes.collaborateurs_proches(G, "Acteur F", 2) == {"Acteur F"}

# Test de la fonction est_proche
def test_est_proche():
    assert requetes.est_proche(G, "Acteur A", "Acteur B", 1) == True
    assert requetes.est_proche(G, "Acteur A", "Acteur D", 2) == True
    assert requetes.est_proche(G, "Acteur A", "Acteur E", 1) == False
    assert requetes.est_proche(G, "Acteur A", "Acteur E", 2) == False
    assert requetes.est_proche(G, "Acteur G", "Acteur H", 1) == False

# Test de la fonction distance
def test_distance():
    assert requetes.distance(G, "Acteur A", "Acteur B") == 1
    assert requetes.distance(G, "Acteur A", "Acteur E") == 3
    assert requetes.distance(G, "Acteur G", "Acteur H") == -1

# Test de la fonction centralite
def test_centralite():
    assert requetes.centralite(G, "Acteur A") == 2
    assert requetes.centralite(G, "Acteur E") == 1
    assert requetes.centralite(G, "Acteur Z") == None  

# Test de la fonction centre_hollywood
def test_centre_hollywood():
    assert requetes.centre_hollywood(G) == "Acteur B" or "Acteur D"

# Test de la fonction eloignement_max
def test_eloignement_max():
    assert requetes.eloignement_max(G) == 3
    G.add_edge("Acteur F", "Acteur G")
    G.add_edge("Acteur G", "Acteur H")
    assert requetes.eloignement_max(G) == 3
    G.add_node("Acteur I")
    assert requetes.eloignement_max(G) == 3 