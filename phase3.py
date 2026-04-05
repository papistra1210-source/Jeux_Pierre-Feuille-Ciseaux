# 1. Importer les bibliothèques nécessaires
import tkinter as tk
import random

# 2. Initialiser la fenêtre
fenetre = tk.Tk()
fenetre.title("Jeu Pierre-Feuille-Ciseaux")
fenetre.geometry("400x350")
fenetre.configure(bg="#1e1e2f")

# 4. Créer une étiquette pour le titre
titre = tk.Label(fenetre, text="Pierre - Feuille - Ciseaux",
                 font=("Arial", 16, "bold"),
                 bg="#1e1e2f", fg="white")
titre.pack(pady=10)

# 5. Instruction pour l'utilisateur
instruction = tk.Label(fenetre,
                       text="Entrez : pierre, feuille ou ciseaux",
                       bg="#1e1e2f", fg="white")
instruction.pack(pady=5)

# 6. Champ de saisie utilisateur
choix_utilisateur = tk.Entry(fenetre)
choix_utilisateur.pack(pady=5)

# 1. Champ de saisie pour afficher le résultat
resultat = tk.Label(fenetre, text="", bg="#1e1e2f", fg="yellow")
resultat.pack(pady=10)

# Liste des choix pour l'ordinateur
choix = ["pierre", "feuille", "ciseaux"]

# =========================
# PHASE 2 : Fonctions de logique
# =========================

def play():
    user = choix_utilisateur.get().lower()
    comp_pick = random.choice(choix)

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

def Reset():
    choix_utilisateur.delete(0, tk.END)
    resultat.config(text="")

def Exit():
    fenetre.destroy()

# =========================
# PHASE 3 : Boutons
# =========================

# 2. Bouton JOUER
btn_play = tk.Button(fenetre, text="JOUER", command=play)
btn_play.pack(pady=5)

# 3. Bouton RÉINITIALISER
btn_reset = tk.Button(fenetre, text="RÉINITIALISER", command=Reset)
btn_reset.pack(pady=5)

# 4. Bouton SORTIE
btn_exit = tk.Button(fenetre, text="SORTIE", command=Exit)
btn_exit.pack(pady=5)

# 6. Lancer l'application
fenetre.mainloop()