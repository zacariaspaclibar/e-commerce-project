from datetime import datetime
import random
import string

FIRSTNAME = 'zac'
LASTNAME = 'pac'
EMAIL = f'zac_{datetime.now().strftime('%Y%m%d%H%M%S')}.@gmail.com'
PHONE_NUMBER = '09876543211'
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