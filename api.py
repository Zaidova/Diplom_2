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


@allure.step('Авторизация учетными данными')
def authorization_user(credentials):
    new_credentials = {
        'email': credentials['email'],
        'password': credentials['password']
    }
    response = login_user(new_credentials)
    response_payload = response.json()
    credentials['accessToken'] = response_payload['accessToken']


@allure.step('Создаем нового пользователя')
def new_user(credentials, login=False):
    response = create_user(credentials)
    response_payload = response.json()
    credentials['accessToken'] = response_payload['accessToken']

    if login:
        authorization_user(credentials)
    return credentials


@allure.step('Удаление пользователя')
def try_to_delete_user(credentials):
    response = login_user(credentials)
    if response.status_code == 200 and 'accessToken' in response.json():
        delete_user(response.json()['accessToken'])


@allure.step('Получаем список ингредиентов')
def get_available_ingredient_hashes(limit=2):
    response = get_ingredients()
    objects = response.json()['data']

    hashes = []
    for obj in objects:
        hashes.append(obj['_id'])
        if len(hashes) >= limit:
            break
    return hashes