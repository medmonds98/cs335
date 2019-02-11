#!/usr/bin/python -tt

import urllib
import re

class Babynames:
   def __init__(self, year, url):
       self.year = year
       self.names_list = self._build_names(url)

   def _build_names(self, url):
       text = self._wget(url)
       
       pagetext = text.read()
       beg = pagetext.find('<p><ol>')
       end = pagetext.find('</ol>\n<div><br />')
       
       matches = re.findall(r'<strong>(\w*)</strong>', pagetext[beg:end])

       return matches
   
   def output(self):
       print str(self.year)
       for item in self.names_list:
           print item
  
   # Get web address from provided url
   def _wget(self, url):
       try:
           text = urllib.urlopen(url)
       except IOError:
           print 'Could not access web address ', url
       else:
           return text
        

#text = wget('http://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names/100-most-popular-boys-names-so-far-in-2018')

bbynames = Babynames(2018, 'http://www.bounty.com/pregnancy-and-birth/baby-names/top-baby-names/100-most-popular-boys-names-so-far-in-2018')
bbynames.output()