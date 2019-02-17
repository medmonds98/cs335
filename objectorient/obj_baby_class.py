#!/usr/bin/python -tt

# Initial web address for reference: https://www.babycentre.co.uk/popular-baby-names

import urllib
import re
import sys

class Babynames :
    year = None
    gender = ''
    names = {}
    
    def __init__(self, url):
        self.url = url
        
    def build_names(self):
        # strip the year and get a gender (if there is one) from the url,
        # year is last 4 digits of each link
        self.year = self.url[-4:]
        
        # gender can be found in the link
        if bool(re.search(r'boy', self.url)):
            self.gender = 'Boy'
            
        elif bool(re.search(r'girl', self.url)):
            self.gender = 'Girl'
        
        # build the list of names from the url:
        pagetext = urllib.urlopen(self.url).read()
        
        # first find where the <ol> and </ol> are in text
        ol_lists = re.findall(r'<ol.*?/ol>', pagetext, re.DOTALL)
        
        # then grab the names from the ordered lists
        if len(ol_lists) != 0:
            
            i = 1
            for list in ol_lists:
                matches = re.findall(r'<a.*?>(\w*?)</a>', list, re.DOTALL)
                
                if len(matches) == 0:
                    matches = re.findall(r'<li> (\w*?) </li>', list)
                
                for match in matches:
                    self.names[i] = match
                    i += 1
                
        # if the <ol>...</ol> patterns arent working, try a different pattern
        else:
            i = 1
            matches = re.findall(r'<a href="[\w/]*?">(\w*?)</a>', pagetext, re.DOTALL)
            
            for match in matches:
                self.names[i] = match
                i += 1
        
        
    def output(self, file):
        
        # Write the gender, year, and names to the given file
        f = open(file, 'w')
        
        # Adjust for the spacing if there is no gender
        if len(self.gender) > 0:
            f.write('Popular ' + self.gender + ' Baby Names in ' + self.year)
        else:
            f.write('Popular Baby Names in ' + self.year)
            
        f.write('\n' + '-----------------------------' + '\n')
        
        for item in self.names.keys():
            f.write( str(item) + ". " + self.names[item] + '\n')
    
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
                        babynames_list.append( Babynames(root_url.group() + link) )
                    
                #build the name lists of each object, then write them to a unique file
                for item in babynames_list:
                    item.build_names()
                    item.output(item.gender + 'babynames' + item.year + '.txt')
                
        except IOError:
            print "could not access web address"
            
    else:
        print 'unrecognized command \'', args[0], '\''
        sys.exit(1)
        
        
        
if __name__ == '__main__':
    main()