# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:54:21 2020

@author: yairg
"""
from nltk.corpus import wordnet as wn


# Return all unique lemma names of all hypernyms of a given word
def get_hypernyms(word):
    terms = set([])
    for synset in wn.synsets(word):
        for hypernym in synset.hypernyms():
            for lemma_name in hypernym.lemma_names():
                terms.add(lemma_name)
    return terms


# Return all unique lemma names of all hyponyms of a given word
def get_hyponyms(word):
    terms = set([])
    for synset in wn.synsets(word):
        for hyponym in synset.hyponyms():
            for lemma_name in hyponym.lemma_names():
                terms.add(lemma_name)
    return terms


# Return all unique lemma names of all entailments of a given word
# Entailments do not exist for most words and are, therefore, not very useful
def get_entailments(word):
    terms = set([])
    for synset in wn.synsets(word):
        for entailment in synset.entailments():
            for lemma_name in entailment.lemma_names():
                terms.add(lemma_name)
    return terms

