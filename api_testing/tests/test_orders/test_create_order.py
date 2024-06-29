import json

import allure
import pytest
import requests

from api_testing.data import Urls


class TestCreateOrder:

    @pytest.mark.parametrize(
        'color',
        [
            (["BLACK"]),
            (["GREY"]),
            (["BLACK", "GREY"]),
            ([])
        ]
    )
    @allure.title('Заказ с выбором цвета самоката_позитивный сценарий')
    def test_create_order_positive_result(self, color):
        scooter_color = color
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": scooter_color
        }
        payload_string = json.dumps(payload)
        print(payload_string)
        response = requests.post(f'{Urls.URL}{Urls.CREATE_ORDER}', data=payload_string)
        print(response.json()['track'])
        assert 201 == response.status_code and response.json()['track']