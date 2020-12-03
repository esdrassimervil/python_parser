#!/usr/bin/env python3

import re
import sys
from random import choice
from collections import defaultdict
from abbreviations import abbr

bos = "__BOS__"
eos = "__EOS__"

twograms = defaultdict(lambda: [])
wordlist = []

sentence_pat = re.compile(r"[.?!][ \n\t]")
word_pat     = re.compile(r"[A-Za-z]+")

def getfile(fname):
    all = ""
    with open(fname, 'r') as fd:
        for line in fd:
            s = line.replace("\n"," ")
            all += s
    return all

def parse_sentence(s):
    global wordlist, twograms

    prev = bos
    for w in word_pat.finditer(s):
        x,y = w.span()
        k = s[x:y]
        twograms[prev].append(k)
        wordlist.append(k)
        prev = k
    wordlist.append(eos)
    twograms[prev].append(eos)

def abfilter(s):
    for k in abbr:
        s = re.sub(k, abbr[k], s)
    return s

def randsentence1():
    while True:
        k = choice(wordlist)
        if k == eos:
            break
        print(k, end=' ')
    print('.')

def randsentence2():
    k = bos
    while k != eos:
        k = choice(twograms[k])
        if k == eos:
            print('.')
        else:
            print(k, end=' ')

if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Missing filename: specify a file to read.", file=sys.stderr)
        sys.exit(0)

    dict = {}

    doc = getfile(sys.argv[1])
    doc = abfilter(doc)
    doc = re.sub('"','',doc)             # dangerous

    n = 0
    for x in sentence_pat.split(doc):
        parse_sentence(x)

    keylist = list(twograms.keys())
    keylist.sort(key=lambda x: len(twograms[x]))

    for k in twograms:
        print(k,twograms[k])
