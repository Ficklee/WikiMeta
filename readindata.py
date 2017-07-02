import numpy as np
import re
import os
import pickle
def ReadCharDict(CharDictPickle,NumpyArrayFile):
    with open(CharDictPickle,'rb') as fDict:
        CharDict = pickle.load(fDict)
    CharVec = np.load(NumpyArrayFile)
    return CharDict,CharVec
def ReadWordDict(WordDictPickle,WordNumpyArrayFile):
    with open(WordDictPickle,'rb') as wDict:
        WordDict = pickle.load(wDict)
    WordVec = np.load(WordNumpyArrayFile)
    return WordDict,WordVec
def DataGen(RawCorpusLine,Char,window):
    TargetChar = re.compile(Char.decode('utf-8'))
    line_ = RawCorpusLine.strip().decode('utf-8')
    corpus_lst = line_.split('\t')
    sentence = corpus_lst.pop(0)
    CharNum = len(corpus_lst)
    RealCharNum = re.findall(TargetChar,sentence)
    if CharNum != RealCharNum:
        return None
    


