
fname = raw_input("Enter filename:\n")

try:
	fobj = open(fname,'r')
except IOError, e:
	print " *** file open error:",e
else:
	for eachline in fobj:
		print eachline
	fobj.close()
