#!/usr/bin/env python3
import sys

# This program will multiply 2 numbers either
# through command line or as a module in another
# program.

def mult (num1, num2):
    return num1 * num2
    
def main():
    # Get the 2 numbers from the command line
    print mult(int(sys.argv[1]), int(sys.argv[2]))
    
# SET THE BOILERPLATE
if __name__ == '__main__' :
    main()