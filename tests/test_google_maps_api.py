from requests import Response

from utils.api import GoogleMapsAPI
from utils.checking import Checking

""" Создание, изменение и удаление локации"""

class TestCreateLocation:

    def test_create_new_place(self):

        print("\nМетод POST")
        result_post : Response = GoogleMapsAPI.create_new_location()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)

        print("\nМетод GET POST")
        result_get : Response = GoogleMapsAPI.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)

        print("\nМетод PUT")
        result_put: Response = GoogleMapsAPI.put_new_location(place_id)
        Checking.check_status_code(result_put, 200)

        print("\nМетод GET PUT")
        result_get: Response = GoogleMapsAPI.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)

        print("\nМетод DELETE")
        result_delete: Response = GoogleMapsAPI.delete_new_location(place_id)
        Checking.check_status_code(result_delete, 200)

        print("\nМетод GET DELETE")
        result_get: Response = GoogleMapsAPI.get_new_location(place_id)
        Checking.check_status_code(result_get, 404)
