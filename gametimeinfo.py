# -*- coding: utf-8 -*-
import urllib
import urllib.request
import re

pageurl = input('输入你的steam个人主页网址：')
url = pageurl + '/games/?tab=all'

data = urllib.request.urlopen(url).read() #读取网页
data = data.decode('utf-8')

#提取游戏名
pname = re.compile(r'\bname\"\:\"(.*?)\"',re.S)
gamename =  re.findall(pname,data)
print (gamename)
#提取游戏时间
ptime = re.compile(r'\"hours\_forever\"\:\"(.*?)\"')
gametime = re.findall(ptime,data)
#print (gametime)
#将游戏名和时间依次按序合并
n=1
for i in gametime:
    gamename.insert(n,i)
    n += 2
#print(gamename)
#写入文档
file = open('gametimeinfo.txt','w+')
t=0
#加入| 作为分隔符
for i in gamename:
    if t == 0:
        file.write(i)
        file.write('|')
        t += 1
    else:
        value = re.compile(r'^[0-9]+\.?[0-9]?$')
        result = value.match(i)
        if result:
            file.write(i)
            file.write('\n')
            t -= 1
        else:
            file.write('\n')
            file.write(i)
            file.write('|\n')
            t -= 1

print (file)    #输出一下组合的结果
file.close()
print('一切数据已放在目录下的gametimeinfo.txt文件内。')
