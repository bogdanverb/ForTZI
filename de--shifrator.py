from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def save_key(key, file_path):
    with open(file_path, 'wb') as file:
        file.write(key)

def load_key(file_path):
    with open(file_path, 'rb') as file:
        key = file.read()
    return key

def encrypt_text(text, key):
    f = Fernet(key)
    encrypted_text = f.encrypt(text.encode())
    return encrypted_text

def decrypt_text(encrypted_text, key):
    f = Fernet(key)
    decrypted_text = f.decrypt(encrypted_text)
    return decrypted_text.decode()

key = generate_key()
save_key(key, 'key.txt')
loaded_key = load_key('key.txt')
text = 'Це текст для шифрування.'
encrypted_text = encrypt_text(text, loaded_key)
decrypted_text = decrypt_text(encrypted_text, loaded_key)
print('Оригінальний текст: ', text)
print('Зашифрований текст: ', encrypted_text)
print('Дешифрований текст: ', decrypted_text)


// для коректної роботи коду потрібно буде встановити бібліотеку "cryptography" або "pycryptodome"

// pip install cryptography
// або
// pip install pycryptodome