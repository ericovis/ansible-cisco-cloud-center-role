#!/usr/bin/env python
ENCODING='utf-8'
import configobj
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mgmtserverdnsName", help="mgmtserver.dnsName is IP address or FQDN of CCM VM")
args = parser.parse_args()

inputFile = '/usr/local/osmosix/etc/gateway_config.properties'
outputFile = inputFile


#http://www.programiz.com/python-programming/dictionary
myDict = {
'mgmtserver.dnsName' : args.mgmtserverdnsName
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
