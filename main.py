class Voiture:
    # Variable de classe pour compter le nombre total de voitures créées
    voiture_crees = 0
    
    #  La méthode __init__ (prononcée "dunder init" pour "double underscore init") est un constructeur spécial en Python. 
    # Il est appelé automatiquement lors de la création d'une nouvelle instance d'une classe.
    # Le rôle principal de __init__ est d'initialiser les attributs de l'objet avec les valeurs spécifiées 
    # lors de la création de l'instance.
    
    # self : C'est une convention en Python d'utiliser le mot-clé self comme le premier paramètre de chaque méthode
    # de classe, y compris __init__. Il représente l'instance de la classe elle-même.
    def __init__(self, marque, couleur):
        # À chaque création d'instance, incrémenter le compteur de voitures créées
        Voiture.voiture_crees += 1
        # Attributs d'instance pour stocker la marque et la couleur de la voiture
        self.marque = marque
        self.couleur = couleur

# Créer des instances de la classe Voiture avec des valeurs spécifiques
voiture1 = Voiture("Bugatti", "Rouge")
voiture2 = Voiture("Porsche", "Gris")

# Afficher les propriétés des instances créées
print("Voiture 1 - Marque:", voiture1.marque, ", Couleur:", voiture1.couleur)
print("Voiture 2 - Marque:", voiture2.marque, ", Couleur:", voiture2.couleur)

# Afficher le nombre total de voitures créées en utilisant la variable de classe
print("Nombre total de voitures créées:", Voiture.voiture_crees)
