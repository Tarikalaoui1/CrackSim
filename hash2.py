import hashlib
import time

def hash_password(password, algorithm='md5'):
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()

def start_attack(target_hash, algorithm, wordlist):
    start_time = time.time()
    for word in wordlist:
        hashed = hash_password(word, algorithm)
        if hashed == target_hash:
            end_time = time.time()
            return (word, round(end_time - start_time, 2))
    return (None, None)
