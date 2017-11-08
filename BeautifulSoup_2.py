import urllib2
#import argparse
from optparse import OptionParser
from bs4 import BeautifulSoup

USAGE = "python BeautifulSoup.py [output file name]"


parser.add_argument("out_file","--output_file")

args = parser.parse_args()

def getTile(url):
    try:
        html  = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print "1",e
        return None

    try:
        baObj = BeautifulSoup(html.read(),"lxml")
        title = baObj.title
    except AttributeError as e:
        print "2",e
        return None
    return title

title = getTile("http://www.baidu.com")
if title == None:
    print "Title not exist"
else:
    print "Title:",title

