# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:57:17 2020

@author: Roy
"""

import random
import re

#随机函数:4位随机函数，8位随机函数，16位随机函数

def random_Num_4():
    Num_4 = []
    for element in range(4):
        Num_4.append(random.randint(0,9))
    return Num_4

def random_Num_8():
    Num_8 = []
    for element in range(8):
        Num_8.append(random.randint(0,9))
    return Num_8
    
def random_Hex_8():      
    Hex_8 = []
    for element in range(8):   
       Hex_8.append(random.choice(['0','1','2','3','4','5',
                                          '6','7','8','9','A','B','C','D','E','F']))
    return Hex_8
  
#换算后会有0x的现象，因此需要用判别语句,255为FF       
def random_Hex_16():      
    Hex_16 = []
    for element in range(16):
       a = hex(random.randint(0,255))
       if len(a) == 4:
           Hex_16.append(a[-2:].upper())
       else:
           Hex_16.append('0'+a[-1:].upper())
    return Hex_16

#luhn算法：偶数位乘以2，结果为2位数时将各位与十位相加，再将所有数相加乘以9，最后一位即为校验位
def luhn(number=''):
    global check_num
    sum_digit =0
    #从右往左开始
    number = number[::-1]
    for i, digit in enumerate([int(x) for x in number]):
        # print(i)
        if i % 2 == 0:
            digit *=2
            if digit > 9:
                digit -=9
        sum_digit += digit
        # print(sum_digit)
    check_digit =  sum_digit * 9
    check_num = str(check_digit)[-1]
    return check_num

#计算ACC
def acc(imsi=''):
    a = str(imsi)[-1]
    b = 2**int(a)
    c = hex(b)
    if len(c) == 3:
        d = '000' + c[-1]
    elif len(c) == 4:
        d = '00' + c[-2:]
    else:
        d = '0' + c[-3:]
    return d

def mccmnc(value=""):
    if len(value) == 5:
        result = value[1] + value[0] + "F" + value[2] + value[4] + value[3]
        return result
    elif len(value) == 6:
        result = value[1] + value[0] + value[3] + value[3] + value[5] + + value[4]
        return  result
    else:
        pass

#搜索
def searchStr(pattern,msg):
    result = re.findall(pattern,msg)
    return result