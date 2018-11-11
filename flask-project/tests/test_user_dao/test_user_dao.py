import unittest
from app.dao.user_dao import *

class TestUserDao(unittest.TestCase):
    def test_adduser(self):
        user = {
            "tel": "13311111111",
            "password": "999999",
        }
        self.assertEqual(1,addUser(user))

    def test_updataUser(self):
        user={
            "id":48,
            "newpwd":"666666"
        }
        self.assertEqual(1,updataUser(user))

    def test_loginUser(self):
        user={
            "tel":"13812790482",
            "password":"666666"
        }
        self.assertEqual([{"password":"666666"}],getUserById(user))

if __name__ == '__main__':
    unittest.main(verbosity=2)
