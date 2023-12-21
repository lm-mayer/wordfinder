#Title: Searching and Visualizing Terms in Text Documents
#Authors: Lisa Mayer and Peyton Tvrdy
#For: University of Vienna Data Stewardship Course, Module 2.7
#Date: December 20th, 2023
#For more information on this script and how to use it, please read the document "README.md"

from fileinput import filename
import sys

def alphanumeric(string):
    return "".join(ch for ch in string if ch.isalnum())

def main():

    if len(sys.argv) != 2:
        print()
        print("Error: Please provide a filename", file=sys.stderr)
        sys.exit(1)

    print()        
    term_dict = {alphanumeric(str(item).lower()): 0 for item in input("Please enter the terms you would like to search this document for: ").split()}
    
    print("\n=> Starting File Read: %s\n" % sys.argv[1])
    fp = open(sys.argv[1], 'r', encoding='utf-8')
    
    with fp:
        for line in fp.readlines():
            words = line.lower().split()
            for word in words:
                cleaned_word = alphanumeric(word)
                if cleaned_word in term_dict.keys():
                     term_dict[cleaned_word] += 1
    
    fp.close()
    print("Term count: ", term_dict)
    should_continue = input("\n=> Would you like a visualization of your terms' frequency? [y/N]: ").upper() == 'Y'

    if not should_continue:
        print("=> Done !")
        sys.exit(0)

    print("\n=> Preparing Request")
    
if __name__ == '__main__':
	main()
