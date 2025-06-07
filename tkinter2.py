import tkinter as tk
from tkinter import messagebox
import Dictionnaire
import hash2

def choisir_wordlist():
    path = Dictionnaire.select_wordlist()
    if path:
        wordlist_var.set(path)

def lancer_attaque():
    target_hash = hash_entry.get().strip()
    algorithm = algo_var.get()
    path = wordlist_var.get()

    if not target_hash or not path:
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
        return

    wordlist = Dictionnaire.read_wordlist(path)
    if not wordlist:
        return

    mot, temps = hash2.start_attack(target_hash, algorithm, wordlist)
    if mot:
        result_text.set(f"✅ Mot de passe trouvé : {mot}\n⏱ Temps : {temps} sec")
    else:
        result_text.set("❌ Mot de passe non trouvé.")
        

root = tk.Tk()
root.title("Attaque par dictionnaire (MD5/SHA-256)")
root.geometry("500x350")
root.resizable(False, False)

tk.Label(root, text="Hash à casser :", font=("Arial", 12)).pack(pady=5)
hash_entry = tk.Entry(root, width=60)
hash_entry.pack(pady=5)

algo_var = tk.StringVar(value="md5")
tk.Label(root, text="Choisir l'algorithme :", font=("Arial", 12)).pack()
tk.Radiobutton(root, text="MD5", variable=algo_var, value="md5").pack()
tk.Radiobutton(root, text="SHA-256", variable=algo_var, value="sha256").pack()

wordlist_var = tk.StringVar()
tk.Button(root, text="Choisir la wordlist", command=choisir_wordlist).pack(pady=10)
tk.Label(root, textvariable=wordlist_var, wraplength=400, fg="blue").pack()

tk.Button(root, text="Lancer l'attaque", command=lancer_attaque, bg="#4CAF50", fg="white").pack(pady=15)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 12), fg="darkred").pack()

root.mainloop()
