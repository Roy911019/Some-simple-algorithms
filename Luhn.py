# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 11:32:09 2020

@author: Roy
"""

from tkinter import*

#luhn算法：偶数位乘以2，结果为2位数时将各位与十位相加，再将所有数相加乘以9，最后一位即为校验位
def luhn(number=''):
    global check_num
    sum_digit =0
    #从右往左开始
    number = number[::-1]
    for i, digit in enumerate([int(x) for x in number]):
        print(i)
        if i % 2 == 0:
            digit *=2
            if digit > 9:
                digit -=9
        sum_digit += digit
        # print(sum_digit)
    check_digit =  sum_digit * 9
    check_num = str(check_digit)[-1]
    return check_num
#用于按键生成校验码
def gen():
    number1 = entry.get()
    luhn(number =number1)
    label_str.set(check_num)
#用于回车生成校验码   
def gen2(event):
    number1 = entry.get()
    luhn(number =number1)
    label_str.set(check_num)

tk =Tk()

tk.title('校验码生成器')
winWidth = 300
winHeight = 100
# 获取屏幕分辨率
screenWidth = tk.winfo_screenwidth()
screenHeight = tk.winfo_screenheight()
 
x = int((screenWidth - winWidth) / 2)
y = int((screenHeight - winHeight) / 2)
 

# 设置窗口初始位置在屏幕居中
tk.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))


entry_var =StringVar()
label_str =StringVar()

frame1 = Frame(tk)
frame1.pack(anchor = W,padx =3,pady=3)
label =Label(frame1,text ='ICCID')
label.pack(side=LEFT,padx =3,pady=3)
entry = Entry(frame1,textvariable = entry_var,width = 30)
entry.pack(side=LEFT,padx =3,pady=3)
entry.bind('<Return>',gen2)
frame2 = Frame(tk)
frame2.pack(anchor = 'center',padx =3,pady=3)
label =Label(frame2,textvariable = label_str,bg='lightyellow',width =5)
label.pack(side=LEFT,padx =3,pady=3)
button =Button(frame2,text ='生成',command=gen)
button.pack(side=LEFT,padx =3,pady=3)







tk.mainloop()    

   