import random
from data.pets import *
import json
from faker import Faker

class Pet:
    fake = Faker()
    def __init__(self):
        self.result = {}
        self.reset()

    def set_id(self, id=random.randint(0, 999)):
        self.result["id"] = id
        return self

    def set_category(self, category={"id": random.randint(0, 100), "name": random.choice(pets)}):
        self.result["category"] = category
        return self

    def set_pet_name(self, pet_name=fake.name()):
        self.result["name"] = pet_name
        return self

    def set_photo_url(self, url=['https://www.google.ru/']):
        self.result["photoUrls"] = url
        return self

    def set_pet_tags(self, tags=[{"id": random.randint(0, 100), "name": random.choice(pets)}]):
        self.result["tags"] = tags
        return self

    def set_status(self, status = 'available'):
        self.result["status"] = status

    def reset(self):
        self.set_id()
        self.set_category()
        self.set_pet_name()
        self.set_photo_url()
        self.set_pet_tags()
        self.set_status()
        return self

    def build(self):
        return self.result

