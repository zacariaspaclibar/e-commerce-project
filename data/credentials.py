import uuid
import random
import string

FIRSTNAME = 'zac'
LASTNAME = 'pac'
def generated_email():
    return f'zac_{uuid.uuid4().hex[:8]}@gmail.com'

EXISTING_EMAIL = 'zacpac@gmail.com'
PHONE_NUMBER = '1234567890'
PASSWORD = 'P@ssw0rd123!'
CONFIRM_PASSWORD = PASSWORD

def generate_password():
    chars = string.ascii_letters
    nums = string.digits
    symbols = "!@#$^&*()"

    password = (
        random.choices(chars, k=5)
        + random.choices(nums, k=4)
        + random.choices(symbols, k=3)
    )
    random.shuffle(password)
    return "".join(password)


INCORRECT_CONFIRM_PASSWORD = generate_password()

BASED_URL = 'https://rahulshettyacademy.com/client'
