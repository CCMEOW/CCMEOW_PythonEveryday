#!usr/bin/env python2
# -*- coding: utf-8 -*- 

#有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
#只统计C/C++/Python代码
import os

support = ['.cpp','.c','.py']
def countCodes(path,cnt,noneCnt,comCnt):
    ext = os.path.splitext(path)[1]
    if ext not in support:
        print u'不支持的文件格式',ext
        return 0,0,0
    mark = False #mark用来标记注释是否以'''或"""开头
    with open(path,'r') as f:
        tmpComCnt = 0 #tmpComCnt用来临时计算以'''或"""开头的注释行数
        for line in f.readlines(mark):
            cnt+=1
            line = line.strip()
            if not len(line):#判断空行
                noneCnt+=1
            elif (ext=='.cpp' or ext=='.c'):#C/C++代码
                if mark and not line.endswith('*/'):#注释代码段
                    tmpComCnt+=1
                if line.startswith('//'):
                    comCnt+=1
                elif line.startswith('/*'):
                    mark = True
                    tmpComCnt+=1
                elif line.endswith('*/'):
                    mark = False
                    comCnt = comCnt+tmpComCnt+1
                    tmpComCnt=0
            elif ext=='.py':#python代码
                if mark and not (line.endswith("'''") or line.endswith('"""')):#注释代码段
                    tmpComCnt+=1
                elif line.startswith('#'):
                    comCnt+=1
                elif (line.startswith("'''") or line.startswith('"""')) and not mark:
                    mark = True
                    tmpComCnt+=1
                elif mark and (line.endswith("'''") or line.endswith('"""')):
                    mark = False
                    comCnt = comCnt+tmpComCnt+1
                    tmpComCnt=0
    return cnt,noneCnt,comCnt

def countAllCodes(fpath):
    totCnt,totNoneCnt,totComCnt = 0,0,0
    for path in os.listdir(fpath):
        cnt,noneCnt,comCnt = 0,0,0
        cnt,noneCnt,comCnt = countCodes(os.path.join(fpath,path),cnt,noneCnt,comCnt)
        totCnt+=cnt
        totNoneCnt+=noneCnt
        totComCnt+=comCnt
    print u'总行数     空行       注释       净代码行数'
    print '{:<10}'.format(totCnt),'{:<10}'.format(totNoneCnt),'{:<10}'.format(totComCnt),'{:<10}'.format(totCnt-totNoneCnt-totComCnt)
        
print u'请输入文件夹路径'
PATH = raw_input()
countAllCodes(PATH)
