import fonctionsfacilitatrices as ff

livres = {
    "978-3-16-148410-0": {"titre": "L'Étranger", "auteur": "Albert Camus", "genre": "Fiction", "statut": "Disponible"},
    "978-0-14-028333-4": {"titre": "1984", "auteur": "George Orwell", "genre": "Science-fiction", "statut": "Disponible"}
}

print("Système de Gestion de la Bibliothèque")
ff.main_programme(livres)
