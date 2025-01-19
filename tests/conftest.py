import pytest
import helpers


@pytest.fixture
def user_data():
    data = helpers.generate_new_user_credentials()

    yield data

    helpers.try_to_delete_user(data)


@pytest.fixture
def created_user():
    data = helpers.generate_new_user_credentials()
    helpers.create_user(data)

    yield data

    helpers.delete_user(data)


@pytest.fixture
def logged_in_user_credentials():
    credentials = helpers.generate_new_user_credentials()
    helpers.create_user(credentials, login=True)

    yield credentials

    helpers.delete_user(credentials)


@pytest.fixture
def valid_ingredient_hashes():
    return helpers.get_available_ingredient_hashes()