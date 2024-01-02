README for "wordfinder" program <br>
Description: Searching and Visualizing Terms in Text Documents <br>
Authors: Lisa Mayer and Peyton Tvrdy <br>
For: University of Vienna Data Stewardship Course, Module 2.7 <br>
Date: December 21st, 2023 <br>

----------------------------------------------------------------
# SUMMARY OF PROGRAM
----------------------------------------------------------------

This program takes text files, counts the frequency of certain words, and visualizes them on a plot. 
This program can read any text files and search for any word(s) or number(s) the user is looking for. 
The program can search for as many search terms as the user desires. The program accounts for non-
alphanumeric characters and capitalization. After searching the document for the requested terms, the 
program returns a total count for each search term. The program then optionally offers to visualize 
the word counts on a bar chart.


----------------------------------------------------------------
# TABLE OF CONTENTS
----------------------------------------------------------------

A. General Information
B. Quickstart & Use Cases
C. Sharing/Access & Policies Information
D. Data and Related File Overview
E. Data-Specific Information for: [dataset title here]
F. Update Log



----------------------------------------------------------------
# A. GENERAL INFORMATION
----------------------------------------------------------------

0. **Title of Program:** Wordfinder 
   

1. **Description of Program:** This program takes text files, counts the frequency of 
certain words, and visualizes them on a plot. This program can read any text files 
and search for any word(s) or number(s) the user is looking for. The program can 
search for as many search terms as the user desires. The program accounts for non-
alphanumeric characters and capitalization. After searching the document for the 
requested terms, the program returns a total count for each search term. The program 
then optionally offers to visualize the word counts on a plot.
   

2. **Github Links:** https://github.com/lm-mayer/wordfinder; 
       


3. **Authorship Information:** 
        Name: Lisa Mayer
           Institution: National Institutes of Health
           Email: lisa.mayer@nih.gov
		   ORCID: https://orcid.org/0000-0001-8499-3043
        Name: Peyton Tvrdy
           Institution: National Transportation Library. US Department of Transportation
           Email: peyton.tvrdy.ctr@dot.gov
		   ORCID: https://orcid.org/0000-0002-9720-4725
	   

4. Date of upload: December 20, 2023   

----------------------------------------------------------------
# B. Quickstart & Use Cases
----------------------------------------------------------------
**Quickstart**
1. Run wordfinder from any command line interface and specify path to text file for review.
```bash
python wordfinder.py input_file.txt
```

2. Specify search term(s) to match throughout the file. Separate multiple terms with commas. Counts of each will be returned in the command line interface.

3.  If you would like a visualization, respond "Y" when prompted. A bar chart of words and counts will pop up in a new window. If not, respont "N" to complete and close the program.

**Use Case: Quickly check if abstracts have relevant key words**
With the modern pace of publishing, staying up-to-date on any research area can be difficult and time consuming. Wordfinder mitigates this by allowing users to quickly check whether key words are present and get an overview of a publication's contents without reading the whole document. Then, the user can decide to only read publications where keywords are present to a certain degree, saving them time.

Note: follow along with this example with file in this repo 'Example Abstract Annual report on surveillance for avian influenza in poultry and wild birds in Member States of the European Union.txt'

For example, a researcher focused on zoonotic epidemiology is interested in influenza surveillance in wild animals around the world. They identified a publication that sounds relevant, but they want to make sure before reading since the PDF is 60 pages long! The researcher uses wordfinder:
 ```bash
 python wordfinder.py 'Example Abstract Annual report on surveillance for avian influenza in poultry and wild birds in Member States of the European Union.txt'

 Please enter the terms you would like to search this document for: 
 ```
They type keywords relevant to their research question. 

```bash
Please enter the terms you would like to search this document for: influenza, wild, surveillance, positive

=> Starting File Read: 'Example Abstract Annual report on surveillance for avian influenza in poultry and wild birds in Member States of the European Union.txt'

Term count:  {'influenza': 10, 'wild': 8, 'surveillance': 5, 'positive': 8}

=> Would you like a visualization of your terms' frequency? [Y/N]:
```
At this prompt, they answer "Y" and get this graph: <br>
![graph of flu word counts](https://github.com/lm-mayer/wordfinder/blob/main/flu_abstract_ex_graph.png)

The researcher is encouraged by the number of times their keywords occurred and verifies they do occur this much in the abstract. They read the article, which helps them understand more about their research landscape, and did not waste time reading something irrelevant.

----------------------------------------------------------------
# C. SHARING/ACCESS & POLICIES INFORMATION 
----------------------------------------------------------------

0. **Recommended citation for the program:**

Mayer, Lisa, and Peyton Tvrdy (2023). "Wordfinder". https://github.com/lm-mayer/wordfinder


1. Licenses/restrictions placed on the program: None
   

----------------------------------------------------------------
# D. DATA & RELATED FILE OVERVIEW
----------------------------------------------------------------

1. **File List for the wordfinder.zip collection**   
        
   A. Filename: README.md
          
        Short description: The file you are reading now. It is a brief description for the wordfinder program. 
         

   B. Filename: wordfinder.py
           
        Short description: The python program for the project. It searches the text for user defined words and creates visualizations.
			
      
   C. Filename: LICENSE
           
        Short description: This file contains license information for this program. 
			

   D. Filename: Example README Annual report on surveillance for avian influenza in poultry and wild birds in Member States of the European Union.txt
         
        Short description: Example of a README document used to test the program and demonstrate its use. The information in that file was obtained from: https://pubmed.ncbi.nlm.nih.gov/38099051/
         
 
   E. Filename: readme_SELDM_draft.txt
          
        Short description: Another example of a README document used to test the program and demonstrate its use. The information in that file was obtained from: https://doi.org/10.5066/P9Q1PP61
        

----------------------------------------------------------------
# E. DATA-SPECIFIC INFORMATION  
----------------------------------------------------------------

Required Programs: python v. 3.0 or above, standard text editor such as Notepad++


----------------------------------------------------------------
# F. UPDATE LOG
----------------------------------------------------------------

This README.md file was originally created on 2023-12-18 by Peyton Tvrdy and Lisa Mayer. 
<br>
2023-12-18: Original file created <br>
2023-12-21: File updated with examples and more details
2024-01-02: Slight changes made to file spacing
