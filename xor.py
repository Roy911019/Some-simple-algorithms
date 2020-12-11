# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:21:05 2020

@author: Roy
"""


'''********************************************************
2     Func Name:    addZero
3     Para:         x    :  字符串  
4                   y    :  长度
5     return:       x    :  处理后的字符串
6     Desc:         将字符串修改为指定长度，不足的补0，只限于加长，不剪短
********************************************************'''

def addZero(x, y):
    while True:
        if len(x) < y:
            x = '0' + x
        else:
            break
        
    return x


'''********************************************************
 2     Func Name:    hexToInt
 3     Para:         h:16进制数  
 4     return:       datalen:  10进制数
 5     Desc:         #将 16进制数 转换为  INT
 8 ********************************************************'''

def hexToInt(h):       
    return int(h,16)

'''********************************************************
13     Func Name:    intToHex
14     Para:         n    :  10进制数
15                   x    :  几个字节
16     return:       16进制字符串
17     Desc:         将 16进制数 转换成对应的16进制字符串，并根据字节长度补0，不带0x或者 x
20 ********************************************************'''

def intToHex(n, x):
    num = hex(n)
    #print(num)
    num_list = num.split('0x')[1:]#num_list = num.split('0x')[1]
    return addZero(num_list[0].upper(), x*2)
         

#16进制转10进制
def add0x(s):
    return eval('0x'+s)

# def checkValue(h):
#     #先取前2组，每组2个做异或运算
#     value = add0x(h[0:2]) ^ add0x(h[2:4])#异或后是10进制数
    
#     for i in range(4, len(h), 2):
#         value = value ^ add0x(h[i:i+2])

        
#     value = intToHex(value, 1)#16进制的校验值，1个字节
#     return value.upper()

def checkValue(h,l):
    #先取前2组，每组2个做异或运算
    result=""
    for i in range(int(len(h)/2)):
        a = 2*(i)
        b = 2*(i+1)
        value = add0x(h[int(a):int(b)]) ^ add0x(l[int(a):int(b)])#异或后是10进制数
        value = intToHex(value, 1)#16进制的校验值，1个字节
        result += value.upper()
    return result


# c = checkValue("10000000000000000010000000000000","4113D062DCD5F04E77EAE738653703C0")
# print(c)