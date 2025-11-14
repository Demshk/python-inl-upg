import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from app.ceasar_cipher import CaesarCipher

class TestCaesarCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = CaesarCipher(data_file="test_data.json")

    def test_encrypt(self):
        resultat = self.cipher.encrypt("ABC", 3)
        self.assertEqual(resultat, "DEF")

    def test_decrypt(self):
        resultat = self.cipher.decrypt("DEF", 3)
        self.assertEqual(resultat, "ABC")

if __name__ == "__main__":
    unittest.main()
