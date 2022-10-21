import json

from utils.http_methods import Http_methods
from utils.pet_generator import Pet

"""Методы для тестирования PetStore"""

base_url = 'https://petstore.swagger.io/v2'

class PetStroreAPI:

    """Метод для создания нового животного"""
    @staticmethod
    def create_new_pet(body):

        post_resource = f'/pet'
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, body)
        print(result_post.text)
        return result_post


    """Метод для проверки нового животного"""
    @staticmethod
    def get_new_pet(pet_id):

        get_resourse = f'/pet/{pet_id}'
        get_url = base_url + get_resourse
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Метод для измнения животного"""
    @staticmethod
    def put_new_pet(json):

        put_resource = f'/pet'
        put_url = base_url+put_resource
        print(put_url)
        result_put = Http_methods.put(put_url, json)
        print(result_put.text)
        return result_put

    """Мотод для удаления животного"""
    @staticmethod
    def delete_new_pet(pet_id):
        delete_resource = f'/pet/{pet_id}'
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = Http_methods.delete(delete_url)
        print(result_delete.text)