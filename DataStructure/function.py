# -*- coding: utf-8 -*-
"""
"""

#Python’s Built-In Functions 

#Input/Output输入输出
#print() #输出到客户端
#input()#接受客户端的输入
#open() #打开文件，可以指定操作类型。 ‘r’ for reading， ‘w’ for writing， ‘a’ for appending， binary ﬁles  ‘rb’ or ‘wb’  

fp=open('file.txt','a')
print(fp.read()) #Return the (remaining)contents of a readable ﬁle as a string. 
print(fp.read(10))#Return the next k bytes of a readable ﬁle as a string
print(fp.readline())#Return (remainderof) the current line of a readable ﬁle as a string. 
print(fp.readlines())#Return all (remaining)lines of a readableﬁle as a list of strings. 

for line in fp:#
    print(line)
print(fp.seek(10)) #Change the current position to be at the kth byte of the ﬁle  
print(fp.tell()) #Return the current position, measured as byte-offsetfrom the start. 

"""
Write each of the strings of the given sequence at the current position of 
the writable ﬁle. This command does not insert any newlines, 
beyond those that are embedded in the strings. 
"""
seq=('\nasdfasd','4343434')
fp.writelines(seq)
fp.write('new string') #Write given string at current position of the writable ﬁle.

print("this a logging", ﬁle=fp) #Redirect output of print functionto the ﬁle

fp.close()

#Character Encoding字符编码
#ord( A ) is 65 and chr(65) is A 
print(ord('A'))
print(chr(65))

#Mathematics数学
#abs, divmod,pow, round,sum

#Ordering排序
#max,min 

#Collections/Iterations
#range # 生成新的序列
#len #序列长度
#reversed, all, any, map 
#iter, next 

if __name__ =='__main__':
    print('main')