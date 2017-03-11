import serial
import threading;
import time
import platform
import signal
from PyQt4 import QtCore
import binascii
import array
from serialport import httpclient
import asyncore
import logging
import socket
from cStringIO import StringIO
import urlparse
from serialport import registry

class SerialPortContext(QtCore.QObject,object):
    _recvSignal_ = QtCore.pyqtSignal(str,name="recvsignal")

    def __init__(self,port = None,baud = 115200,bits = 8,stop_bits = 1,check=None):
        super(SerialPortContext,self).__init__()
        self._port_ = port
        #if self._port_ == None:
        #    if platform.system() == "Windows":
        #        self._port_ = 1
        #    else:
        #        self._port_ = "/dev/ttyUSB0"
        self._port_ = "/dev/ttyUSB0"
        #print("Open port %s", self._port_);

        self._baud_ = baud
        if self._baud_ <= 50 or self._baud_ > 115200:
            self._baud_ = 115200
        self._baud_ = 9600
        self._is_running_ = False
        self._all_counts_ = 0
        self._recv_counts_ = 0
        self._sent_counts_ = 0
        self._serial_port_ = None
        self.my_string = ""
        self.reg = registry.Registry()
        self.reg.readDB()
        self.sURL = 'http://www.YOURDNS.com/dashboard/cgiserial.php'
        self.sURL = self.sURL + '?email=' + self.reg.getEmail() + '&username=' + self.reg.getUsername() + '&password=' + self.reg.getPassword() + '&sDeviceUUID=' + self.reg.getsDeviceUUID()

    def getAllCounts(self):
        return self._all_counts_
    
    def getSendCounts(self):
        return self._sent_counts_
    
    def getRecvCounts(self):
        return self._recv_counts_
       
    def clearAllCounts(self):
        self._all_counts_ = 0
        self._recv_counts_ = 0
        self._sent_counts_ = 0
        
    def clearRecvCounts(self):
        self._recv_counts_ = 0
    def clearSentCounts(self):
        self._sent_counts_ = 0
       
    def setRXD(self,value):
        self._RXD_ = value
        if self._serial_port_ == None:
            self._RXD_ = value
        else:
            self._serial_port_.setRTS(value)
    
    def setCD(self,value):
        self._CD_ = value
        if self._serial_port_ == None:
            self._CD_ = value
        else:
            self._serial_port_.setDTR(value)
        
    def setDTR(self,value = True):
        self._DTR_ = value
        if self._serial_port_ == None:
            self._DTR_ = value
        else:
            self._serial_port_.setDTR(value)
    def setRTS(self,value = True):
        self._RTS_ = value
        if self._serial_port_ == None:
            self._RTS_ = value
        else:
            self._serial_port_.setRTS(value)
        
    def __recv_func__(self,context):
        #print("start serial port")

        
        #print(sURL)
        while context.isRunning():
            line = context._serial_port_.read()
            #self.my_string.append(line)
            self.my_string = self.my_string + line;
            if line == '\r':
                try:
                    self.my_string = self.sURL + "&serial=" + self.my_string
                    #print("%s", self.sURL)
                    c = httpclient.HttpClient(self.my_string)
                    asyncore.loop()
                    response_body = c.read_buffer.getvalue()
                    print "HTTP sent " + c.url, 'got', len(response_body), 'bytes' 
                    print response_body
                    self.my_string = ""

                except:
                    print "HTTP exception"
            context._recvSignal_.emit(line)
            buf_len = len(line)
            self._recv_counts_ += buf_len
            self._all_counts_ += self._recv_counts_ + self._recv_counts_
            
        print("close serial port")
     
    def registerReceivedCallback(self,callback):
        self._recvSignal_.connect(callback)
           
    def open(self):
        self._serial_port_ = serial.Serial(self._port_,int(self._baud_))
        self._serial_port_.setRTS(self._RTS_)
        self._serial_port_.setDTR(self._DTR_)
        self._received_thread_ = threading.Thread(target = self.__recv_func__,args=(self,))
        self._is_running_ = True
        self._received_thread_.setDaemon(True)
        self._received_thread_.setName("SerialPortRecvThread")
        self._received_thread_.start()
        
         
    def close(self):
        print("serial context is running: %s" % self.isRunning())
        self._is_running_ = False
        self._serial_port_.close()
            
    def send(self,data,isHex):
        if not self.isRunning():
            return
        if not isHex:
            buff = data.encode("utf-8")
            self._serial_port_.write(buff)
            buf_len = len(data)
            self._sent_counts_ += buf_len
            self._all_counts_ += self._recv_counts_ + self._recv_counts_

        else:
            hex_datas = data.split(' ')
            buffer = ''
            for d in hex_datas:
                buffer += d
#             print(buffer.decode('hex'))
            buf_len = len(buffer)
            self._sent_counts_ += buf_len
            self._all_counts_ += self._recv_counts_ + self._recv_counts_
            self._serial_port_.write(buffer.decode("hex"))
      
    def isRunning(self):
        return self._is_running_ and self._serial_port_.isOpen()
         
        
        