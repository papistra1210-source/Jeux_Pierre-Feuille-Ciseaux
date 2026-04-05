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

# Zone pour afficher le résultat
resultat = tk.Label(fenetre, text="", bg="#1e1e2f", fg="yellow")
resultat.pack(pady=10)

# 7. Générer un choix aléatoire pour l'ordinateur
choix = ["pierre", "feuille", "ciseaux"]
comp_pick = random.choice(choix)

# (Pour tester, on affiche le choix de l'ordinateur dans la console)
print("Choix ordinateur :", comp_pick)


# PHASE 2

# 1. Fonction play()
def play():
    user = choix_utilisateur.get().lower()
    comp_pick = random.choice(choix)

    # 2. Conditions pour déterminer le gagnant
    if user == comp_pick:
        res = "Égalité 🤝"
    elif (user == "pierre" and comp_pick == "ciseaux") or \
         (user == "feuille" and comp_pick == "pierre") or \
         (user == "ciseaux" and comp_pick == "feuille"):
        res = "Tu gagnes 🎉"
    elif user in choix:
        res = "Ordinateur gagne 🤖"
    else:
        res = "Choix invalide ❌"

    resultat.config(text=f"Ordi: {comp_pick} | {res}")


# 3. Fonction Reset()
def Reset():
    choix_utilisateur.delete(0, tk.END)
    resultat.config(text="")


# 4. Fonction Exit()
def Exit():
    fenetre.destroy()


# Boutons
btn_play = tk.Button(fenetre, text="Jouer", command=play)
btn_play.pack(pady=5)

btn_reset = tk.Button(fenetre, text="Réinitialiser", command=Reset)
btn_reset.pack(pady=5)

btn_exit = tk.Button(fenetre, text="Quitter", command=Exit)
btn_exit.pack(pady=5)

# Lancer la fenêtre
fenetre.mainloop()