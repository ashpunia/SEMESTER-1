# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 00:44:12 2022

@author: puniaa
"""

def parse_line(line):
    tline = line.split('/')
    digits = tline[-3:]
    del tline[-3:]
    digits = (' '.join(map(str,digits)))
    digits = digits.split(" ")
    checker = ''.join(map(str,digits))
    tline = ('/'.join(tline))
    if checker.isdigit():
        ftuple = (int(digits[0]), int(digits[1]), int(digits[2]),tline)
        print(ftuple)
        return ftuple
    else:
        return None

parse_line("import webbrowser/2/3/3")
parse_line("Here is some random text, like 5/4=3./12/3/4")
print(parse_line("Here is some random text, like 5/4=3./12/3/4as"))
print(parse_line("Here is some random text, like 5/4=3./12/412/a/3/4"))
print(parse_line(" Here is some spaces 12/32/4"))
parse_line(" Again some spaces\n/12/12/12")
