#!/usr/bin/python -tt

import urllib
import re
import sys

class Babynames :
    def __init__(self, year):
        self.year = year
        
    

def main():
    
    # Manage console commands
    args = sys.argv[1:]
    
    if not args:
        print 'usage: [--summaryfile] URL'
        sys.exit(1)
    
    if args[0] == '--summaryfile':
        del args[0]
    
    # Attempt to open the given url
    try:
        text = urllib.urlopen(args[0])
        
        # Break the url up into different links
        if text.info().gettype() == 'text/html':
            pages = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
            for page in pages:
                print page
            
    except IOError:
        print "could not access web address"
        
if __name__ == '__main__':
    main()