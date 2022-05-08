
   
from unittest import TestCase
import requests
from fastapi import status
from bson import ObjectId
from cgi import test

from models.user import User

class TestApi(TestCase):
    def setUp(self) : 
        self.url = 'http://127.0.0.1:8000/docs'
        print("oui")

    #def test_create(self):
    #    user = requests.post('http://127.0.0.1:8000/', json = {"name": "test1","email": "test@test.com","password": "123456"})
    #    self.assertEqual(user.status_code, 200)
    
    #def test_getAll(self):
    #    users = requests.get('http://127.0.0.1:8000/').json()
    #    self.assertNotEqual(len(users), 0)

    #def test_updateUser(self):
    #    user = requests.put('http://127.0.0.1:8000/6277ca2a9410356d6bde4792', json = {"name": "test update","email": "test@test.com","password": "123456"})
    #    self.assertEqual(user.status_code, 200)

    def test_deleteUser(self):
        user = requests.delete('http://127.0.0.1:8000/6277c5136c00629f16d2b394')
        self.assertEqual(user.status_code, 200)