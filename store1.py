import os
from pathlib import Path
from cryptography.fernet import Fernet
import json
import logging

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
    
def write_passwords_to_file(passwords, filename):
    """
    Writes generated passwords to a specified file securely.
    Returns True if successful, False otherwise.
    """
    try:
        with open(filename, 'w') as f:
            for i in passwords:
                f.write(i+'\n')
        return True
    except PermissionError:
        logging.error("Permission denied when trying to write to file: {}".format(filename))
        print("Error: Permission denied. Please check file permissions.")
        return False
    except IOError as e:
        logging.error("I/O error occurred while writing to file: {}".format(str(e)))
        print("Error: Unable to write to file. Please check the file path and try again.")
        return False
    except Exception as e:
        logging.error("Unexpected error occurred while writing to file: {}".format(str(e)))
        print("An expected error occurred: {}".formate(str(e)))
        return False
    else:
        print("Passwords successfully saved to: {}".format(filename))
        return True
    finally:
        pass

if __name__=="__main__":
    secret_key=gen_key()
    passwords={"email": "strongpassword123!", "bank_account": "anothersecurepassword456"}
    filename="secure.txt"
    success=write_passwords_to_file(passwords, filename)
    if success:
        print("Passwords saved securely.")
    else:
        print("Error.")