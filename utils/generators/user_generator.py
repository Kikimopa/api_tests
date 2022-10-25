import random
from faker import Faker
import string
import secrets


class User:

    def __init__(self):
        self.result = {}
        self.reset()

    def set_user_id(self, id=random.randint(0, 999)):
        self.result["id"] = id
        return self

    def set_user_name(self, user_name=''.join(Faker().name().split())):
        self.result["username"] = str(user_name)
        return self

    def set_first_name(self, first_name=Faker().first_name()):
        self.result["firstName"] = str(first_name)
        return self

    def set_last_name(self, last_name=Faker().last_name()):
        self.result["lastName"] = str(last_name)
        return self

    def set_email(self, email=Faker().email()):
        self.result["email"] = str(email)
        return self

    def set_password(self, password=''.join(secrets.choice(string.ascii_letters) for i in range(8))):
        self.result["password"] = str(password)
        return self

    def set_phone_number(self, phone_number="+" + ''.join(secrets.choice(string.digits) for i in range(11))):
        self.result["phone"] = str(phone_number)
        return self

    def set_user_status(self, user_status=1):
        self.result["userStatus"] = user_status
        return self

    def reset(self):
        self.set_user_id()
        self.set_user_name()
        self.set_first_name()
        self.set_last_name()
        self.set_email()
        self.set_password()
        self.set_phone_number()
        self.set_user_status()
        return self

    def build(self):
        return self.result


z = User().build()
print(z)
