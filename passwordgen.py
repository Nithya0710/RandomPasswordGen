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

def main():
    include_special=get_special_chars_preference()
    include_nums=get_nums_preference()
    print(f'Include numbers: {include_nums}')
    include_upper=get_uppercase_preference()
    print(f'Include uppercase letters: {include_upper}')

main()