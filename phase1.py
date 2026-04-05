# 1. Importer les bibliothèques nécessaires
import tkinter as tk
import random

# 2. Initialiser la fenêtre
fenetre = tk.Tk()
fenetre.title("Jeu Pierre-Feuille-Ciseaux")
fenetre.geometry("400x300")

# 3. Définir la couleur de fond
fenetre.configure(bg="#1e1e2f")

# 4. Créer une étiquette pour le titre
titre = tk.Label(fenetre, text="Pierre - Feuille - Ciseaux",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e2f", fg="white")
titre.pack(pady=10)

# 5. Inviter l'utilisateur à choisir
instruction = tk.Label(fenetre,
                       text="Entrez : pierre, feuille ou ciseaux",
                       bg="#1e1e2f", fg="white")
instruction.pack(pady=5)

# 6. Champ de saisie utilisateur
choix_utilisateur = tk.Entry(fenetre)
choix_utilisateur.pack(pady=5)

# 7. Générer un choix aléatoire pour l'ordinateur
choix = ["pierre", "feuille", "ciseaux"]
comp_pick = random.choice(choix)

# (Pour tester, on affiche le choix de l'ordinateur dans la console)
print("Choix ordinateur :", comp_pick)

# Lancer la fenêtre
fenetre.mainloop()