import pytest
from requests import Response
from utils.pet_generator import Pet
from utils.petstore_api import PetStroreAPI
from utils.pydantic_schema.post import Post
from utils.cheker.cheker import ResponseValid


class TestCreatePet:
    pet_id = 123

    """Add new pet"""
    @pytest.mark.skip
    def test_create_pet(self):
        print("\nМетод POST")
        body = Pet().set_id(self.pet_id).build()
        response: Response = PetStroreAPI.create_new_pet(body=body)
        post_result = ResponseValid(response)
        post_result.assert_status_code(200).validate(Post)



    """Get pet"""
    def test_get_pet(self):
        print("\nМетод GET")
        response: Response = PetStroreAPI.get_new_pet(self.pet_id)
        get_result = ResponseValid(response)
        get_result.assert_response_photourl_not_empty()


    """Put pet"""
    @pytest.mark.skip
    def test_put_pet(self):
        print("\nМетод PUT")
        body = Pet().set_id(self.pet_id).build()
        put_result: Response = PetStroreAPI.put_new_pet(json=body)

    """Delete pet"""
    @pytest.mark.skip
    def test_delete_pet(self):
        print("\nМетод DELETE")
        delete_result = Response = PetStroreAPI.delete_new_pet(self.pet_id)
