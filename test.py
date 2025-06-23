import unittest
from passwordgen import gen_password

def test_password_gen():
    # Test case 1: Only lowercase letters
    print('\nTest Case 1: Only lowercase letters')
    criteria={
        'length': 10,
        'has_upper': False,
        'has_nums': False,
        'has_special': False
    }
    password=gen_password(10, False, False, False)
    assert password.islower(), 'Test Case 1 Failed: Password contains non-lowercase characters'
    print('Test Case 1 Passed')

    # Test case 2: Include special characters
    print('\nTest Case 2: Include special characters')
    criteria={
        'length': 10,
        'has_upper': False,
        'has_nums': False,
        'has_special': True
    }
    password=gen_password(10, False, False, True)
    special_chars='!@#$%^&*()_+-='
    assert any (char in special_chars for char in password), 'Test Case 2 Failed: Password doesn\'t contain special characters'
    print('Test Case 2 Passed')

    # Test case 3: Include numbers
    print('\nTest Case 3: Include numbers')
    criteria={
        'length': 10,
        'has_upper': False,
        'has_nums': True,
        'has_special': False
    }
    password=gen_password(10, False, True, False)
    assert any(char.isdigit() for char in password), 'Test Case 3 Failed: Password doesn\'t contain numbers'
    print('Test Case 3 Passed')

    # Test case 4: Include uppercase letters
    print('\nTest Case 4: Include uppercase letters')
    criteria={
        'length': 10,
        'has_upper': True,
        'has_nums': False,
        'has_special': False
    }
    password=gen_password(10, True, False, False)
    assert any(char.isupper() for char in password), 'Test Case 4 Failed: Password doesn\'t contain uppercase letters'
    print('Test Cae 4 Passed')

    # Test case 5: All character types
    print('\nTest Case 5: All character types')
    criteria={
        'length': 10,
        'has_upper': True,
        'has_nums': True,
        'has_special': True
    }
    password=gen_password(10, True, True, True)
    has_lower=any(char.islower() for char in password)
    has_upper=any(char.isupper() for char in password)
    has_nums=any(char.isdigit() for char in password)
    has_special=any(char in special_chars for char in password)
    assert has_lower and has_upper and has_nums and has_special, 'Test Case 5 Failed: Password doesn\'t contain all character types'
    print('Test Case 5 Passed')

    # Test case 6: Minimal length
    print('\nTest Case 6: Minimal length')
    criteria={
        'length': 4,
        'has_upper': True,
        'has_nums': True,
        'has_special': True
    }
    password=gen_password(4, True, True, True)
    assert len(password)==4 , f"Test Case 6 Failed: Expected length 4, got {len(password)}"
    print('Test Case 6 Passed')

    # Test case 7: Maximum length
    print('\nTest Case 7: Maximum length')
    criteria={
        'length': 20,
        'has_upper': True,
        'has_nums': True,
        'has_special': True
    }
    password=gen_password(20, True, True, True)
    assert len(password)==20, f"Test Case 7 Failed: Expected length 20, got {len(password)}"
    print('Test Case 7 Passed\n\nAll Test Cases Passed Successfully\n')

test_password_gen()