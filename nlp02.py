#!/usr/bin/env python3
 
import re
import sys
import string
from abbreviations import abbr

#pat = re.compile("[.?!][ \n\t]")    
pat = re.compile(r"[A-Za-z]+[.?!][ \n\t]")
#word_pat = re.compile(r"[A-Za-z]+")

def getFile(fname):
    all = ""
    with open(fname, 'r') as fd:
        for line in fd:
            s = line.replace("\n"," ")
            all += s
    return all

def parse_sentence(txt):
    for x in word_pat.finditer(txt):
        a,b = x.span()
        k = txt[a:b]
        
if __name__ == "__main__":
     
    if len(sys.argv) < 2:
        print("Missing filename: specify a file to read.", file=sys.stderr)
        sys.exit(0)
    
    dict = {}
    txt = getFile(sys.argv[1])
    
    for x in pat.split(txt):
        line = x.strip()
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        words.sort()
        
        for word in words:
            dict[word] = dict.get(word, 0) + 1
#          if word in dict:
#            dict[word] = dict[word] + 1
#          else:
#            dict[word] = 1

    for key in list(dict.keys()):
      print(key, ":",dict[key])
