##import urllib2
##import urllib
##
##f=urllib2.urlopen('httt://www.python.org')
##
##print(f.read(100))
##
##response=urllib.urlopen('httt://google.com')
##for line in response:
##    print line.rstrip()


import urllib2
import urllib

f=urllib2.urlopen('httt://www.python.org')

print(f.read(100))

response=urllib.urlopen('httt://google.com')
for line in response:
    print line.rstrip()
