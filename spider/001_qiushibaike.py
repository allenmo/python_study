# -*- coding: utf-8 -*-

import urllib
import urllib2
import re

page =11
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    
    content = response.read()#.decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?"content">(.*?)</div>(.*?)<i class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImag = re.search("img", item[2])
        if not haveImag:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, '\n', item[1])
            print text.strip(),"\n", item[0].strip(),"   ", item[3].strip(), "\n------------------------------------------------"


except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
