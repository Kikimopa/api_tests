import json

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
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))

        print("\nМетод GET POST")
        result_get : Response = GoogleMapsAPI.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])

        print("\nМетод PUT")
        result_put: Response = GoogleMapsAPI.put_new_location(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])


        print("\nМетод GET PUT")
        result_get: Response = GoogleMapsAPI.get_new_location(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get,
                                  ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                   'language'])

        print("\nМетод DELETE")
        result_delete: Response = GoogleMapsAPI.delete_new_location(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])


        print("\nМетод GET DELETE")
        result_get: Response = GoogleMapsAPI.get_new_location(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])


        print("Тестирование создания, изменения и удаления локации успешно завершено!")


