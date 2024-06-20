import marshal
s='''
a=10
b=20
print("mul=",a*b)
    '''
code=compile(s,"s","exec")
fp=open("marshal.txt","wb")
marshal.dump(code,fp)
fp.close()