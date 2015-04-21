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

"""
English
(2,190,329)  min5: 7623 661805 0.0115184986514 0.809919395019
(1,284,686)  min10: 7585 527446 0.0143806190586 0.810059723609
(2,614,797)  min1:  7637 696863 0.0109591124798 0.812114877365 

German
min10: 8868 985668 0.00899694420434 0.745656280454
min5: 9001 1327243 0.00678172723458 0.737952164527
"""

