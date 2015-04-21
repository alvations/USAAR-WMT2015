# -*- coding: utf-8 -*-

import os, sys, time, itertools, io
from collections import Counter

file1=io.open('newstest.deen.en', 'r')
file2=io.open('train-de_en.min5.en')

testvocab = Counter(file2.read().split())
trainvocab = Counter(file1.read().split())

overlap = set(testvocab.keys()).intersection(trainvocab.keys())

numwords = sum([testvocab[i] for i in overlap])

print len(overlap), len(testvocab), len(overlap)/float(len(testvocab)), numwords/float(sum(testvocab.values()))   