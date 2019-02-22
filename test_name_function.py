#!-_- coding=utf-8 !-_-

import unittest
import name_function

class NameTestCase(unittest.TestCase):
    #TODO 测试name_function.py
    def test_first_last_name(self):
        name = name_function.GetFormatName('conlin','lee')
        self.assertEqual(name , 'ConlinLee')

unittest.main()
