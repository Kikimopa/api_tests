import json

from requests import Response
import allure
from utils.api import GoogleMapsAPI
from utils.checking import Checking

""" Создание, изменение и удаление локации"""
@allure.epic("Test create place")
class TestCreateLocation:
    @allure.description("Test create, update, delete place")
    def test_create_new_place(self):
        with allure.step("Create new place"):
            print("\nМетод POST")
            result_post : Response = GoogleMapsAPI.create_new_location()
            check_post = result_post.json()
            place_id = check_post.get('place_id')
            Checking.check_status_code(result_post, 200)
            Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
            # token = json.loads(result_post.text)
            # print(list(token))
            Checking.check_json_value(result_post, 'status', 'OK')
        with allure.step("Get new place"):
            print("\nМетод GET POST")
            result_get : Response = GoogleMapsAPI.get_new_location(place_id)
            Checking.check_status_code(result_get, 200)
            Checking.check_json_token(result_get,
                                      ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                       'language'])
            Checking.check_json_value(result_get, 'name', "Frontline house")
        with allure.step("Update place"):
            print("\nМетод PUT")
            result_put: Response = GoogleMapsAPI.put_new_location(place_id)
            Checking.check_status_code(result_put, 200)
            Checking.check_json_token(result_put, ['msg'])
            Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        with allure.step("Get updated place"):
            print("\nМетод GET PUT")
            result_get: Response = GoogleMapsAPI.get_new_location(place_id)
            Checking.check_status_code(result_get, 200)
            Checking.check_json_token(result_get,
                                      ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                       'language'])
            Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')
        with allure.step("Delete place"):
            print("\nМетод DELETE")
            result_delete: Response = GoogleMapsAPI.delete_new_location(place_id)
            Checking.check_status_code(result_delete, 200)
            Checking.check_json_token(result_delete, ['status'])
            Checking.check_json_value(result_delete, 'status', 'OK')

        with allure.step("Get deleted place"):
            print("\nМетод GET DELETE")
            result_get: Response = GoogleMapsAPI.get_new_location(place_id)
            Checking.check_status_code(result_get, 404)
            Checking.check_json_token(result_get, ['msg'])
            Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")


        print("Тестирование создания, изменения и удаления локации успешно завершено!")


