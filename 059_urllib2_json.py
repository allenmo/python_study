import urllib, urllib2, json

def http_post():
    url='http://192.168.1.88/prog/prog_check.php'
    #url='http://allstack.net/prog/prog_check.php'
    values = {'user':'Smith', 'passwd':'123456'}

    jdata = json.dumps(values,sort_keys=True, indent=4)
    req = urllib2.Request(url, jdata)
    response = urllib2.urlopen(req)
    return response.read()

resp = http_post()
print resp, "\n"
jobj = json.loads(resp)
print jobj, "\n"
numbers = jobj['numbers']
print numbers
