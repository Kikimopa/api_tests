from requests import Response

from utils.petstore_api import PetStroreAPI

class TestCreatePet:

    def test_create_pet(self):

        print("\nМетод POST")
        post_result : Response = PetStroreAPI.create_new_pet()
        check_post = post_result.json()
        pet_id = check_post.get('id')
        return pet_id

    # def test_get_pet(self):
    #
    #     print("\nМетод GET")
    #     get_result : Response = PetStroreAPI.get_new_pet()
    #     print(get_result.text)




