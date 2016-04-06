#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#生成200个优惠码

import random,string

with open('coupon_code.txt','w') as f:
    for i in range(200):
        str = string.digits + string.letters
        code = ''#优惠券码
        for j in range(8):
            code+=random.choice(str)
        f.write(code+'\n')
print(u'激活码已保存到当前目录，文件名为coupon_code.txt')