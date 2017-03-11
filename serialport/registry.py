# -*- coding: utf-8 -*
import asyncore
import logging
import socket
from cStringIO import StringIO
import urlparse
import json
import codecs
import io
from serialport import AESCipher
import base64
     
def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"
 
  return cpuserial

class Registry():

    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.port = "/dev/ttyUSB0"
        self.baud = "9600"
        self.check = ""
        self.parity = ""
        self.stop = ""
        self.sDeviceUUID =""
        self.AES = AESCipher.AESCipher("aaaaaaaaaaaaaaaa")

    def setUsername(self, value):
        value = str(value)
        self.username = self.AES.encrypt(value)

    def setPassword(self, value):
        value = str(value)
        self.password = self.AES.encrypt(value)

    def setEmail(self, value):
        value = str(value)
        self.email = self.AES.encrypt(value)

    def setPort(self, value):
        self.port = value

    def setBaud(self, value):
        self.baud = value

    def setCheck(self, value): 
        self.check = value

    def setParity(self, value):
        self.parity = value

    def setStop(self, value):
        self.stop = value

    def setsDeviceUUID(self, value):
        self.sDeviceUUID = value

    def getUsername(self):
        return self.AES.decrypt(self.username)

    def getPassword(self):
        return self.AES.decrypt(self.password)

    def getEmail(self):
        return self.AES.decrypt(self.email)

    def getPort(self):
        return self.port

    def getBaud(self):
        return self.baud 

    def getCheck(self): 
        return self.check

    def getParity(self):
        return self.parity

    def getStop(self):
        return self.stop

    def getsDeviceUUID(self):
        suuid = getserial()
        return suuid

    def writeDB(self):
        print("Class Write DB")
        data = {}  
        data['people'] = []  
        data['people'].append({  
            'email': self.email,
            'account': self.username,
            'pass': self.password,
            'port': self.port,
            'baud' : self.baud,
            'check' : self.check,
            'parity' : self.parity,
            'stop' : self.stop,
            'sDeviceUUID' : self.sDeviceUUID
        })

        with open('data.txt', 'w') as outfile:  
            #print (data)
            outfile.write(json.dumps(data))
            #json.dump(data, outfile)  

    def readDB(self):
        try:
            with open('data.txt') as json_file: 
                data = json.load(json_file)
                for p in data['people']:
                    self.email = p['email']
                    self.username = p['account']
                    self.password = p['pass']
                    self.port = p['port']
                    self.baud = p['baud']
                    self.parity = p['parity']
                    self.stop = p['stop']
                    self.sDeviceUUID = p['sDeviceUUID']  
        except:
            print("Create db")
            self.writeDB()
            with open('data.txt') as json_file:  
                data = json.load(json_file)
                for p in data['people']:
                    self.email = p['email']
                    self.username = p['account']
                    self.password = p['pass']
                    self.port = p['port']
                    self.baud = p['baud']
                    self.parity = p['parity']
                    self.stop = p['stop']
                    self.sDeviceUUID = p['sDeviceUUID']
