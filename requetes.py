

import json
import networkx as nx
import matplotlib.pyplot as plt

# Q1
def json_vers_nx(chemin):
    """Convertit le jeu de données (au format json) représentant les collaborations en un graphe Networkx exploitable
    Args:
        chemin (str): Le chemin du fichier json.

    Returns:
        nx.Graph: Le graphe Networkx représentant les collaborations.
    """
    # Ouverture et chargement des données du fichier json
    fic = open(chemin, 'r')
    donnees = json.load(fic)
    fic.close()
    
    graphe = nx.Graph()

    # Création des données pour chaque acteur
    for film in donnees:
        acteurs = film.get("cast", [])
        for acteur in acteurs:
            # Enlever les balises de formatage wiki (par exemple [[...]])
            if "|" in acteur:
                nom_acteur = acteur.strip("[]").split("|")[-1]
            else:
                nom_acteur = acteur.strip("[]")
            graphe.add_node(nom_acteur)

    # Création des arêtes entre les collaborateurs
    for film in donnees:
        acteurs = film.get("cast", [])
        for i in range(len(acteurs)):
            for j in range(i + 1, len(acteurs)):
                if "|" in acteurs[i]:
                    acteur1 = acteurs[i].strip("[]").split("|")[-1]
                else:
                    acteur1 = acteurs[i].strip("[]")
                if "|" in acteurs[j]:
                    acteur2 = acteurs[j].strip("[]").split("|")[-1]
                else:
                    acteur2 = acteurs[j].strip("[]")
                if not graphe.has_edge(acteur1, acteur2):
                    graphe.add_edge(acteur1, acteur2)
    plt.cla()
    nx.draw(graphe, with_labels=True)
    plt.show()
    print(graphe)
    return graphe

json_vers_nx("./data.json")

# Q2
def collaborateurs_communs(G, u, v):
    """Retourne l'ensemble des acteurs qui ont collaboré avec les deux acteurs donnés.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: Le premier acteur.
        v: Le deuxième acteur.

    Returns:
        set: L'ensemble des acteurs en commun.
    """
    collab_u = set(G.neighbors(u))
    collab_v = set(G.neighbors(v))
    return collab_u.intersection(collab_v)

# Q3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs

def est_proche(G, u, v, k=1):
    """Vérifie si deux acteurs se trouvent à une distance au plus k l'un de l'autre dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: Le premier acteur.
        v: Le deuxième acteur.
        k (int, optional): La distance maximale. Par défaut, 1.

    Returns:
        bool: True si les acteurs se trouvent à une distance au plus k l'un de l'autre, False sinon.
    """
    return v in collaborateurs_proches(G, u, k)

def distance_naive(G, u, v):
    """Calcule la distance la plus courte entre deux acteurs dans le graphe de manière naïve.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: Le premier acteur.
        v: Le deuxième acteur.

    Returns:
        int: La distance entre les deux acteurs.
    """
    if u == v:
        return 0
    
    k = 1
    while True:
        proches = collaborateurs_proches(G, u, k)
        if proches is None:
            return float('inf')
        if v in proches:
            return k
        k += 1
    

def distance(G, u, v):
    """Calcule la distance la plus courte entre deux acteurs dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: Le premier acteur.
        v: Le deuxième acteur.

    Returns:
        int: La distance entre les deux acteurs.
    """
    if u == v:
        return 0
    
    distance = 0
    visite = set()
    visite.add(u)
    niveau_courant = {u}  
    
    while niveau_courant:
        niveau_suivant = set()  
        for acteur in niveau_courant:
            if acteur == v:
                return distance
            voisins = set(G.neighbors(acteur))
            visite.update(voisins)
            niveau_suivant.update(voisins - visite)
        niveau_courant = niveau_suivant
        distance += 1
    
    return float('inf')
# Q4
def centralite(G, u):
    """Calcule la centralité d'un acteur dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: L'acteur dont on veut calculer la centralité.

    Returns:
        int: La centralité de l'acteur.
    """
    pass

def centre_hollywood(G):
    """Détermine l'acteur le plus central dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.

    Returns:
        str: L'acteur le plus central.
    """
    pass

# Q5
def eloignement_max(G: nx.Graph):
    """Détermine la distance maximale entre toutes les paires d'acteurs dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.

    Returns:
        int: La distance maximale entre toutes les paires d'acteurs.
    """
    pass
