import os
from pathlib import Path
from cryptography.fernet import Fernet
import json

def gen_key():
    """
    Generate a secret key for encryption.
    """
    key=Fernet.generate_key()
    return key

def encrypt_data(data, key):
    """
    Encrypt the password data using Fernet.
    """
    cipher_suite=Fernet(key)
    cipher_text=cipher_suite.encrypt(data.encode('utf-8'))
    return cipher_text

def save_passwords_securely(passwords, key):
    """
    Save passwords to a secure file with encryption.
    """
    try:
        curr_dir=Path.cwd()
        password_dir=curr_dir/"secure"
        password_dir.mkdir(exist_ok=True)
        file_name="secure_passwords.json"
        file_path=password_dir/file_name
        data=json.dumps(passwords)
        encrypted_data=encrypt_data(data, key)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        os.chmod(file_path, 0o600)
        print(f"Passwords saved securely to {file_name}")
        return True
    except Exception as e:
        print(f"Error saving passwords: {str(e)}")
        return False

if __name__=="__main__":
    secret_key=gen_key()
    passwords={"email": "strongpassword123!", "bank_account": "anothersecurepassword456"}
    success=save_passwords_securely(passwords, secret_key)
    if success:
        print("Passwords saved securely.")
    else:
        print("Error.")