import networkx as nx

# Q1
def json_vers_nx(chemin):
    """Convertit le jeu de données (au format json) représentant les collaborations en un graphe Networkx exploitable.

    Args:
        chemin (str): Le chemin du fichier json.

    Returns:
        nx.Graph: Le graphe Networkx représentant les collaborations.
    """
    return res

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
    return res

# Q3
def collaborateurs_proches(G, u, k):
    """Retourne la liste des acteurs qui se trouvent à une distance au plus k de l'acteur donné.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: L'acteur en question.
        k (int): La distance maximale.

    Returns:
        list: La liste des acteurs à distance au plus k de l'acteur donné.
    """
    return res

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
    return res

def distance_naive(G, u, v):
    """Calcule la distance la plus courte entre deux acteurs dans le graphe de manière naïve.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: Le premier acteur.
        v: Le deuxième acteur.

    Returns:
        int: La distance entre les deux acteurs.
    """
    return res

def distance(G, u, v):
    """Calcule la distance la plus courte entre deux acteurs dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: Le premier acteur.
        v: Le deuxième acteur.

    Returns:
        int: La distance entre les deux acteurs.
    """
    return res

# Q4
def centralite(G, u):
    """Calcule la centralité d'un acteur dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.
        u: L'acteur dont on veut calculer la centralité.

    Returns:
        int: La centralité de l'acteur.
    """
    return res

def centre_hollywood(G):
    """Détermine l'acteur le plus central dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.

    Returns:
        str: L'acteur le plus central.
    """
    return res

# Q5
def eloignement_max(G: nx.Graph):
    """Détermine la distance maximale entre toutes les paires d'acteurs dans le graphe.

    Args:
        G (nx.Graph): Le graphe Networkx représentant les collaborations.

    Returns:
        int: La distance maximale entre toutes les paires d'acteurs.
    """
    return res
