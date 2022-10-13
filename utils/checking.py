""" Методы для проверки ответов наших запросов"""
from requests import Response


class Checking:

    """ Метод для прооерки статус кода"""
    @staticmethod
    def check_status_code(response : Response, status_code):
        assert response.status_code == status_code
        if response.status_code == status_code:
            print(f'Успешно! Статус код = {response.status_code}')
        else:
            print(f'Провал! Статус код = {response.status_code}')