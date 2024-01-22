# Définition de la classe Personne
class Personne:
    # Méthode d'initialisation (constructeur)
    def __init__(self, nom: str, age: int, genre: bool):
        # Initialisation des attributs de l'objet
        self.nom = nom
        self.age = age
        self.genre = genre
        # Message d'indication du constructeur
        print("Constructeur personne " + self.nom)

    # Méthode pour la présentation de la personne
    def SePresenter(self):
        # Affichage des informations sur la personne
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")
        
        # Détermination du genre sous forme de chaîne
        genre_str = "Masculin" if self.genre else "Féminin"
        print(f"Genre : {genre_str}")
        
        # Ajout optionnel de la lettre "e" pour le féminin
        e_optionnel = "" if self.genre else "e"
        
        # Vérification si la personne est majeure
        if self.EstMajeur():
            print("Je suis majeur" + e_optionnel)
        else:
            print("Je suis mineur" + e_optionnel)
        
        print()  # Ligne vide pour une meilleure lisibilité

    # Méthode pour déterminer si la personne est majeure
    def EstMajeur(self):
        return self.age >= 18

# Création d'instances de la classe Personne
personne1 = Personne("Moustapha", 50, True)
personne1.SePresenter()

personne2 = Personne("Aminata", 15, False)
personne2.SePresenter()
