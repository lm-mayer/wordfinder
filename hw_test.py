#test code for homework
#search abstracts for important research terms ("influenza" in this case)
#for rubric we need
    #decision, loop, and something to graph at the end




#implementation would be adding a .txt file (or a couple) to the GitHub, which we can read in here. If multiple, can add a loop through files, but might make our code too long

#this should read in a text file but it wasn't working for me earlier - can try later since technically this is in rubric
#path1=open(<filepath>)
#ab1=path1.read()

#paste text - replace with read text if we can get it to work. copy/pasted from https://pubmed.ncbi.nlm.nih.gov/38099051/
ab1 = "All European Union (EU) Member States (MSs) are required to implement surveillance for avian influenza (AI) in poultry and wild birds and (i) to notify the outbreaks, when relevant and (ii) to report the results to the responsible authority. In addition, Iceland, Norway, Switzerland and the United Kingdom (Northern Ireland) also implement ongoing surveillance programmes to monitor occurrences of avian influenza viruses (AIVs) in poultry and wild birds. EFSA received a mandate from the European Commission to collate, validate, analyse and summarise the data resulting from these AI surveillance programmes in an annual report. The present report summarises the results of the surveillance activities carried out in MSs, Iceland, Norway, Switzerland and the United Kingdom (Northern Ireland) in 2022. Overall, the 31 reporting countries (RCs) sampled 22,171 poultry establishments (PEs) during the 2022 surveillance activity: 18,490 PEs were sampled for serological testing and 3775 were sampled for virological testing. Some PEs were therefore sampled for both type of analytical methods. Out of the 18,490 PEs sampled for serological testing, 15 (0.08%) were seropositive for influenza A(H5) viruses. Out of the 3775 PEs sampled for virological testing, 74 PEs (1.96%) were positive to the virological assay for influenza A(H5) viruses. Seropositive PEs were found in four RCs (Belgium, Poland, Spain and Sweden) and as in previous years, the highest percentages of seropositive PEs were found in PEs raising breeding geese and waterfowl game birds. Out of these 15 seropositive PEs, 3 also tested positive by polymerase chain reaction (PCR) for influenza A (H5) viruses - 2 for highly pathogenic avian influenza virus (HPAIV) and 1 low pathogenic avian influenza (LPAI) (H5N3). In relation to the virological surveys, 10 RCs (32%) out of the 31 reported the detection of A (H5) viruses in 74 PEs, covering 12 different poultry categories. More specifically, 54 reported HPAIV A(H5N1), 17 HPAIV (H5N8), 2 AIV (H5N1) with unknown virus pathogenicity and 1 low pathogenic avian influenza (LPAI) (H5N3). Additionally, six PEs tested positive for undefined AIVs in three RCs. A total of 32,143 wild birds were sampled, with 4163 (12.95%) wild birds testing positive for HPAIVs by PCR, from 25 RCs. In contrast to previous years, out of the 4163 wild birds testing positive for HPAIv, subtype A(H5N1) virus was the main influenza A virus subtype identified among the wild bird testing positive for HPAIVs (3942; 95%). In addition, RCs also reported 984 wild birds testing positive for low pathogenic avian influenza (LPAI). Out of those, for 660 (67%) it was ascertained that the subtype was non-A(H5/H7); 260 (26%) wild birds tested positive for LPAIv of A(H5 or H7) subtypes and the remaining 64 (7%) LPAI viruses were belonging to other H-subtypes."

#convert full text to just words
words1=ab1.split()

#make function to count words in a list - expects variable 1 = list of words and variable 2 = key word to search and will output a count of times the keyword appeared
def count_words(wordlist,keyword):
    count = 0
    for i in range(len(wordlist)): #loop for rubric
        if wordlist[i] == keyword: #does this count as a decision? If not we can add something like if wordlist[i] < 3 : continue to skip short words
            count = count + 1
    return(count)
        
#test function
count_words(words1,"influenza")

#since we want a graph, we can get a few abstracts or look for a few words (ex. on this topic, we could check for multiple respiratory viruses) and graph counts of those words
#would also require arrays and libraries
#have not done any graphing, so we'll need to figure that out
#I'll have to look for old code, but theoretically can set up so that other users will be prompted to add their own keywords - would add some dev time but it's a little fancier

#tests are basically just we read the text and verify if words are present/not present