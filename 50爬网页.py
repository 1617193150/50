import urllib
import urllib2
import re
import thread
import time
user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
url = 'https://hr.163.com/position/list.do?positionName=Java'
headers = {'User-Agent': user_agent}
result = urllib2.Request( url, headers=headers )
response = urllib2.urlopen(result)
pageCode = response.read().decode('utf-8')
pattern = re.compile('<a class=.*?>(.*?)</a>.*?<td>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>',re.S)
items = re.findall(pattern, pageCode)
for i in items:
        input = raw_input()
        for g in i:

            print g

