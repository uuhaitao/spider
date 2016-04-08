import urllib2
import urllib


def doGet(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()

def doPost():
    values = {}
    values['username'] = "1016903103@qq.com"
    values['password'] = "XXXX"
    data = urllib.urlencode(values)
    url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
    request = urllib2.Request(url,data)
    response = urllib2.urlopen(request)
    print response.read()



base_url = "https://book.douban.com/subject/2035162/"
doGet(base_url)






