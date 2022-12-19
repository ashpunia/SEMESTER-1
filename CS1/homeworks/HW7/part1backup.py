# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 19:45:19 2022

@author: puniaa
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
        
def drop(word,dictionary):
    drop_set= set()   
    for i in range(len(word)):
       new_word = word[:i] + word[i+1:] 
       if new_word in dictionary: 
           drop_set.add(new_word)
    return drop_set

def insert(word,dictionary):
    insert_set = set()
    alpha_list = ["a","b","c","d","e","f","g","h","i","j",
                  "k","l","m","n","o","p","q","r","s","t",
                  "u","v","w","x","y","z"]   
    for i in range(len(word)):
        for alpha in alpha_list:
            temp_word = word[:i] + alpha + word[i:]
            if temp_word in dictionary:
                insert_set.add(temp_word)
    return insert_set
    
    
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
    file2 = input("Input file => ").strip()
    file1 = input("Keyboard file => ").strip()

    ## opening and turning input words into a list##
    f2 = open(file2)
    line2 = f2.read()
    line2 = line2.split("\n")
    line2.pop(-1)
    #print(line2)
    ############################################
    
    eng_dict = english_dictionary(file)
    keyb_dict = keyboard_dict(file1)
    
    for word in line2:
        if word in eng_dict:
            print("{:>15}".format(word),"-> FOUND")
        else:
            dset = drop(word,eng_dict)
            iset = insert(word,eng_dict)
            sset = swap(word,eng_dict)
            rset = replace(word,eng_dict,keyb_dict)
            large_set = dset.union(iset)
            large_set = large_set.union(sset)
            large_set = large_set.union(rset)
            if len(large_set) == 0:
                print("{:>15}".format(word),"-> NOT FOUND")
            else: 
                print("{:>15}".format(word),"-> FOUND {:>2}:  ".format(len(large_set)),end = "")
                for item in large_set:
                    print(item, end = " ")
                print()
           
            
             
            
            
    