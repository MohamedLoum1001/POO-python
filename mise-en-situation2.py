# Définition de la classe Personne
class Personne:
    # Méthode d'initialisation (constructeur)
    def __init__(self, nom: str, age: int):
        # Initialisation des attributs de l'objet
        self.nom = nom
        self.age = age
        # Message d'indication du constructeur
        print("Constructeur personne " + self.nom)

    # Méthode pour la présentation de la personne
    def SePresenter(self):
        # Affichage des informations sur la personne
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        
        # Vérification si la personne est majeure
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
        
        print()  # Ligne vide pour une meilleure lisibilité

    # Méthode pour déterminer si la personne est majeure
    def EstMajeur(self):
        return self.age >= 18

# Création d'instances de la classe Personne
personne1 = Personne("Moustapha", 50)
personne2 = Personne("Aminata", 15)

# Appel de la méthode SePresenter pour chaque personne
personne1.SePresenter()
personne2.SePresenter()