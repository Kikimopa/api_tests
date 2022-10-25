import pytest
import allure
from requests import Response
from utils.generators.pet_generator import Pet
from utils.generators.user_generator import User
from utils.petstore_api import PetStroreAPI
from utils.pydantic_schema.post import PostPet, PostUser
from utils.pydantic_schema.get import GetPet
from utils.pydantic_schema.put import PutPet
from utils.pydantic_schema.delete import DeletePet
from utils.cheker.cheker import ResponseValid


@pytest.mark.pets
@allure.epic("Tests to create, get, update, delete pet.")
class TestCreatePet:
    pet_id = 123

    """Add new pet"""
    @allure.description("Add new pet")
    def test_create_pet(self):
        print("\nМетод POST")
        with allure.step("Build new pet"):
            body = Pet().set_id(self.pet_id).build()
            response: Response = PetStroreAPI.Pets.create_new_pet(body=body)
            with allure.step("Validate response"):
                post_result = ResponseValid(response)
                post_result.assert_status_code(200).validate(PostPet)



    """Get pet"""

    @allure.description("Get new pet")
    def test_get_pet(self):
        print("\nМетод GET")
        with allure.step("Get pet by id"):
            response: Response = PetStroreAPI.Pets.get_new_pet(self.pet_id)
            with allure.step("Validate response"):
                get_result = ResponseValid(response)
                get_result.assert_status_code(200).validate(GetPet)


    """Put pet"""

    @allure.description("Update pet")
    def test_put_pet(self):
        print("\nМетод PUT")
        with allure.step("Build new pet"):
            body = Pet().set_id(self.pet_id).build()
            response: Response = PetStroreAPI.Pets.put_new_pet(json=body)
            with allure.step("Validate response"):
                put_result = ResponseValid(response)
                put_result.assert_status_code(200).validate(PutPet)

    """Delete pet"""

    @allure.description("Delete pet")
    def test_delete_pet(self):
        print("\nМетод DELETE")
        with allure.step("Delete pet by id"):
            response : Response = PetStroreAPI.Pets.delete_new_pet(self.pet_id)
            with allure.step("Validate response"):
                delete_result = ResponseValid(response)
                delete_result.assert_status_code(200).validate(DeletePet)

@pytest.mark.users
class TestCreateUsers:

    """Create new user"""
    def test_create_new_user(self):
        body = User().build()
        response : Response = PetStroreAPI.Users.post_new_user(body)
        post_result = ResponseValid(response)
        post_result.assert_status_code(200).validate(PostUser)
