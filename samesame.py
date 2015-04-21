# -*- coding: utf-8 -*-

import os, sys, time, itertools, io
from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def sents(infile, numlines=20000000):
    """ Lazy corpus reader that yields line. """
    with io.open(infile, 'r', encoding='utf8') as fin:
        for i, line in enumerate(fin):
            if i > numlines:
                break
            yield line.strip()

def train_classifier(onefile, zerofile, num_tags, ngram_order=2):
    train_docs = itertools.chain(sents(onefile, num_tags), 
                             sents(zerofile, num_tags))
    ngram_vectorizer = CountVectorizer(analyzer='word',
                                   ngram_range=(n, n), min_df=1)
    trainset = ngram_vectorizer.fit_transform(train_docs)
    tags = [1]*numtags + [0]*numtags
    classifier = MultinomialNB()
    classifier.fit(trainset, tags)
    return ngram_vectorizer, classifier


num_tags = 2169
# English
onefile1 = 'newstest.deen.en'
zerofile1 = '/media/2tb/wmt15/data/monolingual/en/news.2014.en.shuffled'
testfile1 = '/media/2tb/wmt15/corpus.tok/train-de_en.en'
# German
onefile2 = 'newstest.deen.en'
zerofile2 = '/media/2tb/wmt15/data/monolingual/en/news.2014.de.shuffled'
testfile2 = '/media/2tb/wmt15/corpus.tok/train-de_en.en'

fout = io.open('train-de_en', 'w')

eng_vectorizer, eng_classifier = train_classifier(onefile1, zerofile1, num_tags)
deu_vectorizer, deu_classifier = train_classifier(onefile1, zerofile1, num_tags)


for enline, deline in zip(sents(testfile1), sents(testfile2)):
    is_eng = eng_classifier.predict(eng_vectorizer.transform(enline))
    is_deu = deu_classifier.predict(deu_vectorizer.transform(deline))
    if is_eng == is_deu == 1:
        outline = enline + '\t' + deline + '\n'
        print outline
        fout.write(outline)