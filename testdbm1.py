import dbm

db = dbm.open("dbm1.db", "r")
print(list(dbm.keys()))
