from bs4 import BeautifulSoup
import urllib2

try:
    html = urllib2.urlopen("http://www.baidiu.com")
except  urllib2.URLError as e:
    print e

bsObj = BeautifulSoup(html.read())

with open("Source_code.txt","w")  as f:
    f.write(str(bsObj))
print "bsObj",bsObj


