import re
ret=re.match(r'<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>','<html><h1>www.baidu.com</h1><html>')

ret.group

