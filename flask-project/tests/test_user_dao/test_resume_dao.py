import unittest
from app.dao.resume_dao import *

class TestResumeDao(unittest.TestCase):
    # def test_addResumeBase(self):
    #     resume = {
    #         "title": "china resume",
    #         "name": "桑宇林",
    #         "birth":"1991-1-1"
    #     }
    #     self.assertEqual(1,addResumeBase(resume))

    # def test_addResumejob(self):
    #     resume = {
    #         "cname": "apple",
    #         "pname": "manage",
    #         "resume_basic_id":'5'
    #     }
    #     self.assertEqual(1,addResumejob(resume))

    # def test_addResumeedu(self):
    #     resume = {
    #         "school": "北京",
    #         "resume_basic_id":'5'
    #     }
    #     self.assertEqual(1,addResumeedu(resume))

    def test_updataResume(self):
        resume_updata = {
            "table": "resume_basic",
            "term":'sex',
            "new":'1',
            "id":'5'
        }
        self.assertEqual(1,updataResume(resume_updata))

if __name__ == '__main__':
    unittest.main(verbosity=2)