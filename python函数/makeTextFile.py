import os
ls = os.linesep


fname = raw_input("input file name")

#get filename
while True:
    if os.path.exists(fname):
        print "ERROR: '%s' already exists" % fname
    else:
      break

all = []

print "\n ENTER lines ('.' by itself to quit)\n"

while True:
 	entry = raw_input('>')
 	if entry == '.':
 		break
 	else:
 		all.append(entry)
fobj = open(fname,'w')
fobj.writelines(['%s%s' %(x,ls) for x in all])
fobj.close()
print 'DONE'