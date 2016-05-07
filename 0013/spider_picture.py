#!usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

class Picture:
    def __init__(self,url,seeLZ,path):
        self.picUrl = url
        self.data = {
            'see_lz':'1',
            'pn':'1'
        }
        self.soup=BeautifulSoup('','lxml')
        self.PATH = path
        self.pgNum = 1
        self.picTag = 1
    #保存单页的源码
    def getPage(self,pgIndex=1):
        self.data['pn'] = pgIndex
        result = requests.get(self.picUrl, params=self.data)
        text = result.text.encode('utf-8', 'ignore')
        # beautiful找到图片来源链接
        self.soup = BeautifulSoup(text, 'lxml')
     #保存单页图片
    def getPagePicture(self):
        for link in self.soup.find_all('img', 'BDE_Image'):
            print u'正在保存第',self.picTag,u'张图片'
            singleUrl = link.get('src')
            pic = requests.get(singleUrl)
            picData = pic.content
            pic = requests.get(singleUrl)
            path =  self.PATH + '\pic'+ str(self.picTag) + '.png'
            with open(path, 'wb') as f:
                f.write(picData)
            self.picTag += 1

    #得到帖子总页数
    def getPageNum(self):
        def redButNoStyle(tag):
            return tag.has_attr('class') and tag['class']==['red'] and not tag.has_attr('style')
        result = self.soup.find(redButNoStyle)
        self.pgNum =  result.get_text()

    def getAllPicture(self):
        print u'正在保存...'
        self.getPage()
        self.getPageNum()
        currPage = 2
        self.getPagePicture()
        while currPage<=int(self.pgNum):
            self.getPage(currPage)
            self.getPagePicture()
            currPage+=1

print u'本工具用于爬去百度贴吧帖子中的图片，未做异常处理，请勿胡乱输入数据'
print u'输入帖子地址，如http://tieba.baidu.com/p/1234'
url=raw_input()
print u'输入要保存图片的地址，如C:\\test'
path = raw_input()
print u'是否只看楼主？是请输入1 否请输入0'
seeLZ = str(raw_input())

# url = 'http://tieba.baidu.com/p/2166231880'
# path = r'E:\picture\test'
# seeLZ = '1'

picture = Picture(url,seeLZ,path)
picture.getAllPicture()
print u'Done~按任意键退出'
tmp = raw_input()