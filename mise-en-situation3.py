# Définition de la classe Chien
class Chien:
    # Méthode d'initialisation (constructeur)
    def __init__(self, nom_facultatif="inconnu"):
        # Initialisation de l'attribut nom avec une valeur par défaut "inconnu"
        self.nom = nom_facultatif
    
    # Méthode pour la présentation du chien
    def SePresenter(self):
        print("Bonjour, nous avons un chien et son nom est " + self.nom)

# Définition de la classe Personne
class Personne:
    # Méthode d'initialisation (constructeur)
    def __init__(self, nom: str):
        # Initialisation de l'attribut nom avec la valeur fournie
        self.nom = nom
    
    # Méthode pour la présentation de la personne
    def SePresenter(self):
        print("Bonjour, nous avons une personne et son nom est " + self.nom)

# Création d'instances de la classe Chien
chien1 = Chien()
chien1.SePresenter()

chien2 = Chien("Koutiii")
chien2.SePresenter()

# Création d'une instance de la classe Personne
personne = Personne("Moustapha")
personne.SePresenter()
