#!/usr/bin/python -tt

# Initial web address for reference: https://www.babycentre.co.uk/popular-baby-names

import urllib
import re
import sys

class Babynames :
    year = None
    names = {}
    
    def __init__(self, url):
        # upon instantiation, set t
        self.url = url
        
    def build_names(self):
        # strip the year from the url,
        # year is last 4 digits of each link
        self.year = self.url[-4:]
        
        # build the list of names from the url
        pagetext = urllib.urlopen(self.url)
        matches = re.findall(r'<a href="[\w/]*?">(\w*?)</a><span class="plusMinus">', pagetext.read())
        
        i = 1
        for match in matches:
            self.names[i] = match
            i += 1
        
        
    def output(self):
        print self.names, '\n'
        #print 'Popular Baby Names in ', self.year
        #print '---------------------------'
        
        #for item in self.names.keys().sort():
        #    print item, ". ", self.names[item]
        
    
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
        
        # Attempt to open the given url and find the baby name links
        try:
            text = urllib.urlopen(args[0])
            
            if text.info().gettype() == 'text/html':
                
                # Grab each website link from the html of the given url
                link_lists = re.findall(r'\d+\sto\s\d+</h2><ul>(.*?)</ul>', text.read())
                
                # get the root url for the page from args[0]
                root_url = re.search(r'https://([\w.]*)', args[0])
                babynames_list = []
                
                #Refine the search further
                for item in link_lists:
                    links = re.findall(r'<a href="(.*?)">', item)
                    
                    #instantiate a Babynames obj with each full url, and put them in a list
                    for link in links:
                        bn = Babynames(root_url.group() + link)
                        bn.build_names()
                        babynames_list.append( bn )
                
                # Print all babynames to different files
                for item in babynames_list:
                    print id(item)
                    item.output()
                
        except IOError:
            print "could not access web address"
            
    else:
        print 'unrecognized command \'', args[0], '\''
        sys.exit(1)
        
        
        
if __name__ == '__main__':
    main()