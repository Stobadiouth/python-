import unittest
from tests.test_user_dao.test_user_dao import TestUserDao

if __name__ == '__main__':
    suite=unittest.TestSuite
    tests=[TestUserDao("test_adduser"), TestUserDao("test_updataUser")]
    suite.addTests(tests)
    # suite.addTest(TestUserDao("test_adduser"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)