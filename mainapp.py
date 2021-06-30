#!/usr/bin/python3


import cgi
import subprocess as sp

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
akey = sp.getstatusoutput("sudo " + cmd +" --kubeconfig /admin.conf")
if akey[0] == 0:
    print(akey[1])
else:
    print("Error Occured: {} ".format(akey[1]))

