# -*- coding:utf-8 -*-
import urllib2


proxy = {"http":"119.146.68.10:8118"}
proxy_s = urllib2.ProxyHandler(proxy)
opener = urllib2.build_opener(proxy_s)
urllib2.install_opener(opener)
content = urllib2.urlopen("http://ip.catr.cn/").read()
print content

