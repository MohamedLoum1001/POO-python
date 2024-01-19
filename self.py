# Définition de la classe Voiture
class Voiture:
    # Le constructeur __init__ est appelé lors de la création d'une instance
    def __init__(self, marque):
        # Initialisation de l'attribut d'instance "marque" avec la valeur passée en paramètre
        self.marque = marque
    
    # Méthode pour afficher la marque de la voiture
    def afficherMarque(self):
        # Utilisation de la fonction print pour afficher la marque
        print(f"La voiture est une {self.marque}")

# Création d'une instance de la classe Voiture avec la marque "Lamborghini"
Voiture1 = Voiture("Lamborghini")

# Appel de la méthode afficherMarque de l'instance créée pour afficher la marque
Voiture1.afficherMarque()
