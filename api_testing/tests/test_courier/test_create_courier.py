import allure
import requests

from api_testing.data import Urls


class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier_new_courier_positive_result(self, register_new_courier):
        payload = register_new_courier
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', data=payload)
        assert 201 == response.status_code and '{"ok":true}' == response.text

    @allure.title('Создание курьера с тем же логином')
    def test_create_courier_the_same_login_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[0],
            "password": param[1],
            "firstName": param[2]
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', data=payload)
        assert 409 == response.status_code and '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}' == response.text

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "password": param[1],
            "firstName": param[2]
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', data=payload)
        assert 400 == response.status_code and '{"code":400,"message":"Недостаточно данных для создания учетной записи"}' == response.text

    @allure.title('Создание курьера без password')
    def test_create_courier_without_password_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[0],
            "firstName": param[2]
        }
        response = requests.post(f'{Urls.URL}{Urls.CREATE_COURIER}', data=payload)
        assert 400 == response.status_code and '{"code":400,"message":"Недостаточно данных для создания учетной записи"}' == response.text
