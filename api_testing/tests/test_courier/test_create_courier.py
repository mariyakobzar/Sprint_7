import allure
import requests
class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier_new_courier_positive_result(self):
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data={
        "login": "логи89н41",
        "password": "24d892921",
        "firstName": "saske"
    })
        assert 201 == response.status_code and '{"ok":true}' == response.text

    @allure.title('Создание курьера с тем же логином')
    def test_create_courier_the_same_login_negative_result(selfr, register_new_courier_and_return_login_password):
        param = register_new_courier_and_return_login_password
        payload = {
            "login": param[0],
            "password": param[1],
            "firstName": param[2]
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data=payload)
        assert 409 == response.status_code and '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}' == response.text

    @allure.title('Создание курьера без логина')
    def test_create_courier_without_login_negative_result(self):
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data={
            "password": "92ey1",
            "firstName": "saske"
        })
        assert 400 == response.status_code and '{"code":400,"message":"Недостаточно данных для создания учетной записи"}' == response.text

    @allure.title('Создание курьера без password')
    def test_create_courier_without_password_negative_result(self):
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier", data={
            "login": "логи3491",
            "firstName": "saske"
        })
        assert 400 == response.status_code and '{"code":400,"message":"Недостаточно данных для создания учетной записи"}' == response.text
