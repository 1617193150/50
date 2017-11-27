Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import urllib2
>>> url = 'http://hr.163.com/position/list.do?positionName=Java'
>>> headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
>>> req = urllib2.Request(url,headers=headers)
>>> response = urllib2.urlopen(req)
>>> with open ('D:/test.html','wb') as f:
	f.write(response.read())

	
>>> 
