from requests import Response

from utils.api import GoogleMapsAPI

""" Создание, изменение и удаление локации"""

class TestCreateLocation:

    def test_create_new_place(self):

        print("\nМетод POST")
        result_post : Response = GoogleMapsAPI.create_new_location()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print("\nМетод GET")
        result_get : Response = GoogleMapsAPI.get_new_location(place_id)