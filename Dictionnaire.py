from tkinter import filedialog, messagebox

def select_wordlist():
    # Ouvre une fenêtre pour choisir un fichier texte (.txt)
    chemin = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt")])
    return chemin

def read_wordlist(chemin):
    try:
        with open(chemin, 'r', encoding='utf-8') as fichier:
            mots = [ligne.strip() for ligne in fichier]
        return mots
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Le fichier wordlist est introuvable.")
        return None
