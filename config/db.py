from pymongo import MongoClient

connect = MongoClient("mongodb+srv://hadil:Fh0508@tptestunit.lygru.mongodb.net/tptestunit?retryWrites=true&w=majority")
connect["tptestunit"]["users"].find()

