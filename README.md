I den här uppgiften har jag skapat ett program som använder Caesar cipher för att kryptera och dekryptera text. När programmet startar får användaren skapa ett lösenord och det lösenordet behövs senare om man vill dekryptera något man själv har krypterat tidigare.
Programmet sparar även alla krypteringar i en JSON-fil, så man kan gå tillbaka och se sin historik när man vill.
Jag har också gjort två tester med hjälp av Pythons inbyggda testmodul unittest. För att köra testerna går man in i mappen “test” och kör filen test_ceasar.py.

Det som va svårast med programmet va själva krypteringen. Jag hade svårigheter med att det skulle funka med både stora och små bokstäver utan att behöva skriva ut allt i små eller stora bokstäver i terminalen. Bokstäverna Å, Ä och Ö fungerar dock fortfarande inte då det endast går att använda de engelska alfabetet.
När jag väl fick det att fungera va nästa problem att knyta ihop allting i main så att allt fungerar som det ska. Det tog lite tid att förstå hur krypteringen, dekrypteringen, JSON och klassen skulle sammarbeta utan att det blir rörigt.
Jag testade mycket steg för steg och på vägen lärde jag mig hur viktigt det är att ha väl strukturerad och tydlig kod. 
