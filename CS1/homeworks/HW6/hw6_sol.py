# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 18:08:53 2022

@author: puniaa
"""
'''Overall Purpose of this program is toanalyze documents
based on the sophistication of word usage, frequently used words, and words that appear closely
together. This program can be used to analyze the style or even check if the two things are 
written by the same person
'''

#This function takes a file and returns a clean list based on the given criteria##
def parse_line(file):
    cleanlist = []
    f = open(file, encoding = "utf8")
    lines = f.read() 
    words = lines.split()
    for word in words:
        cleanword = ""
        for letter in word:
            if letter.isalpha():
                cleanword = cleanword+letter.lower()
        if len(cleanword) > 0:
            cleanlist.append(cleanword)
    f.close()
    return cleanlist

##computing the average of the length of words in a list##
def compute_avg(List):
    lengthlist = []
    for word in List:
        length  = len(word)
        lengthlist.append(length)
    avg = sum(lengthlist)/len(List)
    return "{:.2f}".format(avg)


## finding the ration of distinct words to total words in a List## 
def ratiodiscwords(List):
    discset = set(List)
    ratio = len(discset)/len(List)    
    return "{:.3f}".format(ratio)
    

#making the dictionary out of the length of the words and the words##
def make_dictionary(List):
    lengthlist = []
    worddict = {}
    for word in List:
        length = len(word)
        lengthlist.append(length)
        if length not in worddict.keys():
           worddict[length] = []    
        worddict[length] += [word]
    return worddict

##formatting and printing out that dictionary##
def wordset(List):
    lengthlist = []
    worddict = {}
    for word in List:
        length = len(word)
        lengthlist.append(length)
        if length not in worddict.keys():
           worddict[length] = []    
        worddict[length] += [word]
        worddict[length] = set(worddict[length])
        worddict[length] = list(worddict[length])
        
        worddict[length].sort()
        maxlength = max(lengthlist)
    for i in range(1,maxlength+1):
        if i not in worddict.keys():           
            print("{:>4}:   0:".format(i))
        else: 
            print("{:>4}:{:>4}:".format(i,len(worddict[i])),end = "")
            if len(worddict[i]) < 6:    
                for word in worddict[i]:
                    print(" {}".format(word),end ="") 
                print()
            else:
                for word in worddict[i][:3]:
                    print(" {}".format(word),end ="")
                print(" ...",end = "")
                for word in worddict[i][-3:]:
                    print(" {}".format(word),end ="")
                print()


##calculating the total word pair in a given list based on a max seperation
##given
def totalwordpairs(List,max_sep):
    List = list(List)
    temp_list = []
    for i in range(len(List)):
        for j in range(i+1,max_sep+1+i):
            if j < len(List):
                tup = tuple((List[i],List[j]))
                tup = sorted(tup)
                tup = tuple(tup)
                temp_list.append(tup)
    return temp_list
    
##finding the distinct word pairs from the total words and formatting it#   
def distinctpair(List,max_sep):
    List1 = list(set(totalwordpairs(List,max_sep)))
    List1.sort()
    print(" ",len(List1),"distinct pairs")
    if len(List1) <= 5:
        for tup in List1:
            print("  ",end="")
            print(" ".join(list(tup)))
    else: 
        for tup in List1[:5]: 
            print(" ",end="")
            print(" ",end="")
            print(" ".join(list(tup)))
        print("  ...")
        for tup in List1[-5:]:
            print(" ",end="")
            print(" ",end="")
            print(" ".join(list(tup)))
    #print(" ".join(List1[:5]))
    return List1 

##ratio to the distinct pairs to total pairs##
def ratiopairs(List,max_sep):
    List1 = totalwordpairs(List,max_sep)
    List2 = list(set(totalwordpairs(List,max_sep)))
    return len(List2)/len(List1)   
 
##Jaccard Similarity based on two lists##
def word_use_similar(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(set(list1)) + len(set(list2))) - intersection
    n = (float(intersection))/ union
    return n
   
## word length with the Jaccard similarity##
def compare_length_word(dic1,dic2):
    lengthlist = []    
    for length in dic1:
        lengthlist.append(length)
    for length1 in dic2:
        lengthlist.append(length1)
    maxlength = max(lengthlist)
    for i in range(1,maxlength+1):       
        if i in dic1.keys() and i in dic2.keys():
            list1 = dic1[i]
            list2 = dic2[i]
            numbsimilar = word_use_similar(list1, list2)
            print("{:>4}: {:.4f}".format(i,numbsimilar),end = "")
            print()
        else:
            print("{:>4}: 0.0000".format(i)) 
 
##Jaccard Similarity with the list of distinct words pairs and total word pairs#
def wordpairsimilar(onelist,twolist,max_sep):
    List1 = list(set(totalwordpairs(onelist,max_sep)))
    List2 = list(set(totalwordpairs(twolist,max_sep)))
    simalar = word_use_similar(List1, List2)
    return simalar
      
if __name__ == "__main__":
    ##INPUT STATMENTS##
    file1 = input("Enter the first file to analyze and compare ==> ").strip()
    print(file1)
    file2 = input("Enter the second file to analyze and compare ==> ").strip()
    print(file2)
    max_sep = int(input("Enter the maximum separation between words in a pair ==> "))
    print(max_sep)
    
    
    
    onelist = parse_line(file1)
    twolist = parse_line(file2)
    stopset= set(parse_line("stop.txt"))
    ##taking words out that are in the stop set from file 1##
    for word in stopset:
        while word in onelist:
            onelist.remove(word)
    ##taking words out that are in the stop set from file 2##
    for word in stopset:
        while word in twolist:
            twolist.remove(word)
    
    ##computing average for both files##
    oneavg = compute_avg(onelist)
    twoavg = compute_avg(twolist)
   
    ##computing distinct words##
    onediscratio = ratiodiscwords(onelist)
    twodiscratio = ratiodiscwords(twolist)
     
    dic1 = make_dictionary(onelist)
    dic2 = make_dictionary(twolist)
   
    numb = wordpairsimilar(onelist,twolist,max_sep)

    ####### PRINT STATEMENTS #######
    print()
    ##PRINT STATEMENT FOR THE FIRST FILE##
    print("Evaluating document {}".format(file1))
    print("1. Average word length:",oneavg)
    print("2. Ratio of distinct words to total words:",onediscratio)
    print("3. Word sets for document {}:".format(file1))
    wordset(onelist)   
    print("4. Word pairs for document",file1)
    distinctpair(onelist,max_sep)
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratiopairs(onelist,max_sep)))
    print()
    
    ##PRINT STATEMENT FOR THE SECOND FILE##
    print("Evaluating document {}".format(file2))
    print("1. Average word length:",twoavg)
    print("2. Ratio of distinct words to total words:",twodiscratio)
    print("3. Word sets for document {}:".format(file2))
    wordset(twolist)
    print("4. Word pairs for document",file2)
    distinctpair(twolist,max_sep)
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(ratiopairs(twolist,max_sep)))
    print()
    print("Summary comparison")
    
    #PRINTING SUMMARY COMPARSION#
    if oneavg > twoavg:
        print("1. {} on average uses longer words than {}".format(file1,file2))
    else:
        print("1. {} on average uses longer words than {}".format(file2,file1))
    number = round(word_use_similar(onelist, twolist),3)
    print("2. Overall word use similarity: {}".format(number))
    print("3. Word use similarity by length:")
    compare_length_word(dic1,dic2)
    print("4. Word pair similarity: {:.4f}".format(numb))

    
    
    
    
    
    