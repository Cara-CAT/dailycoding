import os

def count_file():
    f = open('C:\\Users\\HUAWEI\\Downloads\\data.txt')
    d=a=s=other=0
    content = f.readlines()
    for line in content:
        for i in line:
        #判断是否为数字isdigit()
            if i.isdigit():
                d+=1
            elif i.isalpha():
                a+=1
            elif i.isspace():
                s+=1
            else:
                other+=1
    print(d,a,s,other)
        #判断是否为字母isalpha()
        #判断是否为空格isspace()
    f.close()

count_file()

