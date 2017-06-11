---
title: 不到百行代码就能抓取宿舍用电情况
date: 2017-06-11 14:53:49
tags: Python3
category: Python
---

我校装上空调以后，许多担心宿舍用空调久了就没电了。

then~中心校区提供了一个用电查询的系统

![](https://ws1.sinaimg.cn/large/006tKfTcly1fghd3pu094j31400p0q6j.jpg)

# 1.chrome 开发者模式

在 chrome 开发者模式下查看它的网络请求

![](https://ws1.sinaimg.cn/large/006tKfTcly1fghd4llyldj31400p07bj.jpg)

可以看出是 post 请求，而且在每一栋楼、每一层获取时都是 post，并伴随着`_VIEWSTATE`的变化

然后在 FormData 着看到了数据

![](https://ws4.sinaimg.cn/large/006tKfTcly1fghd52k6qaj30fj0csq6c.jpg)

不断修改，selector 的 option可以发现关键字段`drlouming`、`drceng`、`drfangjian`分别代表着楼名、楼层、房间号。

*注*：楼名是01-18，分别代表1-16楼、18楼南、18楼北，楼层为楼名+层名，例如0101表示1号楼1层，房间名为楼名+楼层+房间，例如010103表示1号楼103

# 2.Python3实现

```python
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
##构建页面访问时的 headers
def getHeaders():
    return   {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        "Connection": "keep-alive",
        'Host': '219.218.115.151',
        'Referer': 'http://219.218.115.151/ISIMS3/default.aspx'
    }
##获取初始的 state
def getInit(url):
    res=urllib.request.urlopen(url)
    r = res.read().decode('gbk')
    state=BeautifulSoup(r,'html5lib').find(id='__VIEWSTATE')['value']
    return state
##获取楼时 state 的变化
def getLou(url,lou):
    state=getInit(url)
    data = {
        "__EVENTTARGET": 'drlouming',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": state,
        "__VIEWSTATEGENERATOR": 'B4EA4745',
        "drlouming": lou,
        "drceng": '',
        "drfangjian": ''
    }
    data = urllib.parse.urlencode(data).encode()
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(url,data,getHeaders())
    r = opener.open(req)
    r = r.read().decode('gbk')
    state = BeautifulSoup(r, 'html5lib').find(id='__VIEWSTATE')['value']
    # print(state)
    return state
##获取层数时发生的变换
def getCeng(url,lou,ceng):
    state=getLou(url,lou)
    data = {
        "__EVENTTARGET": 'drceng',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": state,
        "__VIEWSTATEGENERATOR": 'B4EA4745',
        "drlouming": lou,
        "drceng": ceng,
        "drfangjian": ''
    }
    data = urllib.parse.urlencode(data).encode()
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(url,data,getHeaders())
    r = opener.open(req)
    r = r.read().decode('gbk')
    state = BeautifulSoup(r, 'html5lib').find(id='__VIEWSTATE')['value']
    return state
##最终查询的 state
def getData(url,louming,ceng,fangjian):

    state= getCeng(url,louming,ceng)
    data = {
        "__EVENTTARGET": '',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": state,
        "__VIEWSTATEGENERATOR": 'B4EA4745',
        "drlouming": louming,
        "drceng": ceng,
        "drfangjian": fangjian,
        "radio": 'usedR',
        "ImageButton1.x": 42,
        "ImageButton1.y": 21
    }
    data=urllib.parse.urlencode(data).encode()
    return data
if __name__=='__main__':
    url = 'http://219.218.115.151/ISIMS3/Default.aspx'
    room='160112'#16楼1层12号房间  ===如何确定自己的房间上有说明
    req = urllib.request.Request(url,getData(url,room[0:2],room[0:4],room),getHeaders())
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    r = opener.open(req)
    r = r.read().decode('utf-8')
    soup=BeautifulSoup(r,'html5lib')
    print('剩余电量',soup.h6.contents[1].string)
```
# 3.构建微信自动回复



```python
import urllib
import http.cookiejar
from bs4 import BeautifulSoup
from wxpy import *
def getHeaders():
    return   {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        "Connection": "keep-alive",
        'Host': '219.218.115.151',
        'Referer': 'http://219.218.115.151/ISIMS3/default.aspx'
    }
def getInit(url):
    res=urllib.request.urlopen(url)
    r = res.read().decode('gbk')
    state=BeautifulSoup(r,'html5lib').find(id='__VIEWSTATE')['value']
    return state
def getLou(url,lou):
    state=getInit(url)
    data = {
        "__EVENTTARGET": 'drlouming',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": state,
        "__VIEWSTATEGENERATOR": 'B4EA4745',
        "drlouming": lou,
        "drceng": '',
        "drfangjian": ''
    }
    data = urllib.parse.urlencode(data).encode()
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(url,data,getHeaders())
    r = opener.open(req)
    r = r.read().decode('gbk')
    state = BeautifulSoup(r, 'html5lib').find(id='__VIEWSTATE')['value']
    # print(state)
    return state
def getCeng(url,lou,ceng):
    state=getLou(url,lou)
    data = {
        "__EVENTTARGET": 'drceng',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": state,
        "__VIEWSTATEGENERATOR": 'B4EA4745',
        "drlouming": lou,
        "drceng": ceng,
        "drfangjian": ''
    }
    data = urllib.parse.urlencode(data).encode()
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = urllib.request.Request(url,data,getHeaders())
    r = opener.open(req)
    r = r.read().decode('gbk')
    state = BeautifulSoup(r, 'html5lib').find(id='__VIEWSTATE')['value']
    return state
def getData(url,louming,ceng,fangjian):

    state= getCeng(url,louming,ceng)
    data = {
        "__EVENTTARGET": '',
        "__EVENTARGUMENT": '',
        "__LASTFOCUS": '',
        "__VIEWSTATE": state,
        "__VIEWSTATEGENERATOR": 'B4EA4745',
        "drlouming": louming,
        "drceng": ceng,
        "drfangjian": fangjian,
        "radio": 'usedR',
        "ImageButton1.x": 42,
        "ImageButton1.y": 21
    }
    data=urllib.parse.urlencode(data).encode()
    return data
if __name__=='__main__':
    url = 'http://219.218.115.151/ISIMS3/Default.aspx'
    bot = Bot()


    # 打印来自其他好友、群聊和公众号的消息
    @bot.register()
    def print_others(msg):
        # msg.
        print('收到消息: {} ({})'.format(msg.text, msg.type))
        room=msg.text
        req = urllib.request.Request(url,getData(url,room[0:2],room[0:4],room),getHeaders())
        cj = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
        r = opener.open(req)
        r = r.read().decode('utf-8')

        soup=BeautifulSoup(r,'html5lib')
        s='剩余电量'+ soup.h6.contents[1].string
        print('剩余电量', soup.h6.contents[1].string)
        chat=msg.sender.name
        friend = bot.friends().search(chat)[0]
        friend.send(s)
        print(msg.sender)

    embed()
```



