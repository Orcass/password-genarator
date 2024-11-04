import random
import hashlib
import requests
from cryptography.fernet import Fernet

# Fungsi shuffle
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Fungsi untuk menghasilkan password
def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    password_chars = ""
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    digit = "0123456789"
    symbols = "@#$%&*!?"

    if use_uppercase:
        password_chars += uppercase_letters
    if use_lowercase:
        password_chars += lowercase_letters
    if use_digits:
        password_chars += digit
    if use_symbols:
        password_chars += symbols

    if not password_chars:
        raise ValueError("Anda harus memilih setidaknya satu jenis karakter!")

    password = "".join(random.choice(password_chars) for _ in range(length))
    return shuffle(password)

# Fungsi untuk memeriksa kekuatan kata sandi
def check_password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbols = any(c in "@#$%&*!?" for c in password)

    if length >= 12 and has_upper and has_lower and has_digit and has_symbols:
        return "Sangat Kuat"
    elif length >= 8 and ((has_upper and has_lower) or (has_digit and has_symbols)):
        return "Kuat"
    else:
        return "Lemah"

# Fungsi untuk cek apakah password pernah muncul dalam kebocoran data
def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return f"Password ditemukan dalam kebocoran data sebanyak {count} kali!"
    return "Password aman dan tidak ditemukan dalam kebocoran data."

# Fungsi untuk enkripsi dan penyimpanan password
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def save_password_encrypted(password):
    key = load_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password.encode())
    with open("encrypted_password.txt", "wb") as file:
        file.write(encrypted_password)

def load_password_decrypted():
    key = load_key()
    cipher_suite = Fernet(key)
    with open("encrypted_password.txt", "rb") as file:
        encrypted_password = file.read()
    return cipher_suite.decrypt(encrypted_password).decode()

# Fungsi untuk membuat passphrase
def generate_passphrase(num_words=4):
    word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
    return '-'.join(random.choice(word_list) for _ in range(num_words))
