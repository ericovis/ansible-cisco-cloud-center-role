#!/usr/bin/env python
ENCODING='utf-8'
import configobj
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("connectionbrokerhost", help=" e.g.  cc amqp dns name e.g. ncwt-clab-cca02")
parser.add_argument("connectionbrokerport1", help=" e.g.  7788")
parser.add_argument("connectionbrokerport2", help=" e.g.  7789")
args = parser.parse_args()

# 
inputFile = '/usr/local/osmosix/etc/rev_connection.properties'
outputFile = inputFile

#http://www.programiz.com/python-programming/dictionary
myDict = {
'connection.broker.host': args.connectionbrokerhost,
'connection.broker.port1': args.connectionbrokerport1,
'connection.broker.port2': args.connectionbrokerport2
}

propertyDict = {}
#http://stackoverflow.com/questions/11555468/how-should-i-read-a-file-line-by-line-in-python
with open(inputFile) as fp:
 for line in fp:
  if '=' in line:
   key,value = line.split("=", 1)
   propertyDict[key] = value.rstrip()

propertyDict.update(myDict)

with open(outputFile, 'w') as f:
 f.writelines('{}={}\n'.format(k,v) for k, v in propertyDict.items())
 f.write('\n')
