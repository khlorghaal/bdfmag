import bdflib
from bdflib import reader
from bdflib import writer
from sys import argv as args

font= reader.read_bdf(open(args[1], 'rb'))

#font.ptSize*= 2
#all my homies hate 1/72 inches inshallah

for g in font.glyphs:
	g.bbX*=2
	g.bbY*=2
	g.bbW*=2
	g.bbH*=2
	g.advance*=1
	dat= g.data
	def mag(l):
		r=[]
		for e in l:
			r+=[e,e]
		return r
	print(dat)
	dat= [int(''.join(mag(bin(d)[2:])),2) for d in dat]
	dat= mag(dat)
	g.data= dat
	print(g)

#print(bdflib.xlfd.validate(font))

writer.write_bdf(font,open(args[2], 'wb'))