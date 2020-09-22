import re             #导入正则模块
import sys     #用于获取命令行参数
filename = ''


#获取命令行参数
#filename = sys.argv[2]
filename = 'test.txt'
"""
def get_parameters(para):
    #filename = sys.argv[2]
    filename = para
get_parameters("test.txt")
"""

#统计词频
def word_fre(filename):
    with open(filename) as f_obj:
        contents = f_obj.read() #contents 为文章内容字符串
    contents = contents.lower()#字母全部转换成小写
    wordlist = re.findall(r'[\w^-]+',contents)#去掉文章符号
    #转换成小写字符  分割单词


    fre_dic = {}#存储词频的空字典
    for word in wordlist:
        fre_dic[word] = wordlist.count(word) #count方法可以返回列表wordlist中w元素的个数
    #output
    total = len(fre_dic.keys())
    print("total   ",total)
    print("\n\n")

    #按照词频排序

    fre_dic_list = sorted(fre_dic.items(),key=lambda x:x[1],reverse=True)#sorted高阶函数语法格式：  sorted(可迭代对象,key=函数名,reverse=False/True)
    #print(fre_dic)   注意排序之后字典会变成列表
    """
        for key in fre_dic_list:
        print('{:10} {:10}'.format(key ,value))
    """
    for one_fre_dic in fre_dic_list:
       print("%20s  %5d"%(one_fre_dic[0],one_fre_dic[1]))




word_fre(filename)


