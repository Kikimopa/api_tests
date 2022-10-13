
import json

from requests import Response


""" Методы для проверки ответов наших запросов"""
class Checking:

    """ Метод для проверки статус кода"""
    @staticmethod
    def check_status_code(response : Response, status_code):
        assert response.status_code == status_code
        if response.status_code == status_code:
            print(f'Успешно! Статус код = {response.status_code}')
        else:
            print(f'Провал! Статус код = {response.status_code}')

    """ Метод для проверки наличия обязательных полей в ответе запросов"""
    @staticmethod
    def check_json_token(response : Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутствуют")