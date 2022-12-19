# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:45:19 2022

@author: puniaa
In this program, we are making an autocorrect. We have input words and we are finding if 
there are words there possibly can be
"""
# creating python dictionary to english dictionary
def english_dictionary(file):
  f = open(file)
  line = f.read()
  line = line.split("\n")
  #print(line[0]) # word and it's frequency
  line.pop(-1)
  words = dict()
  for pair in line: 
      pairs = pair.split(",")
      words[pairs[0].strip()] = pairs[1]
  return words
# creating a keyboard dictionary  
def keyboard_dict(file):
    f1 = open(file)
    line1 = f1.read()
    line1 = line1.split("\n")
    line1.pop(-1)
    #print(line1)
    letters = dict()
    for l in line1:
        List = l.split()
        letters[List[0]] = List[1:]
    return letters
      
#dropping a letter  
def drop(word,dictionary):
    drop_set= set()   
    for i in range(len(word)):
       new_word = word[:i] + word[i+1:] 
       if new_word in dictionary: 
           drop_set.add(new_word)
    return drop_set
#inserting a letter
def insert(word,dictionary):
    insert_set = set()
    alpha_list = ["a","b","c","d","e","f","g","h","i","j",
                  "k","l","m","n","o","p","q","r","s","t",
                  "u","v","w","x","y","z"]   
    for i in range(len(word)+1):
        for alpha in alpha_list:
            temp_word = word[:i] + alpha + word[i:]
            if temp_word in dictionary:
                insert_set.add(temp_word)
    return insert_set
    
#swaping letters next to each other    
def swap(word,dictionary):
    swap_set = set()    
    word = word.strip()
    for i in range(len(word)-1):
        temp_word = list(word)
        #print(temp_word)
        temp_word[i],temp_word[i+1] = temp_word[i+1],temp_word[i]
        temp_word = "".join(temp_word)
        if temp_word in dictionary:
            swap_set.add(temp_word)
    return swap_set

#swapping letters within the keyboard dictionary#
def replace(word,engdict,kbdict):
    replace_set = set()    
    for i in range(len(word)):
        for alpha in kbdict[word[i]]:
            temp_word = word[:i] + alpha + word[i+1:]
            if temp_word in engdict:
                replace_set.add(temp_word)
    return replace_set

if __name__ == "__main__":
    file = input("Dictionary file => ").strip()
    print(file)
    file2 = input("Input file => ").strip()
    print(file2)
    file1 = input("Keyboard file => ").strip()
    print(file1)

    ## opening and turning input words into a list##
    f2 = open(file2)
    line2 = f2.read()
    line2 = line2.split("\n")
    line2.pop(-1)
    #print(line2)
    ############################################
    
    ##printing and formatting##
    eng_dict = english_dictionary(file)
    keyb_dict = keyboard_dict(file1)
    for orgword in line2:
        orgword = orgword.strip()
        if orgword in eng_dict:
            print("{:>15}".format(orgword),"-> FOUND")
        else:
            dset = drop(orgword,eng_dict)
            iset = insert(orgword,eng_dict)
            sset = swap(orgword,eng_dict)
            rset = replace(orgword,eng_dict,keyb_dict)
            large_set = dset.union(iset)
            large_set = large_set.union(sset)
            large_set = list(large_set.union(rset))
            large_list = []
            for word in large_set:
                if word in eng_dict: 
                    newt = (eng_dict[word],word)
                    large_list.append(newt)
            large_list.sort(reverse = True)
            
            if len(large_list) == 0:
                print("{:>15}".format(orgword),"-> NOT FOUND")
            else: 
                print("{:>15}".format(orgword),"-> FOUND {:>2}:  ".format(len(large_list)),end = "")
                if len(large_list) <= 3:
                    for item in range(len(large_list)-1):
                        print(large_list[item][1], end = " ")
                    print(large_list[-1][1])
                else: 
                    for item in range(2):
                        print(large_list[item][1], end = " ")
                    print(large_list[2][1])
                
           
            
            
            
    
    
    
