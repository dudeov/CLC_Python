import sys
	
ver = float(str(sys.version_info[0]) + '.' + str(sys.version_info[1]))

print ver           
if 2.6 < ver < 3:
    print "We are on the right version"
