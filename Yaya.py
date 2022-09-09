import requests
from lxml import etree
import re
from fake_useragent import UserAgent



for count in range(1,20):  #确定下载章数
    ua=UserAgent()
    header={'User-Agent':ua.ie}  #UA伪装
    last='read'+'_'+str(count)+'_'+'p100'+'.html'  #确定每章URL
    url='https://0530.yayayd.com/chapter/WanYuZhiWang/'+last
    mid=requests.get(url,headers=header) #get方法获取网页
    
    x=mid.text    #网页文件转为文本
    print(mid.status_code)  #判断网页链接情况（正常200，错误404)
    html=etree.HTML(x)  #HTML方法，便于xpath获取
    chapter=html.xpath('/html/body/div[1]/div[1]/text()') #提取章节名
    content=html.xpath('/html/body/div[1]/div[3]/div/a/p/text()') #提取正文
   
    address='c:/Users/leviouseyon/Desktop/sample.txt' #确定保存位置
    for ch in chapter:    #保存章节名
        with open (address,'a',encoding='utf-8') as fp:
            fp.writelines(ch)
            fp.write('\n')
            fp.flush()

    for i in content:      #保存正文内容
        i=re.sub('本章未完，请点击下一页继续阅读！ 第[0-9]+页/共[0-9]+页','',i)   #正则排除无关内容
        i=re.sub('(第[\u4e00-\u9fa5]章.*){,1}','',i,flags=re.S)   #正则排除正文内出现的章节名
        with open (address,'a',encoding='utf-8') as fp:
            if i:
                fp.writelines(i)
                fp.write('\n')    #每输入一次，自动换行
                fp.flush()
