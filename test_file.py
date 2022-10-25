import requests
from utils.pet_generator import Pet
from utils.pydantic_schema.delete import Delete
from utils.cheker.cheker import ResponseValid

base_url = 'https://petstore.swagger.io/v2'
post_resource = '/pet'
get_resource  = '/pet/'
delete_resource = f'/pet/'

pet_id = 123
headers = {
        'Content-Type' : "application/json",
    'api-key': "special-key"
    }
house_pet = Pet().set_id(pet_id).build()

r = requests.post(url=base_url+post_resource,json=house_pet, headers=headers)
print(r)

response = requests.delete(url=base_url+delete_resource+ "123", headers=headers)

result = ResponseValid(response)
result.assert_status_code(200).validate(Delete)


