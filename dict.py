dic={1:"one",2:"two"}
print(dic)
print("first number is",dic[1])

print(len(dic))
dic1=dic.copy()
print(dic1)
print(dic.get(2))
print(dic.values())
print(dic.items())
dic.update({1:"three"})
print(dic)
dic.pop(1)
print(dic)
dic.clear()
print(dic)