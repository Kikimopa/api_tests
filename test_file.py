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


response = requests.get(url=base_url+get_resource+ "123", headers=headers)
print(response.json().get('photoUrls')[0])
