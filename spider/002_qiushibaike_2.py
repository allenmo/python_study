# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

#糗事百科爬虫类
class QSBK:

    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Window NT)'
        #初始化headers
        self.headers = { 'User-Agent' : self.user_agent }
        #存放段子的变量，每一个元素（3维）是每一页的段子们（2维）
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False
    
    #传入某一页的索引，获得页面代码html
    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            #构建请求的request
            request = urllib2.Request(url, headers = self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为UTF-8编码， 其实本来就是，不用转
            pageCode = response.read()#.decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接糗事百科失败， 错误原因:", e.reason
                return None

    #传入某一页的索引，调用getPage()，返回本页不带图片的段子列表
    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败...."
            return None
        pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?"content">(.*?)</div>(.*?)<i class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)
        #item[0]是发布者， item[1]是内容， item[2]是图片内容， item[3]是点赞数
        #用来存储每页的段子们
        pageStories = []
        #去掉含图片的段子
        for item in items:
            #是否含有图片
            haveImg = re.search("img", item[2])
            #如果不含图片， 把它存入pageStories的list中
            if not haveImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR, '\n', item[1])
                pageStories.append([item[0].strip(), text.strip(), item[2].strip(), item[3].strip()])
        return pageStories
    
    #加载并提取页面的内容， 加入到self.stories列表中
    def loadPage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1
                    
    #调用该方法， 每次敲回车打印输出一个段子
    def getOneStory(self, pageStories, page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print "第%d页\t发布人：%s\t赞：%s\n%s" %(page, story[0], story[3], story[1])

    #开始方法
    def start(self):
        print "正在读取糗事百科，按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        #局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)

spider = QSBK()
spider.start()








