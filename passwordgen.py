import secrets
import string
import random

def get_password_len():
    """
    Gets and validates the password length from the user.
    Returns:
        int: The validated password length
    """
    while True:
        try:
            length=int(input("Enter Password Length (between 8-128):"))
            if length<8:
                print('Password length must be at least 8 characters.')
            elif length>128:
                print('Password length cannot exceed 128 characters.')
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a number.")

def validate(prompt):
    while True:
        preference=input(prompt).strip().lower()
        if preference in ['yes','y']:
            return True
        elif preference in ['no','n']:
            return False
        else:
            print('Please enter \'yes\' or \'no\' (or \'y\'/\'n\' for short)')

def get_special_chars_preference():
    return validate('Include special characters? (yes/no): ')

def get_nums_preference():
    return validate('Include numbers? (yes/no): ')

def get_uppercase_preference():
    return validate('Include uppercase letters? (yes/no): ')

def gen_password(length: int, has_uppercase: bool=True, has_nums: bool=True, has_special: bool=True) -> str:
    """
    Generates a random password with specified length and character set options.
    
    Args:
        length (int): The desired length of the password
        has_uppercase (bool): Include uppercase letters (A-Z)
        has_numbers (bool): Include numbers (0-9)
        has_special (bool): Include special characters (!@#$%^&*())
        
    Returns:
        str: The generated password
    """
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    special_chars='!@#$%^&*()'
    char_sets=[lowercase]
    if has_uppercase:
        char_sets.append(uppercase)
    if has_nums:
        char_sets.append(digits)
    if has_special:
        char_sets.append(special_chars)
    base=[]
    for char_set in char_sets:
        base.append(secrets.choice(char_set))
    all_chars=''.join(char_sets)
    remaining_len=length-len(base)
    if remaining_len>0:
        additional_chars=[secrets.choice(all_chars) for _ in range(remaining_len)]
        base+=additional_chars
    secrets.SystemRandom().shuffle(base)
    return ''.join(base)

def get_char_sets():
    """
    Returns a dictionary of character sets for password generation.
    """
    lowercase=string.ascii_lowercase
    uppercase=string.ascii_uppercase
    digits=string.digits
    special_chars=string.punctuation
    return {
        'lowercase': lowercase,
        'uppercase': uppercase,
        'digits': digits,
        'special': special_chars
    }

def gen_password1(length, use_uppercase, use_nums, use_special):
    """
    Generates a random password with specified length and character criteria
    Ensures at least one character from each selected category
    """
    chars=set(string.ascii_lowercase)
    if use_uppercase:
        chars.update(string.ascii_uppercase)
    if use_nums:
        chars.update(string.digits)
    if use_special:
        chars.update(string.punctuation)
    char_list=list(chars)
    password=[]
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_nums:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    password.append(random.choice(string.ascii_lowercase))
    for _ in range(length-len(password)):
        password.append(random.choice(char_list))
    random.shuffle(password)
    return ''.join(password)

def main():
    length=get_password_len()
    has_special=get_special_chars_preference()
    has_nums=get_nums_preference()
    has_uppercase=get_uppercase_preference()
    password=gen_password1(length, has_uppercase, has_nums, has_special)
    print(f'Password: {password}')

if __name__ == "main":
    main()