# Définition de la classe Personne
class Personne:
    # Méthode d'initialisation (constructeur)
    def __init__(self, nom: str):
        # Initialisation de l'attribut nom avec la valeur fournie
        self.nom = nom
    
    # Méthode pour la présentation de la personne
    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# Nombre de personnes à créer
nbre_de_personne = 3

# Liste pour stocker les instances de la classe Personne
liste_personnes = []

# Boucle pour créer des instances de Personne et les ajouter à la liste
for i in range(nbre_de_personne):
    # Demande à l'utilisateur d'entrer le nom de la personne
    nom = input("Nom de la personne " + str(i+1) + " : ")
    # Création d'une instance de Personne avec le nom fourni
    liste_personnes.append(Personne(nom))

# Boucle pour présenter chaque personne de la liste
for personne in liste_personnes:
    personne.SePresenter()
