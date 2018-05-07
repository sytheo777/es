f = open("english_bip39.txt","r")
lines = f.readlines()
f.close()

es = {}
es_li = {}

for li in lines:
	if li[0:2] in es:
		es[li[0:2]]+=1
		es_li[ li[0:2] ].append(li)
	else:
		es[ li[0:2] ] = 1
		es_li[ li[0:2] ] = []


for k in es.keys():
	print k, es[k] #es_li[ k ]