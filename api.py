import requests
import allure
import url


@allure.step('Отправляем запрос на создание пользователя')
def create_user(data):
    return requests.post(url.CREATE_USER, json=data)


@allure.step('Отправляем запрос авторизации пользователя')
def login_user(data):
    return requests.post(url.LOGIN_USER, json=data)


@allure.step('Отправляем запрос на удаление пользователя')
def delete_user(token):
    return requests.delete(url.CHANGE_USER, headers={"Authorization": token})


@allure.step('Отправляем запрос на изменение данных пользователя')
def change_user(data, token):
    if token:
        return requests.patch(url.CHANGE_USER, headers={"Authorization": token}, json=data)
    else:
        return requests.patch(url.CHANGE_USER, json=data)


@allure.step('Отправляем запрос на создание заказа')
def create_order(data, token):
    if token:
        return requests.post(url.CREATE_ORDER, headers={"Authorization": token}, json=data)
    else:
        return requests.post(url.CREATE_ORDER, json=data)


@allure.step('Отправляем запрос на получение заказов')
def get_orders(token):
    if token:
        return requests.get(url.CREATE_ORDER, headers={"Authorization": token})
    else:
        return requests.get(url.CREATE_ORDER)


@allure.step('Отправляем запрос на получение ингредиентов')
def get_ingredients():
    return requests.get(url.GET_INGREDIENTS)