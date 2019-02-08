#!/usr/bin/python -tt

import urllib
import re

# Get web address from provided url
def wget(url):
    try:
        text = urllib.urlopen(url)
        #if text.info().gettype() == 'text/html':
        #    print text.read()
    except IOError:
        print 'Could not access web address ', url
    else:
        return text
        

text = wget('http://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names/100-most-popular-boys-names-so-far-in-2018')

pagetext = text.read()
beg = pagetext.find('<ol>')
end = pagetext.find('</ol>')
list = pagetext[beg:end]

for item in list:
    print item

# class Babynames:
#   def __init__(year):
#       boy = {}
#       girl = {}
#
#   year = None
