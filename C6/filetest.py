import os

def count_file():
    f = open('C:\\Users\\HUAWEI\\Downloads\\data.txt')#打开文件，此时文件在磁盘中
    d=a=s=other=0
    content = f.readlines()#读文件里的数据，读到内存中,
    #优化1：将检索结果放在内存的表list[]里面，可以降低IO与检索次数
    #优化2：部分读，建立缓存，减少内存的占用

    
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

