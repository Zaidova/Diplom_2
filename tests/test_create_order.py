import allure
import data
import api


class TestCreateOrder:
    @allure.title('Создание заказа с авторизацией и корректными ингредиентами')
    def test_create_correct_order(self, logged_in_user_credentials, valid_ingredient_hashes):
        payload = {
            'ingredients': valid_ingredient_hashes[:2]
        }
        token = logged_in_user_credentials['accessToken']
        response = api.create_order(payload, token)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа с корректными ингредиентами но без авторизации')
    def test_create_order_without_auth(self, logged_in_user_credentials, valid_ingredient_hashes):
        payload = {
            'ingredients': valid_ingredient_hashes[:2]
        }
        token = None
        response = api.create_order(payload, token)

        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, logged_in_user_credentials):
        payload = {
            'ingredients': []
        }
        token = logged_in_user_credentials['accessToken']
        response = api.create_order(payload, token)

        assert response.status_code == 400
        assert response.json()['message'] == data.MISSED_INGREDIENTS_MESSAGE

    @allure.title('Создание заказа с невалидными ингредиентами')
    def test_create_order_with_invalid_ingredients(self, logged_in_user_credentials):
        payload = {
            'ingredients': data.INVALID_INGREDIENT_HASHES
        }
        token = logged_in_user_credentials['accessToken']
        response = api.create_order(payload, token)

        assert response.status_code == 500