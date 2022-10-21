import pytest
from requests import Response
from utils.pet_generator import Pet
from utils.petstore_api import PetStroreAPI
import requests


class TestCreatePet:
    pet_id = 123

    """Add new pet"""

    @pytest.mark.skip
    def test_create_pet(self):
        print("\nМетод POST")
        body = Pet().set_id(self.pet_id).build()
        post_result: Response = PetStroreAPI.create_new_pet(body=body)

    """Get pet"""

    @pytest.mark.skip
    def test_get_pet(self):
        print("\nМетод GET")
        get_result: Response = PetStroreAPI.get_new_pet(self.pet_id)

    """Put pet"""

    def test_put_pet(self):
        print("\nМетод PUT")
        body = Pet().set_id(self.pet_id).build()
        put_result: Response = PetStroreAPI.put_new_pet(json=body)

    """Delete pet"""

    @pytest.mark.skip
    def test_delete_pet(self):
        print("\nМетод DELETE")
        delete_result = Response = PetStroreAPI.delete_new_pet(self.pet_id)
