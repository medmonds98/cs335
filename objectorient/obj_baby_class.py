#!/usr/bin/python -tt

# Initial web address for reference: https://www.babycentre.co.uk/popular-baby-names

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
    
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
    
    if summary:
        # Attempt to open the given url
        try:
            text = urllib.urlopen(args[0])
            
            if text.info().gettype() == 'text/html':
                
                # Grab each website link from the html of the given url
                addresses = []
                link_lists = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
                
                #Refine the search further
                for item in link_lists:
                    links = re.findall(r'<a href="(.*?)">', item)
                    
                    #add the grouped links to the adresses array
                    for link in links:
                        addresses.append(link)
                        
                print addresses
                
                # For each address, open the url and grab a list of babynames from that page
                
        except IOError:
            print "could not access web address"
            
    else:
        print 'unrecognized command \'', args[0], '\''
        sys.exit(1)
        
        
        
if __name__ == '__main__':
    main()