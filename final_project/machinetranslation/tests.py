import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french("Red"), "Rouge") # test one.
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test two.
        self.assertNotEqual(english_to_french("Happry"),"Heureuse")  # test not match.

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english("Rouge"), "Red") # test one.
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test two.
        self.assertNotEqual(french_to_english("Heureuse"),"Happry")  # test not match.

unittest.main()
