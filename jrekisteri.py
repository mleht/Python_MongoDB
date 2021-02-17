import pymongo
from bson.objectid import ObjectId
from pprint import pprint

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
database = myclient["register"]
collection = database["members"]

collectionlist = database.list_collection_names()
if "members" in collectionlist:
    pass
else:
    first_member = { "Etunimi": "Admin", "Sukunimi": "", "Osoite" : "", "Postinumero" : "", "Puhelin" : "", "Sähköposti" : "", "JäsenyydenAlkuPvm" : "" }
    x = collection.insert_one(first_member)


print()
print("---------------------------------")
print("Tervetuloa jäsenrekisteriin!")
print("---------------------------------")
print()


while True:
    try:
        print()
        print("(1) Lue jäsenrekisterin sisältö\n(2) Lisää jäsen\n(3) Muokkaa tietoja\n(4) Poista jäsen\n(5) Lopeta")
        valinta=int(input("Mitä haluat tehdä?: "))
    
        if valinta == 1:
            print()
            cursor = collection.find({})
            for document in cursor: 
                pprint(document) #printpretty
                print()
           
            
        elif valinta == 2:
            print()
            enimi = input("Anna etunimi: ")
            snimi = input("Anna sukunimi: ")
            osoite= input("Anna osoite: ")
            pnumero = input("Anna postinumero: ")
            puh = input("Anna puhelinumero: ")
            email = input("Anna sähköposti: ")
            pvm = input("Anna liittymispäivä pv.kk.vvvv ")
            lisattava = { "Etunimi": enimi, "Sukunimi": snimi, "Osoite" : osoite, "Postinumero" : pnumero, "Puhelin" : puh, "Sähköposti" : email, "JäsenyydenAlkuPvm" : pvm }
            x = collection.insert_one(lisattava)
            print()
            print("Uusi jäsen lisätty tietokantaan.")

        elif valinta == 3:
            print()
            print("Päivitys tehdään vain jos antamasi käyttäjän objectid sekä kentän otsikko löytyvät tietokannasta.")
            print()
            paivitettava_kayttaja = input("Anna päivitettävän jäsenen objectid: ")
            paivitettava_kentta = input("Anna päivitettävän kentän otsikko : ")
            paivitettava_kentta = (paivitettava_kentta.capitalize()) # Kenttien ensimmäinen kirjain on isolla
            uusi_tieto = input("Anna päivitettävän kentän uusi sisältö: ")
            try:
                myquery = { "_id": ObjectId(paivitettava_kayttaja), paivitettava_kentta : {"$exists": True} }
                newvalues = { "$set": { paivitettava_kentta: uusi_tieto } }
                collection.update_one(myquery, newvalues)
            except:
                print()
                print("Virhe päivitettäessa. Tarkasta tiedot.")    
            
        elif valinta == 4:
            print()
            poistettava = input("Anna poistettavan jäsenen objectid: ")
            try:
                myquery = { "_id": ObjectId(poistettava) }
                collection.delete_one(myquery)
                print()
                print(f"Jäsen {poistettava} poistettu tietokannasta.")
            except:
                print()
                print("Virhe poistettaessa. Tarkasta objectid.")
            
        elif valinta == 5:
            print()
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta.")
    except:
        continue        





