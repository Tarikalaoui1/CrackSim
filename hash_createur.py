import hashlib

def get_hash(text, algo='md5'):
    algo = algo.lower()
    if algo == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algo == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        raise ValueError("Algorithme non supporté. Utilisez 'md5' ou 'sha256'.")

if __name__ == "__main__":
    texte = input("Entrez le texte à hasher : ")
    algo = input("Choisissez l'algorithme (md5/sha256) [md5 par défaut] : ") or "md5"
    try:
        print("Hash :", get_hash(texte, algo))
    except ValueError as e:
        print(e)
