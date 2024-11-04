import password_generator as pg

# Hasilkan password dengan berbagai parameter
length = 12
password = pg.generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True)
print("Generated Password:", password)

# Periksa kekuatan password
strength = pg.check_password_strength(password)
print("Password Strength:", strength)

# Cek keunikan password terhadap kebocoran data
breach_check = pg.check_password_breach(password)
print("Breach Check:", breach_check)

# Enkripsi dan simpan password
pg.generate_key()  # Jalankan sekali untuk membuat kunci
pg.save_password_encrypted(password)
print("Password terenkripsi dan disimpan.")

# Dekripsi dan tampilkan password
decrypted_password = pg.load_password_decrypted()
print("Decrypted Password:", decrypted_password)

# Hasilkan passphrase
passphrase = pg.generate_passphrase(4)
print("Generated Passphrase:", passphrase)