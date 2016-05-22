import urlparse
url = 'http://www.somethong.com:1234/foo/index.html?name=allen&age=32#second'
up = urlparse.urlparse(url)
print("scheme:%s"% up.scheme)
print("hostname:%s"% up.hostname)
print("port:%s"% up.port)
print("path:%s"% up.path)
print("query:%s"% up.query)
print("fragment:%s"% up.fragment)


