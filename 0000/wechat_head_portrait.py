#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#微信强迫症头像

from PIL import Image,ImageFont,ImageDraw
import sys,locale

print(u'请输入文件夹完整路径(如g:\\test.jpg)：')
PATH = raw_input()
im = Image.open(PATH)
draw = ImageDraw.Draw(im)
print(u'请输入要添加的数字/文字：')
text = raw_input().strip().decode(sys.stdin.encoding or locale.getpreferredencoding(True))
text.encode('utf-8')
width,height = im.size
font = ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc',int(width*0.07))
draw.ellipse((width*0.8-int(width*0.07),height*0.1-int(width*0.07),width*0.8+int(width*0.07)*2,height*0.1+int(width*0.07)*2),outline='white',fill='white')
draw.text((width*0.8,height*0.1),text,font = font,fill = 'red')
im.save('pic.jpg')
print(u'图片已保存到当前目录，文件名为pic.jpg。按回车键退出')
raw_input()

