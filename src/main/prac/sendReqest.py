import urllib2




base_url = "https://book.douban.com/subject/2035162/"

def doGet(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()

doGet(base_url)





