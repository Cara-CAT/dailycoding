'''
#统计文件中出现数字、字母、空格等的次数
def count_file(fname):
    digits = letters = spaces = others = 0
    infile = open(fname,encoding="utf_8")
    for line in infile:  #读取行
        for c in line:  #读取每行的字符
            if c.isdigit():
                digits+=1
            elif c.isalpha():
                letters+=1
            elif c.isspace():
                spaces+=1
            else:
                others+=1
    infile.close()
    print("文件中数字共：\t",digits,"digits;")
    print("文件中字母共：\t",letters,"letters;")
    print("文件中空格共：\t",spaces,"blank chars;")
    print("文件中其他字符共：\t",digits,"other chars;")
count_file("C:\\Users\\HUAWEI\\Downloads\\data.txt")

#打开文件，读出数据的平均值。利用文件的当前位置重定位功能，第一遍读完，重新设定到文件开头，再读一遍。
# 在计算平均值的过程中，用一个表记录所有数据；在做方差计算时扫描该数据表。
def mean_v(fname):
    num = 0
    fsum = 0.0
    data = [] #该数据表用于计算过程中得到的平均值
    infile = open(fname)
    for line in infile:
        for s in line.split(): #每行的数据切分。split("str",num)表示以str为分隔符，切分num次
            x = float(s) #将s转换为浮点数
            data.append(x) #将x追加到data数据表中
            fsum += x #计算文件中所有数据的和
            num += 1 #统计个数
    
    if num == 0:
        return(0,0,0)

    mean = fsum / num #计算平均值

    #计算方差
    fsum = 0
    for x in data: #重新扫描数据表，计算方差
        fsum += (x - mean)**2
    return (num, mean, (fsum / num)**0.5)

    print("该文件中数据的平均值是：\t",mean,"mean;")
    print("该文件中数据的方差是：\t",fsum,"fsum;")

    infile.close()
    
mean_v("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\test.txt")


#改进：每次调用得到文件里的一个浮点数，尽量避免建立大型数据对象
#定义open_float()函数用于打开文件；next_float()用于逐一读出文件里的浮点数

#定义需要的全局变量
infile = None
nlist = [] #用于保存浮点数的字符串
crt = 0
#定义打开文件的函数
def open_float(fname):
    global infile
    infile = open(fname)

#next_float()采用“缓冲区”式工作方式；用一个缓冲区（一个表）来保存文件中的一行
#信息，每次调用时根据表里的信息生成一个浮点数返回。一旦表中的内容用完，然后再从文件中读取一行。
#分解后行的内容后存入缓存区
#next_float（）使用缓存区在函数调用之后还应该继续存在，以便下次调用时继续使用。
#因此，需要生命周期长的变量记录这些数据对象。
def next_float():
    global nlist, crt #缓冲式处理，使用全局变量
    if crt == len(nlist): #当前用完一行，在读一行。其中crt类似一个指针
        line = infile.readline() #读一行数据
        if not line: #空字符串表示文件已经处理完毕
            infile.close()
            return None
        nlist = line.split() #切分单词
        crt = 0
    x = nlist[crt]
    crt+=1 #移动指针
    print("指针位置：",crt)
    return float(nlist[crt-1])

#调用方式：首先调用open_float(filename)初始化相关功能，然后每次调用next_float()得到下一个浮点数
if __name__ =="__main__":
    open_float("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\test.txt")
    for i in range(50):#根据文件定义循环
        print(next_float())
    print("\n")


#分析上面的实现过程：函数中创建的最长字符串就是文件里最长的一行，通过切分产生的表只包括一行里的浮点数，不会产生很大的浮点数
#存在的问题也很明显：使用了几个全局变量，其中保存的是函数内部使用的数据，不太安全。
#针对存在的问题可以这样处理：把这两个函数以及相关的数据定义为一个模块，用import导入时把它们都留在模块对象里，并不导入主程序的全局名字空间
#但是全局变量还是会出现在模块的名字空间里

# 缺点：用了几个全局变量，功能可能受到干扰
'''
#优化：定义一个函数，处理文件打开工作，为了局部化，文件打开中和打开后使用的变量
#另一种实现，其中使用了局部函数和局部变量（为什么呢？）
#返回局部定义的函数对象（实际上带着局部变量）
def read_floats(fname):
    nlist=[]
    infile = open(fname)
    crt = 0
    #定义局部函数
    def next_float():
        nonlocal nlist
        nonlocal crt
        if crt == len(nlist):#一行已经用完
            line = infile.readline()
            if not line:#如果是空串，整个文件已经处理完
                infile.close()
                return None
            nlist = line.split()
            crt = 0
        crt += 1
        return float(nlist[crt-1])
    return next_float #返回局部定义的函数对象

if __name__=="__main__":
    nextf1 = read_floats("D:\\Astudyfile\\GitRepo\\dailycoding\\C6\\test.txt")

    for i in range(10):
        print(nextf1())


