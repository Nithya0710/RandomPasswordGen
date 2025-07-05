import os
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import getpass

def gen_key(master_password):
    """
    Generate a secure encryption key from a master password
    """
    password=master_password.encode()
    salt=os.urandom(16)
    kdf=PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    key=base64.urlsafe_b64encode(kdf.derive(password))
    return key, salt

def write_passwords_to_file(passwords, filename='passwords.dat', master_password=None):
    """
    Write passwords to an encrypted file
    
    Args:
        passwords (list): List of passwords to store
        filename (str): Name of the output file
        master_password (str): Password to encrypt/decrypt the file
    
    Returns:
        str: Path to the created file
    
    Raises:
        ValueError: If master_password is not provided but encryption is required
        IOError: If file writing fails
    """
    directory=os.path.dirname(filename)
    if directory:
        os.makedirs(directory, exist_ok=True)
    if master_password:
        key, salt=gen_key(master_password)
        cipher_suite=Fernet(key)
    else:
        cipher_suite=None
    try:
        with open(filename, 'wb') as file:
            for i in passwords:
                if cipher_suite:
                    encrypted_password=cipher_suite.encrypt(i.encode())
                    file.write(encrypted_password + b'\n')
                else:
                    file.write(i.encode() + b'\n')
        return os.path.abspath(filename)
    except IOError as e:
        raise IOError(f"Failed to write to file: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while writing passwords: {str(e)}")

def check_file_permissions(filename):
    """
    Check if the file has secure permissions"
    """
    try:
        permissions=oct(os.stat(filename).st_mode)[-3:]
        if permissions!='600':
            print('Warning: File permissions are not secure. They should be set to 600.')
            os.chmod(filename, 0o600)
        return True
    except PermissionError:
        print("Permission denied when accessing file permissions.")
        return False
    
if __name__ == "__main__":
    passwords_to_save=["password1", "password2", "password3"]
    master_password=getpass.getpass("Enter master password: ")
    try:
        file_path=write_passwords_to_file(passwords_to_save, filename='secure/passwords.dat', master_password=master_password)
        print(f"Passwords saved securely to: {file_path}")
        check_file_permissions(file_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")