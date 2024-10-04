
# http
import http.client

#'https://dummyjson.com/todos'
con = http.client.HTTPSConnection('dummyjson.com')
con.request("GET", '/')
response = con.getresponse()
print(response.status) #200
print(response.headers) #headers
print(response.read) # response data


import math 
res= math.sqrt(16)
# print(res)


import os #file system
a = os.getcwd
# print(a)

#sys
import sys
# print(sys.version)
import random 
number = random.randint(1, 100)
print(number)

#time
import time 
print(time.time())

#json
import json 

myself ='{"name":"mehedi"}'
jsonmy = json.loads(myself)

print(jsonmy['name'])


#subprocess
import subprocess

result = subprocess.run(
    ['python' ,'--version'],
    capture_output=True,
    text=True,
)
print(result.stdout) 

#hashlib
import hashlib

password =b"mahedi12345"
print(password)
hashobj= hashlib.md5(password)
print(hashobj.hexdigest()) #Unknown code


#csv
import csv

with open("new.csv","w") as file:
    writerr = csv.writer(file)
    writerr.writerow(['name','mehedi'])
    writerr.writerow(['age',21])

