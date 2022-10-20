import json

from utils.http_methods import Http_methods
from utils.pet_generator import Pet

"""Методы для тестирования PetStore"""

base_url = 'https://petstore.swagger.io/v2'

class PetStroreAPI:

    """Метод для создания нового животного"""
    @staticmethod
    def create_new_pet():

        house_pet = Pet().build()
        # json_for_create_new_pet = json.dumps(house_pet)
        post_resource = f'/pet'
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, house_pet)
        print(result_post.text)
        return result_post


    """Метод для проверки нового животного"""
    @staticmethod
    def get_new_pet(pet_id):

        get_resourse = f'/pet/{pet_id}'
        get_url = base_url + get_resourse
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get)
        return result_get