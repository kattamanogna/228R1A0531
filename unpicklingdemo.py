import pickle
fp=open("pickle1.txt","rb")
unp=pickle.load(fp)
print(unp)
fp.close()