#fa=None
#fb=None
#fc=None
#fd=None
#fs=None
#fl=None

def es_ro(te):
	for wo in te.split(" "):
		#if wo="ap": fa=True
		#if wo="ba": fb=True
		#if wo="ca": fc=True
		#if wo="da": fd=True
		#if wo="sa": fs=True

		print wo[0:2], " ",


f = open("blox.txt", "r")
l = f.readlines()
f.close

for	 ll in l:
	#w = "".join(l)
	print es_ro(ll)