import json

import allure
import pytest
import requests

from api_testing.data import Urls


class TestListOfOrders:

    @allure.title('Получение общего списка всех заказов')
    def test_get_the_list_of_all_orders_positive_result(self):
        response = requests.get(f'{Urls.URL}{Urls.CREATE_ORDER}')
        r = response.json()
        assert response.status_code == 200
        assert 'orders' in r

    @pytest.mark.parametrize(
        'params',
        [
            ('?limit=10&page=0'),
            ('?limit=10&page=0&nearestStation=["110"]')
        ]
    )
    @allure.title('Получение списка 10 заказов доступных курьеру и 10 заказов возле метро')
    def test_get_the_list_of_10_orders_positive_result(self, params):
        response = requests.get(f'{Urls.URL}{Urls.CREATE_ORDER}{params}')
        r = response.json()
        assert response.status_code == 200
        assert 'orders' in r


    @allure.title('Получение списка всех активных/завершенных заказов курьера')
    def test_get_the_list_of_courier_orders_positive_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[0],
            "password": param[1]
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        courier_id = response.json()['id']
        response_1 = requests.get(f'{Urls.URL}{Urls.LIST_OF_COURIERS_ORDERS}{courier_id}')
        r = response_1.json()
        assert 200 == response_1.status_code
        assert r['orders'] == []

    @allure.title('Получение списка всех активных/завершенных заказов курьера возле метро')
    def test_get_the_list_of_courier_orders_near_metro_station_positive_result(self, return_login_password):
        param = return_login_password
        payload = {
            "login": param[0],
            "password": param[1]
        }
        response = requests.post(f'{Urls.URL}{Urls.LOGIN_COURIER}',
                                 data=payload)
        courier_id = response.json()['id']
        response_1 = requests.get(f'{Urls.URL}{Urls.LIST_OF_COURIERS_ORDERS_NEAR_METRO}{courier_id}{Urls.NEAREST_STATIONS}')
        r = response_1.json()
        assert 200 == response_1.status_code
        assert r['orders'] == []



