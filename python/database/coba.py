import dbm
db = dbm.open("D:\\Projek Programmer\\Python_VSCode\\phonebook", "c")

db["ahmad"] = "08152300182"
db["hari"] = "08762767236"

db.sync()