#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests

resp = requests.get('https://www.baidu.com')
print resp