import unittest
from translator import frenchToEnglish, englishToFrench
class test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertEqual(englishToFrench(" ")," ")


class test_frenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish(" ")," ")
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main() 