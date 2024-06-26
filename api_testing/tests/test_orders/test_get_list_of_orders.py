import json

import allure
import pytest
import requests

class TestListOfOrders:

    @allure.title('Получение общего списка всех заказов')
    def test_get_the_list_of_all_orders_positive_result(self):
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders')
        r = response.json()
        assert response.status_code == 200
        assert 'orders' in r

    @pytest.mark.parametrize(
        'params',
        [
            ('limit=10&page=0'),
            ('limit=10&page=0&nearestStation=["110"]')
        ]
    )
    @allure.title('Получение списка 10 заказов доступных курьеру и 10 заказов возле метро')
    def test_get_the_list_of_10_orders_positive_result(self, params):
        response = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders?{params}')
        r = response.json()
        assert response.status_code == 200
        assert 'orders' in r


    @allure.title('Получение списка всех активных/завершенных заказов курьера')
    def test_get_the_list_of_courier_orders_positive_result(self, register_new_courier_and_return_login_password):
        param = register_new_courier_and_return_login_password
        payload = {
            "login": param[0],
            "password": param[1]
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
                                 data=payload)
        courier_id = response.json()['id']
        response_1 = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId={courier_id}')
        r = response_1.json()
        assert 200 == response_1.status_code
        assert r['orders'] == []

    @allure.title('Получение списка всех активных/завершенных заказов курьера возле метро')
    def test_get_the_list_of_courier_orders_near_metro_station_positive_result(self, register_new_courier_and_return_login_password):
        param = register_new_courier_and_return_login_password
        payload = {
            "login": param[0],
            "password": param[1]
        }
        response = requests.post("https://qa-scooter.praktikum-services.ru/api/v1/courier/login",
                                 data=payload)
        courier_id = response.json()['id']
        response_1 = requests.get(f'https://qa-scooter.praktikum-services.ru/api/v1/orders?courierId={courier_id}&nearestStation=["1", "2"]')
        r = response_1.json()
        assert 200 == response_1.status_code
        assert r['orders'] == []



