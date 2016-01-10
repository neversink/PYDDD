# coding:utf-8
import urllib2
import re


class PYDDD:
    url = 'http://pyddd.com/index.html'

    def getPage(self):
        try:
            request = urllib2.Request(self.url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u'链接失败，错误原因:', e.reason
                return None

    def getItems(self):
        page = self.getPage()
        pattern = re.compile('<div class="hot_list_n w520 fr">.*?title="(.*?)" href="(.*?)".*?>', re.S)
        items = re.findall(pattern, page)

        # print type(items)
        # print len(items)
        # print type(items[0])
        for item in items:
            for s in item:
                print s


pyddd = PYDDD()
# pyddd.getPage()
pyddd.getItems()
