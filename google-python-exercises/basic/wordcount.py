#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_words(filename):
  # Get the word counts
  word_counts = count_words(filename)

  # print the sorted dictionary along with the appropriate word counts
  for item in sorted(word_counts.keys()):
    print item + ' ' + str(word_counts[item])
  
def print_top(filename):
  
  def sortFunc(tuples):
    return tuples[-1]
  
  # Get the word counts dict as a list of tuples, sorted by word count  
  word_counts = sorted(count_words(filename).items(), key=sortFunc, reverse=True)
  i = 0
  
  # Print the top 20 words with highest word counts
  for i in range(20):
    if i < len(word_counts):
      print str(i+1) + '. ' + word_counts[i][0]


def count_words(filename):
  file = open(filename, 'r')
  words = []
  words_counts = {}
  
  # Get the words from the file, split by the whitespace
  for line in file:
    words += line.split()
    
    
  # Iterate through each word in the list, adding each new word
  # and count of that word to the dictionary, make sure to format
  # each word to be lower case
  for item in words:
    item = (item.strip('.,!?')).lower()
    
    if item in words_counts:
      words_counts[item] += 1
    else:
      words_counts[item] = 1
      
  return words_counts


###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
