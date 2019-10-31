#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cgi

html_body = """
<!DOCTYPE html>
<html>
<head>
<title>受信したデータを表示</title>
<style>
h1 {
font-size: 3em;
}
</style>
</head>
<body>
<pre>%s</pre>
</body>
</html>
"""

form = cgi.FieldStorage()
text = form.getvalue('text','').replace('\n','') + '\n'

file = open('a.java','w')
file.write(text)
file.close()

print(html_body % (text))
# print(html_body % (form))