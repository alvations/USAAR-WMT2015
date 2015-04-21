# -*- coding: utf-8 -*-

import os, sys, time, itertools, io
from collections import Counter

file1=io.open('newstest.deen.en', 'r')
file2=io.open('train-de_en.min5.en')

testvocab = set(file2.read().split())
trainvocab = set(file1.read().split())


overlap = testvocab.intersection(trainvocab)
diff = testvocab.difference(trainvocab)

print overlap, diff, overlap/float(diff) 