#coding=utf-8
import urllib
import re

model_url = 'http://tieba.baidu.com/p/2460150866?pn='

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
	
def getPageNum(html):
    reg = r'<a href=.*pn=(.*)">尾页</a>'
    imgre = re.compile(reg)
    html_str = re.findall(imgre,html)
    print html_str
    num=int(html_str[0])
    print num
    return num

def getImg(html,i):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x=1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'page_%s_the_%s.jpg' %(i,x))
        x+=1

html = getHtml("http://tieba.baidu.com/p/2460150866")
getImg(html,1)
print('The 1 page\'s pictures are downloaded')
num = getPageNum(html)
print getPageNum(html) 
print('The total page is %d'  % num)
if num>1:
  for i in range(44,num+1):
    real_url = model_url+str(i)
    print real_url
    htmls=getHtml(real_url)
    getImg(htmls,i)
    print('The %d page\'s pictures are downloaded' % i)

