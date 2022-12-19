# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 12:14:05 2022

@author: puniaa
"""

def parse_line(line):
    line = line.rstrip()
    tline = line.split('/')
    digits = tline[-3:]
    del tline[-3:]
    digits = (' '.join(map(str,digits)))
    digits = digits.split(" ")
    checker = ''.join(map(str,digits))
    tline = ('/'.join(tline))
    if checker.isdigit():
        ftuple = (int(digits[0]), int(digits[1]), int(digits[2]),tline)
        #print(ftuple)
        return ftuple
    else:
        return None
'''
parse_line("Here is some random text, like 5/4=3./12/3/4")
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))
parse_line(" Again some spaces\n/12/12/12")
'''
def get_line(filen, paranum, linenum):
    paragraph = 1
    lnumb = 0 
    flist = []
    for line in open(filen,encoding = "utf8"):
        flist.append(line)
    for line in range(len(flist)-1):
        if flist[line] == "\n" and flist[line+1] !="\n":
            paragraph +=1
        if paragraph == paranum:
            if lnumb != linenum:
                lnumb+=1
            elif lnumb == linenum:
                return flist[line]
            
filen = input("Enter File number ==> ").strip()
paranum = int(input("Enter the paragraph number ==> ").strip())
linenum = int(input("Enter the line number ==> ").strip())
file_text = ""

f = open("program.py", 'w')
while True: 
    #print(filen,paranum,linenum)
    line = get_line(filen,paranum,linenum)
    print(line)
    parsedline = parse_line(line)   
    #print(parsedline)
    if (parsedline[0] == 0) or (parsedline == None): 
        if (parsedline == None):
            print("Parsing has failed")
        break
    else: 
        filen = str(str(parsedline[0])+".txt")
        paranum = parsedline[1] 
        linenum = parsedline[2]
        file_text = file_text + parsedline[-1] + '\n'
print(file_text)
f.write(file_text)
f.close()          









