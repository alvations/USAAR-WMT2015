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

testfile1 = '/media/2tb/wmt15/corpus.tok/train-de_en.en'
testfile2 = '/media/2tb/wmt15/corpus.tok/train-de_en.de'

fout = io.open('train-de_en', 'w', encoding='utf8')

for engline, deuline in zip(sents(testfile1), sents(testfile2)):
    engoverlap = set(engline.split()).intersection(engvocab)
    deuoverlap = set(deuline.split()).intersection(deuvocab)
    
    if len(engoverlap) > 10 and len(deuoverlap) > 10:
        outline = unicode(engline+'\t'+deuline+'\n')
        #print engoverlap
        #print deuoverlap
        #print outline
        fout.write(outline)
        