# 🔐 HashBreaker – Simulation d'une attaque par dictionnaire (MD5 / SHA-256)

## 🔍 Description du projet
HashBreaker est un projet éducatif développé en Python qui simule une attaque par dictionnaire contre des mots de passe hashés. Il a pour but de démontrer la vulnérabilité des algorithmes de hachage non sécurisés, et de sensibiliser à l'importance des bonnes pratiques en cybersécurité (salage, hash robustes, etc.).

## ⚙️ Fonctionnalités principales
- 📁 Lecture d’un fichier de dictionnaire de mots de passe.
- 🔐 Comparaison de hash (MD5 et SHA-256) pour retrouver le mot de passe d'origine.
- 🧰 Génération de hash à partir d’un mot de passe (`hash_createur.py`).
- 💻 Interface possible avec Tkinter pour une interaction utilisateur simple.

## 🧠 Objectifs pédagogiques
- Comprendre le fonctionnement des fonctions de hachage.
- Simuler une attaque de type "dictionnaire" sur des mots de passe hashés.
- Se familiariser avec Python (lecture de fichiers, bibliothèques comme `hashlib`, `tkinter`).

## 🛠️ Technologies utilisées
- Python 3.x  
- hashlib  
- Tkinter (interface graphique)

## 📂 Fichiers principaux
- `Dictionnaire.py` – script principal de l’attaque par dictionnaire  
- `hash_createur.py` – génère un hash MD5 ou SHA-256 à partir d’un mot  
- `hash2.py` – version alternative ou test complémentaire  
- `tkinter2.py` – interface utilisateur graphique (facultative)

## ⚠️ Avertissement
> Ce projet est uniquement à but éducatif. Il ne doit en aucun cas être utilisé pour des activités malveillantes. Apprenez à vous défendre en comprenant les techniques d’attaque.

## 📚 Auteur
Projet développé dans le cadre de ma formation en "Infrastructure Digitale", module "Sécurité Informatique".  
"Étudiant passionné par les systèmes, réseaux et la cybersécurité."
