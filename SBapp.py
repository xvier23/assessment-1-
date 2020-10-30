'''
Simple Billing System

Created on Oct 6, 2020

@author: tchan
'''
import fileinput
import sys

def displayFile(datafile):
    for line in fileinput.input(datafile):
        sys.stdout.write(line)

    
def main():
    instructions = """\nEnter one of the following:
        1 to print the contents of input transaction file
        2 to print all valid input transaction data
        3 to enter adjustment transaction
        4 to print customer report
        Q to end \n"""
    
       
    while True:
        sys.stdout.write(instructions) 
        sys.stdout.flush()      
        choice = input( "Enter 1 to 4 " ) 

        if choice == "1":
            displayFile(sys.argv[1])
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "Q":
            break

    print ("End Simple Billing System")

if __name__ == "__main__":
    
    displayFile(sys.argv[1])
    main()
