
from ceasar_cipher import CaesarCipher

def main():
    cipher = CaesarCipher()

    sparad_data = cipher.load_data()
    if sparad_data:
        print("\nTidigare krypteringar:")
        for entry in sparad_data:
            print(f"{entry['original']} → {entry['resultat']} (key: {entry['key']})")
    else:
        print("\nInga tidgare krypteringar sparade.")


    resultat = ""
    key = 0
    lösenord = input("Skapa ett lösenord: ") 
    
    while True:
        print("\n--- Caesar Cipher ---")
        lösenord
        if resultat:
          print(f"Din krypterade text: {resultat}")
        print("1. Kryptera meddelande")
        print("2. Dekryptera meddelande")
        print("3. Visa sparad data")
        print("4. Avsluta")

        val = input("Välj ett alternativ: ")

        if val == "1":
            meddelande = input("Skriv text att kryptera: ")

            try:
                key = int(input("Ange nyckel (tex 3): "))
                resultat = cipher.encrypt(meddelande, key)
                print(f"Krypterat meddelande {resultat}")

            except ValueError:
                print("Fel: nyckeln måste vara ett heltal!")


        elif val == "2":
          
          if resultat == "":
              print("Du har inte krypterat något ännu!")

          else:
              försök = input("Skriv in lösenordet för att dekryptera: ") 

              if försök == lösenord:
                  resultat = cipher.decrypt(resultat, key)
                  print("Dekrypterat meddelande:", resultat)

              else:
                  print("Fel lösenord! Du får inte dekryptera meddelandet.")

        elif val == "3":
           cipher.show_saved_data()
             
            
        elif val == "4":
            print("Avslutar programmet...")
            break

        else:
            print("Ogiltigt val, försök igen.")

if __name__ == "__main__":
    main()












