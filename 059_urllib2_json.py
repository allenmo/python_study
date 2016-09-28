import urllib, urllib2, json

def http_post():
    url='http://192.168.1.188/prog_check.php'
    values = {'user':'Smith', 'passwd':'123456'}

    jdata = json.dumps(values)
    req = urllib2.Request(url, jdata)
    response = urllib2.urlopen(req)
    return response.read()

resp = http_post()
print resp
