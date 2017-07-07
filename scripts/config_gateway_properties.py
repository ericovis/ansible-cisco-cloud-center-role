#!/usr/bin/env python
ENCODING='utf-8'
import configobj
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("monitorid", help="monitorId must be unique to identify the monitor instance so that multiple monitor instances can use the same cloud accounts to do health check without interfering with each other")
parser.add_argument("mgmtserverhost", help="mgmtserver host name is required to retrieve cloud image information")
args = parser.parse_args()

# /usr/local/tomcat/webapps/ROOT/WEB-INF/gateway.properties
inputFile = '/usr/local/tomcat/webapps/ROOT/WEB-INF/gateway.properties'
outputFile = inputFile

#http://www.programiz.com/python-programming/dictionary
myDict = {
'monitor.id': args.monitorid,
'mgmtserver.host': args.mgmtserverhost
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
