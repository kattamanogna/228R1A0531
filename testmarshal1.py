import marshal
fp=open("marshal1.txt","rb")
d=marshal.load(fp)
exec(d)