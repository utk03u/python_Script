import httplib
conn = httplib.HTTPConnection("www.python.org")
conn.request("HEAD", "/")
r1 = conn.getresponse()
print r1.status, r1.reason
