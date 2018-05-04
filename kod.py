import hashlib
a=open("yazi.txt")
x=a.read()
a.close()
y=""
n=int(input("Yazi girin"))
for i in range(0,n):
	x=hashlib.md5(x.encode('utf-8')).hexdigest()
	y=y+x[7]
print("hex karsilik: ",y)
print("decimal karsilik: ",int(y,16))
