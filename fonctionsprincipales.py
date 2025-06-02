import numpy as np

def ajouter(livres):
    print("Ajouter un livre à la bibliothèque")
    while True:
        ISBN = input("Veuillez saisir l'ISBN (ex: 978-3-16-148410-0) : ")
        if ISBN in livres:
            print("Ce livre existe déjà. Veuillez saisir un autre ISBN.")
        else:
            break
    t = input("Titre du livre : ")
    a = input("Auteur du livre : ")
    g = input("Genre de l'oeuvre : ")
    livres[ISBN] = {"titre": t, "auteur": a, "genre": g, "statut": "Disponible"}
    print("Livre ajouté avec succès.")

def supprimer(livres):
    print("Supprimer un livre de la bibliothèque")
    ISBN = input("Veuillez saisir l'ISBN du livre : ")
    if ISBN in livres:
        del livres[ISBN]
        print("Livre supprimé.")
    else:
        print("Ce livre n'existe pas.")

def rechercher(livres):
    print("Rechercher des livres dans la bibliothèque")
    cle = input("Saisissez le titre ou l'auteur du livre que vous cherchez : ").lower()
    resultats = []

    for ISBN, l in livres.items():
        titre = l['titre'].lower()
        auteur = l['auteur'].lower()
        if cle in titre or cle in auteur:
            resultats.append((ISBN, l))

    if resultats:
        for ISBN, l in resultats:
            print("ISBN :", ISBN)
            for key, value in l.items():
                print(key + " :", str(value))
            print("-----------------------------------")
    else:
        print("Aucun livre de ce titre ou de cet auteur n'a été trouvé :(")

def lister(livres):
    print("Lister les livres de la bibliothèque")
    choix = input("Voulez-vous filtrer par statut ? F pour filtrer / T pour tout afficher (F/T) : ").strip().upper()
    if choix == "T":
        for isbn, livre in livres.items():
            print("ISBN :", isbn)
            for key, value in livre.items():
                print(key + " :", str(value))
            print("-----------------------------------")
    elif choix == "F":
        filtre = input("Voulez-vous les livres disponibles (D) ou empruntés (E) ? (D/E) : ").strip().upper()
        if filtre not in ("D", "E"):
            print("Erreur : Choix invalide. Veuillez entrer D ou E.")
            return
        statut_recherche = "disponible" if filtre == "D" else "emprunté"
        trouve = False
        for ISBN, l in livres.items():
            if l.get("statut", "").lower() == statut_recherche:
                print("ISBN :", ISBN)
                for key, value in l.items():
                    print(key + " :", str(value))
                print("-----------------------------------")
                trouve = True
        if not trouve:
            print("Aucun livre trouvé avec le statut :", statut_recherche)
    else:
        print("Erreur : Veuillez entrer F pour filtrer ou T pour tout afficher.")

def emprunter(livres):
    print("Service d'emprunt")
    ISBN = input("Saisissez l'ISBN du livre à emprunter : ")
    if ISBN in livres:
        if livres[ISBN]["statut"] == "Disponible":
            livres[ISBN]["statut"] = "Emprunté"
            print("Livre emprunté avec succès !")
        else:
            print("Ce livre est déjà emprunté.")
    else:
        print("Ce livre est inexistant.")

def retourner(livres):
    print("Service de retour")
    ISBN = input("Saisissez l'ISBN du livre à retourner : ")
    if ISBN in livres:
        if livres[ISBN]["statut"] == "Emprunté":
            livres[ISBN]["statut"] = "Disponible"
            print("Livre retourné avec succès !")
        else:
            print("Ce livre est déjà disponible.")
    else:
        print("Ce livre est inexistant.")

def afficher(livres):
    print("Les statistiques : Le nombre de livres disponibles, d'empruntés et du total")
    td = []
    te = []
    for l in livres.values():
        if l["statut"] == "Disponible":
            td.append(1)
        else:
            te.append(1)
    d = sum(td) 
    e = sum(te)
    t = d + e
    stats = np.array([t, d, e])
    print("Total : "+str(stats[0])+", Disponibles : "+str(stats[1])+", Empruntés : "+str(stats[2]))

def sauvegarder(livres):
    print("Sauvegarde des données dans bibliotheque.txt")
    try:
        file=open("bibliotheque.txt","w", encoding='utf-8')
        for ISBN, l in livres.items():
            donneel = ISBN+","+l['titre']+","+l['auteur']+","+ l['genre']+","+l['statut']+"\n"
            file.write(donneel)
        print("Données sauvegardées avec succés")
    except Exception as e:
        print("Erreur lors du sauvegarde:"+e)

def charger(livres):
    print("Chargement des données depuis bibliotheque.txt")
    try:
        with open("bibliotheque.txt", "r") as f:
            for ligne in f:
                ISBN, t, a, g, s = ligne.strip().split(",", 4)
                livres[ISBN] = {"titre": t, "auteur": a, "genre": g, "statut": s}
        print("Données chargées avec succès.")
    except FileNotFoundError:
        print("Fichier introuvable. Aucun chargement effectué.")
    except Exception as e:
        print(f"Erreur lors du chargement : {e}")
