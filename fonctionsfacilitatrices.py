import fonctionsprincipales as fp

def menu():
    print("Menu : \n 1. Ajouter un livre \n 2. Supprimer un livre \n 3. Rechercher un livre \n 4. Lister les livres \n 5. Emprunter un livre \n 6. Retourner un livre \n 7. Afficher les statistiques \n 8. Sauvegarder les données \n 9. Charger les données \n 10. Quitter\n")


def main_programme(livres):

    action = 0
    menu()
    while action != 10:
        try:
            action = int(input("Veuillez saisir le numéro de l'action que vous souhaitez effectuer : "))
        except ValueError:
            print("Entrée invalide. Veuillez saisir un chiffre entre 1 et 10.")
            continue
        if action == 1:
            fp.ajouter(livres)
        elif action == 2:
            fp.supprimer(livres)
        elif action == 3:
            fp.rechercher(livres)
        elif action == 4:
            fp.lister(livres)
        elif action == 5:
            fp.emprunter(livres)
        elif action == 6:
            fp.retourner(livres)
        elif action == 7:
            fp.afficher(livres)
        elif action == 8:
            fp.sauvegarder(livres)
        elif action == 9:
            fp.charger(livres)
        elif action == 10:
            print("Vous avez quitté le système. Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option du menu.")
