# -*- coding: utf-8 -*-

import os, sys, time, itertools, io
from collections import Counter

from nltk.corpus import stopwords


def sents(infile):
    """ Lazy corpus reader that yields line. """
    with io.open(infile, 'r', encoding='utf8') as fin:
        for i, line in enumerate(fin):
            yield line.strip()

engstop = set(stopwords.words('english'))
deustop = set(stopwords.words('german'))

_engvocab = io.open('newstest.deen.en', 'r').read().split()
_deuvocab = io.open('newstest.deen.de', 'r').read().split()

engvocab = set(_engvocab).difference(engstop)
deuvocab = set(_deuvocab).difference(deustop)

testfile1 = '/media/2tb/wmt15/corpus.tok/train-lm.en'
testfile2 = '/media/2tb/wmt15/corpus.tok/train-lm.de'

fout_en = io.open('train-lm.en', 'w', encoding='utf8')
fout_de = io.open('train-lm.de', 'w', encoding='utf8')

for engline in sents(testfile1):
    engoverlap = set(engline.split()).difference(engvocab)
    if len(engoverlap) > 10:
        fout_en.write(engline+'\n')

for deuline in sents(testfile2):
    deuoverlap = set(deuline.split()).difference(deuvocab)
    if len(deuoverlap) > 10:
        fout_de.write(deuline+'\n')
        

