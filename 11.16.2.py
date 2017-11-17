Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: D:/利大163  13/11.16.1.py =====================
>>> import urllib
>>> import urllib2
>>> 
>>> url = 'http://www.baidu.com/'
>>> user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
>>> values = {'username' : 'cqc',  'password' : 'XXXX' }
>>> headers = { 'User-Agent' : user_agent }
>>> data = urllib.urlencode(values)
>>> request = urllib2.Request(url, data, headers)
>>> response = urllib2.urlopen(request)
>>> page = response.read()
>>> page = response.read(1000)
>>> page
''
>>> 
===================== RESTART: D:/利大163  13/11.16.1.py =====================
>>> import urllib
>>> import urllib2
>>> 
>>> url = 'http://www.baidu.com'
>>> user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
>>> vallues = {'username':'cqc','password':'XXXX'}
>>> headers = {'User-Agent':user_agent}
>>> data = urllib.urlencode(values)

Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data = urllib.urlencode(values)
NameError: name 'values' is not defined
>>> data = urllib.urlencode(values)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    data = urllib.urlencode(values)
NameError: name 'values' is not defined
>>> data = urllib.urlencode(vallues)
>>> request = urllib2.Request(url,data,headers)
>>> response= urllib2.urlopen(request)
>>> page = response.read(1000)
>>> page
'<!DOCTYPE html>\r\n<!--STATUS OK-->\r\n<html>\r\n<head>\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\r\n    <meta http-equiv="content-type" content="text/html;charset=utf-8">\r\n    <meta content="always" name="referrer">\r\n    <script src="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/nocache/imgdata/seErrorRec.js"></script>\r\n    <title>\xe9\xa1\xb5\xe9\x9d\xa2\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8_\xe7\x99\xbe\xe5\xba\xa6\xe6\x90\x9c\xe7\xb4\xa2</title>\r\n    <style data-for="result">\r\n        body {color: #333; background: #fff; padding: 0; margin: 0; position: relative; min-width: 700px; font-family: arial; font-size: 12px }\r\n        p, form, ol, ul, li, dl, dt, dd, h3 {margin: 0; padding: 0; list-style: none }\r\n        input {padding-top: 0; padding-bottom: 0; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box } img {border: none; }\r\n        .logo {width: 117px; height: 38px; cursor: pointer }\r\n         #wrapper {_zoom: 1 }\r\n        #head {padding-left: 35px; margin-bottom: 20px; width: 900px }\r\n        .fm {clea'
>>> 
