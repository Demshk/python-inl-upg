import json
import os

class CaesarCipher:

    def __init__(self, data_file="data.json"):
        self.data_file = data_file

    def encrypt(self, meddelande, key):
       resultat = ""
       for char in meddelande:
           if char.isalpha():
               base = ord('A') if char.isupper() else ord('a')
               resultat += chr((ord(char) - base + key) % 26 + base)
           else:
               resultat += char
       self.save_data("encrypt", meddelande, resultat, key)
       return resultat
    
    def decrypt(self, meddelande, key):
       resultat = ""
       for char in meddelande:
           if char.isalpha():
               base = ord('A') if char.isupper() else ord('a')
               resultat += chr((ord(char) - base - key) % 26 + base)
           else:
               resultat += char
       self.save_data("decrypt", meddelande, resultat, key)
       return resultat

    def save_data(self, att_göra, original, resultat, key):
       in_data = {
           "Att göra": att_göra,
           "original": original,
           "resultat": resultat,
           "key": key
        }
      
       if os.path.exists(self.data_file):
           with open(self.data_file, "r") as f:
               data = json.load(f)
       else:
           data = []
       data.append(in_data)
       with open(self.data_file, "w") as f:
           json.dump(data, f, indent=4)
           
    def load_data(self):
      if os.path.exists(self.data_file):
          with open(self.data_file, "r") as f:
              data = json.load(f)
              return data
      else:
          return []
    
    def show_saved_data(self):
       if os.path.exists(self.data_file):
           with open(self.data_file, "r") as f:
               data = json.load(f)
               if not data:
                   print("\nIngen sparad data ännu.")
               else:
                   print("\n--- Sparad data ---")
                   for in_data in data:
                       print(f"{in_data['Att göra'].capitalize()}: '{in_data['original']}' → '{in_data['resultat']}' (nyckel: {in_data['key']})")
       else:
           print("\nIngen sparad fil hittades.")









