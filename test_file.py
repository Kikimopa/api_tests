import requests
from utils.pet_generator import Pet
import json

base_url = 'https://petstore.swagger.io/v2'
post_resource = '/pet'
get_resource  = '/pet/'

headers = {
        'Content-Type' : "application/json"
    }
house_pet = Pet().build()

json_post = json.dumps(house_pet)
print(json_post)

response = requests.post(url=base_url+post_resource, json=json_post, headers=headers)
print(response.text)

check_post = response.json()
pet_id = check_post.get("id")
print(pet_id)