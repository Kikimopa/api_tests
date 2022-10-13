from requests import Response

from utils.api import GoogleMapsAPI

""" Создание, изменение и удаление локации"""

class TestCreateLocation:

    def test_create_new_place(self):

        print("Метод POST")
        result_post = Response = GoogleMapsAPI.create_new_location()
