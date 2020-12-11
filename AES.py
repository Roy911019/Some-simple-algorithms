# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 15:02:04 2020

@author: Roy
"""


from Crypto.Cipher import AES
import binascii


class Aescrypt():
    def __init__(self,key,model,iv):
        self.key = self.add_16(key)
        self.model = model
        self.iv = iv

    def add_16(self,par):
        if type(par) == str:
            par = par.encode()
        while len(par) % 16 != 0:
            par += b'\x00'
        return par

    def aesencrypt(self,text):
        text = self.add_16(text)
        if self.model == AES.MODE_CBC:
            self.aes = AES.new(self.key,self.model,self.iv) 
        elif self.model == AES.MODE_ECB:
            self.aes = AES.new(self.key,self.model) 
        self.encrypt_text = self.aes.encrypt(text)
        return self.encrypt_text

    def aesdecrypt(self,text):
        if self.model == AES.MODE_CBC:
            self.aes = AES.new(self.key,self.model,self.iv) 
        elif self.model == AES.MODE_ECB:
            self.aes = AES.new(self.key,self.model) 
        self.decrypt_text = self.aes.decrypt(text)
        self.decrypt_text = self.decrypt_text.strip(b"\x00")
        return self.decrypt_text


if __name__ == '__main__':
    passwd = "9999999999999999"
    passwd1 = binascii.a2b_hex(passwd)
    print("hexstr编码:",passwd1)
    # iv = '1234567812345678'
    
    # passwd = binascii.b2a_hex(b"99999999999999999999999999999999")
    # print("hexstr编码:",passwd)   
    text = "ffeeea"
    text2 = binascii.a2b_hex(text)
    print("hexstr编码:",text2)
    
    # crypted_str =binascii.b2a_hex(crypt)       #输出Hex
    # result = crypted_str.decode()

    
    # aescryptor = Aescrypt(passwd,AES.MODE_CBC,iv) # CBC模式
    aescryptor = Aescrypt(passwd1,AES.MODE_ECB,"") # ECB模式
    # text = "606DC703B80335B05E0A3EDEBD7BAA3A"
    en_text = aescryptor.aesencrypt(text2)
    print("hexstr编码:",en_text)
    en_text1 = binascii.b2a_hex(en_text)
    print(en_text1)
    en_text2 = str(en_text1, encoding = "utf-8").upper()
    print("hexstr解码:",en_text2)
   
    

   
