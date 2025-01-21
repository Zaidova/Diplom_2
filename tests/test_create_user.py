import pytest
import allure
import data
import api
import helpers


class TestCreateUser:
    @allure.title('Создание пользователя')
    def test_create_user(self, user_data):
        create_response = api.create_user(user_data)

        assert create_response.status_code == 200

        response_payload = create_response.json()
        assert response_payload['success'] is True
        assert len(response_payload['accessToken']) > 0

    @allure.title('Повторное создание пользователя')
    def test_create_user_twice(self, created_user):
        create_response = api.create_user(created_user)

        assert create_response.status_code == 403
        assert create_response.json()["message"] == data.USER_ALREADY_EXISTS_MESSAGE

    @allure.title('Создание пользователя с пустым обязательным полем')
    @pytest.mark.parametrize(
        'credentials',
        [
            helpers.generate_new_user_credentials(empty_field='email'),
            helpers.generate_new_user_credentials(empty_field='password'),
            helpers.generate_new_user_credentials(empty_field='name')
        ]
    )
    def test_create_user_with_empty_field(self, credentials):
        create_response = api.create_user(credentials)

        assert create_response.status_code == 403
        assert create_response.json()["message"] == data.USER_MISSED_FIELD_MESSAGE