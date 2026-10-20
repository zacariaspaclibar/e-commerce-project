import random
import string
import uuid
# TODO: Transfer all the repeated parameter regarding ording and entry point
def generated_email():
    return f'zac_{uuid.uuid4().hex[:8]}@gmail.com'

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



DEFAULT_SINGLE_ORDER = ('home_page', 1)
DEFAULT_MULTI_ORDER = ('home_page', 3)
ALTERNATIVE_SINGLE_ORDER = ('product_page', 1)

DEFAULT_SINGLE_ORDER_WITH_COUNTRY = DEFAULT_SINGLE_ORDER + ('Philippines',)

LIST_OF_PRODUCTS = [
        'ADIDAS',
        'ZARA',
        'iphone',
        'adidas'
    ]


INCORRECT_CONFIRM_PASSWORD = generate_password()
GENERATED_EMAIL_ADDRESS = generated_email()
