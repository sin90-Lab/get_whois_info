# -*- coding: utf-8 -*-

import whois
import json
import argparse
# import pythonwhois
import datetime
import sys

#adding argument parser
parser = argparse.ArgumentParser(description="args parser")
parser.add_argument("-f","--file",action="store")
args = parser.parse_args()

#make exception later 
f=open(args.file, "r")
data=f.read()

#find whois informatino
domain = whois.query(data)
parsed = domain.__dict__

#change unparseble data

# use try except 
if 'last_updated' in parsed: 
    parsed["last_updated"] = parsed["last_updated"].isoformat()
if 'expiration_date' in parsed:
    parsed["expiration_date"] = parsed["expiration_date"].isoformat()
if 'creation_date' in parsed:
    parsed["creation_date"] = parsed["creation_date"].isoformat()

if 'name_servers' in parsed:
    parsed["name_servers"]=list(parsed["name_servers"])
    print type(parsed["name_servers"])

#print it as jason
result=json.dumps(parsed)
print result
f.close()
out=open('result.txt','w')
out.write(result)
out.close()
