#!/usr/bin/env python
ENCODING='utf-8'
import configobj
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("rabbitgatewaybrokerHost", help=" e.g.  cc amqp dns name e.g. ncwt-clab-cca02")
parser.add_argument("rabbitgatewaybrokerPort", help=" e.g.  cc amqp port, standard port: 5671")
args = parser.parse_args()

# /usr/local/tomcat/webapps/ROOT/WEB-INF/rabbit-gateway.properties
inputFile = '/usr/local/tomcat/webapps/ROOT/WEB-INF/rabbit-gateway.properties'
outputFile = inputFile

#http://www.programiz.com/python-programming/dictionary
myDict = {
'rabbit.gateway.brokerHost': args.rabbitgatewaybrokerHost,
'rabbit.gateway.brokerPort': args.rabbitgatewaybrokerPort,
'rabbit.gateway.cluster.addresses': args.rabbitgatewaybrokerHost+":"+args.rabbitgatewaybrokerPort
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
