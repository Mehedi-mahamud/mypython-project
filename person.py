



#pyton ---> json + adding a file 
'''
import json
personOBJ = {
    "name" : "mehdei",
    "work": "programer",
    "salary": 25000,
    "work daily": True
    }
 

with open("learn.json","w") as personjsonF:
    json.dump(personOBJ,personjsonF, indent=4)



with open ("learn.json","r") as pythonjsonF:
   pythonOBJ=json.load(pythonjsonF)
   pythonjson=json.dumps(pythonOBJ, indent=4)
   print( pythonjson)
'''

from calculator import add,sub,mul,div

print(add(1,3))
sub(1,3)
mul(1,3)
div(1,3)