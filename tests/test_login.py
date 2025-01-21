import pytest
import allure
import data
import api
import helpers


class TestCreateUser:
    @allure.title('Авторизация с корректными реквизитами')
    def test_login_user_with_correct_credentials(self, created_user):
        response = api.login_user(created_user)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title('Авторизация с некорректными реквизитами')
    @pytest.mark.parametrize(
        'incorrect_field',
        [
            'email',
            'password'
        ]
    )
    def test_login_user_with_incorrect_credentials(self, created_user, incorrect_field):
        created_user[incorrect_field] = helpers.generate_random_field(incorrect_field, 10)
        response = api.login_user(created_user)
        payload = response.json()

        assert response.status_code == 401
        assert payload["success"] is False
        assert payload["message"] == data.UNSUCCESSFUL_LOGIN_MESSAGE