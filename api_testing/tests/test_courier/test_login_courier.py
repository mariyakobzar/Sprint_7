import json

import allure
import requests

from api_testing.data import Urls


class TestLoginCourier:

    @allure.title('Логин курьера')
    def test_login_courier_positive_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[0],
            "password": param[1]
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        print(response.json()['id'])
        assert 200 == response.status_code

    @allure.title('Логин курьера с неверным логином')
    def test_login_courier_with_wrong_login_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[1],
            "password": param[1]
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        print(response.json())
        assert 404 == response.status_code and '{"code":404,"message":"Учетная запись не найдена"}' == response.text

    @allure.title('Логин курьера с неверным password')
    def test_login_courier_with_wrong_password_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[0],
            "password": param[0]
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        print(response.json())
        assert 404 == response.status_code and '{"code":404,"message":"Учетная запись не найдена"}' == response.text

    @allure.title('Логин курьера без логина')
    def test_login_courier_without_login_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "password": param[1]
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        print(response.json())
        assert 400 == response.status_code and '{"code":400,"message":"Недостаточно данных для входа"}' == response.text

    @allure.title('Логин курьера без password')
    def test_login_courier_without_password_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[0]
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        assert 504 == response.status_code and 'Service unavailable' == response.text

    @allure.title('Логин курьера с неверными данными')
    def test_login_courier_with_wrong_data_negative_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": f"Q+{param[0]}",
            "password": f"1+{param[1]}"
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        assert 404 == response.status_code and '{"code":404,"message":"Учетная запись не найдена"}' == response.text
