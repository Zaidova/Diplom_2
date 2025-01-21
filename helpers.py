import string
import random
import api


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string


def generate_random_email(length):
    login = generate_random_string(length)
    return login + '@yandex.ru'


def generate_random_field(field, length):
    if field == 'email':
        return generate_random_email(length)
    else:
        return generate_random_string(length)


def generate_new_user_credentials(empty_field=None):
    email = generate_random_email(10)
    password = generate_random_string(10)
    name = generate_random_string(10)

    credentials = {
        "email": email,
        "password": password,
        "name": name
    }
    if empty_field is not None:
        credentials[empty_field] = ""
    return credentials


def delete_user(credentials):
    api.delete_user(credentials['accessToken'])
