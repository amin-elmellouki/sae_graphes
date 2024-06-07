import networkx as nx
import matplotlib.pyplot as plt
import requetes

def oracle():
    chemin_fichier_json = "./data.json"
    G = requetes.json_vers_nx(chemin_fichier_json)
    
    print("Bienvenue dans l'Oracle des Collaborations!")
    print("Voici les différentes fonctionnalités disponibles : ")
    print("1. Afficher le graphe des collaborations")
    print("2. Trouver les collaborateurs communs entre deux acteurs")
    print("3. Vérifier si deux acteurs sont proches")
    print("4. Calculer la distance entre deux acteurs")
    print("5. Calculer la centralité d'un acteur")
    print("6. Trouver l'acteur le plus central dans le graphe")
    print("7. Calculer l'éloignement maximal entre toutes les paires d'acteurs")
    print("0. Quitter")

    while True:
        choix = input("Entrez le numéro de l'opération que vous souhaitez effectuer (0 pour quitter) : ")
        
        match choix:
            case "1":
                # Afficher le graphe des collaborations
                nx.draw(G, with_labels=True)
                plt.show()
                "\n"
            case "2":
                # Trouver les collaborateurs communs entre deux acteurs
                acteur1 = input("Entrez le nom du premier acteur : ")
                acteur2 = input("Entrez le nom du deuxième acteur : ")
                communs = requetes.collaborateurs_communs(G, acteur1, acteur2)
                if not communs:
                    print("Il n'y a pas de collaborateurs communs entre", acteur1, "et", acteur2, ".")
                else:
                    print("Les collaborateurs communs sont : ", communs)
                "\n"
            case "3":
                # Vérifier si deux acteurs sont proches
                acteur1 = input("Entrez le nom du premier acteur: ")
                acteur2 = input("Entrez le nom du deuxième acteur: ")
                k = int(input("Entrez la distance maximale souhaitée : "))
                if requetes.est_proche(G, acteur1, acteur2, k):
                    print(acteur1 + " et " + acteur2 + " sont proches dans le graphe.")
                else:
                    print(acteur1 + " et " + acteur2 + " ne sont pas proches dans le graphe.")
                "\n"
            case "4":
                # Calculer la distance entre deux acteurs
                acteur1 = input("Entrez le nom du premier acteur : ")
                acteur2 = input("Entrez le nom du deuxième acteur : ")
                distance = requetes.distance(G, acteur1, acteur2)
                if distance == -1:
                    print("Il n'existe aucun chemin entre " + acteur1 + " et " + acteur2)
                else:
                    print("La distance entre ", acteur1, "et", acteur2, "est : ", distance)
                "\n"
            case "5":
                # Calculer la centralité d'un acteur
                acteur = input("Entrez le nom de l'acteur : ")
                print("La centralité de ", acteur, "est : ", requetes.centralite(G, acteur)) 
                "\n"
            case "6":
                # Trouver l'acteur le plus central dans le graphe
                print("L'acteur le plus central dans le graphe est : ", requetes.centre_hollywood(G))
            case "7":
                # Calculer l'éloignement maximal entre toutes les paires d'acteurs
                print("L'éloignement maximal entre toutes les paires d'acteurs est : ", requetes.eloignement_max(G))
                "\n"
            case "0":
                # Quitter le programme
                print("Merci d'avoir utilisé l'Oracle de Bacon. Au revoir !")
                break
                "\n"
            case _:
                print("Choix invalide. Veuillez entrer un numéro valide.")

# Appel de fonction pour lancer l'application
oracle()