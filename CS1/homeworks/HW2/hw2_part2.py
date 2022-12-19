# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:52:12 2022

@author: puniaa

Description of overall program
"""

'''
Import Statements
'''



'''
Function Definitions
'''

def encrypt(word):
  word1=word.replace(' a', '%4%')
  word2=word1.replace('he', '7!')
  word3=word2.replace('e','9(*9(')
  word4=word3.replace( 'y','*%$' )
  word5=word4.replace('u', '@@@' )
  word6=word5.replace('an','-?')
  word7=word6.replace('th','!@+3')
  word8=word7.replace('o','7654' )
  word9=word8.replace('9', '2')
  word10=word9.replace('ck','%4')
  return word10

def decrypt(word):
    word1=word.replace('%4','ck')
    word2=word1.replace('2','9')
    word3=word2.replace('7654','o')
    word4=word3.replace('!@+3','th')
    word5=word4.replace('-?','an')
    word6=word5.replace('@@@','u')
    word7=word6.replace('*%$','y')
    word8=word7.replace('9(*9(','e')
    word9=word8.replace('7!','he')
    word10=word9.replace('%4%', ' a')
    return word10

'''
Main Body
'''

x = input("Enter a string to encode ==> ".strip("\r"))
print(x)
print(" ")
y = encrypt(x)
print("Encrypted as ==> ", y)
diff = len(y) - len(x)
print("Difference in length ==> ",diff)
print("Deciphered as ==> ".strip("\r"), decrypt(y))
z = decrypt(y)
if x == z:
   print("Operation is reversible on the string.")
else:
   print("Operation is not reversible on the string.")
