#Title: Searching and Visualizing Terms in Text Documents
#Authors: Lisa Mayer and Peyton Tvrdy
#For: University of Vienna Data Stewardship Course, Module 2.7
#Date: December 21th, 2023
#For more information on this script and how to use it, please read the document "README.md"

from fileinput import filename
import sys
import matplotlib.pyplot as plt 

def alphanumeric(string):
    return "".join(ch for ch in string if ch.isalnum())

def main(input_file): #added explict variable in place of sys.argv[1], but could roll back

    if len(sys.argv) != 2:
        print()
        print("Error: Please provide a filename", file=sys.stderr)
        sys.exit(1)

    print()        
    term_dict = {alphanumeric(str(item).lower()): 0 for item in input("Please enter the terms you would like to search this document for: ").split()}
    
    print("\n=> Starting File Read: %s\n" % input_file)
    fp = open(input_file, 'r', encoding='utf-8')
    
    #read lines and store word counts in term_dict
    with fp:
        for line in fp.readlines():
            words = line.lower().split()
            for word in words:
                cleaned_word = alphanumeric(word)
                if cleaned_word in term_dict.keys():
                     term_dict[cleaned_word] += 1
    
    fp.close()
    print("Term count: ", term_dict)
    
    #prompt for visualization
    should_continue = input("\n=> Would you like a visualization of your terms' frequency? [Y/N]: ").upper() == 'Y'

    if not should_continue:
        print("=> Done !")
        sys.exit(0)

    print("\n=> Preparing Request")

    #make visual if yes - bar chart of word counts
    words = list(term_dict.keys())
    counts = list(term_dict.values())
    
    plt.bar(words, counts)
    plt.xlabel('Words')
    plt.ylabel('Count')
    plt.title('Word Frequency')

    plt.show()


if __name__ == '__main__':
    input_file=sys.argv[1]
    main(input_file)
