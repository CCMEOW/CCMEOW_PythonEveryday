#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

import string

print u'请输入文件完整路径如c:\\test.txt'
PATH = raw_input()
with open(PATH,'r') as f:
    d = {}
    symbols = string.punctuation
    for line in f.readlines():
        line = line.split()
        for word in line:
            word = word.strip(symbols)
            if word in d:
                d[word]+=1
            else:
                d.setdefault(word,1)
    for elem in d:
        print elem,d[elem]