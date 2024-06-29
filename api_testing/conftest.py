import pytest
import requests
import random
import string

from api_testing.data import Urls
from api_testing.helpers import Helpers


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@pytest.fixture()
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    Helpers.generate_random_string()
    #def generate_random_string(length):
        #letters = string.ascii_lowercase
        #random_string = ''.join(random.choice(letters) for i in range(length))
        #return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    def generate_payload():
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }

    payload = generate_payload()

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    def registration(data):
        login_pass.append(data['login'])
        login_pass.append(data['password'])
        login_pass.append(data['first_name'])

    registration(payload)
    # возвращаем список
    return login_pass


@pytest.fixture()
def register_new_courier():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # генерируем логин, пароль и имя курьера
    def generate_payload():
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }
    return generate_payload()

@pytest.fixture()
def return_login_password(register_new_courier):

    courier = register_new_courier

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=courier)

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    def registration(data):
        login_pass.append(data['login'])
        login_pass.append(data['password'])
        login_pass.append(data['firstName'])

    registration(courier)
    # возвращаем список
    return login_pass


