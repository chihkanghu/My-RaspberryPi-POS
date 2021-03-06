import asyncore
import logging
import socket
from cStringIO import StringIO
import urlparse

class HttpClient(asyncore.dispatcher):

    def __init__(self, url):
        try:
            self.url = url
            print url;
            self.logger = logging.getLogger(self.url)
            self.parsed_url = urlparse.urlparse(url)
            asyncore.dispatcher.__init__(self)
            self.write_buffer = 'GET %s HTTP/1.0\r\n\r\n' % self.url
            self.read_buffer = StringIO()
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            address = (self.parsed_url.netloc, 80)
            self.logger.debug('connecting to %s', address)
            self.connect(address)
        except:
            print "HTTP client exception"

    def handle_connect(self):
        self.logger.debug('handle_connect()')

    def handle_close(self):
        self.logger.debug('handle_close()')
        self.close()

    def writable(self):
        is_writable = (len(self.write_buffer) > 0)
        if is_writable:
            self.logger.debug('writable() -> %s', is_writable)
        return is_writable
    
    def readable(self):
        self.logger.debug('readable() -> True')
        return True

    def handle_write(self):
        sent = self.send(self.write_buffer)
        self.logger.debug('handle_write() -> "%s"', self.write_buffer[:sent])
        self.write_buffer = self.write_buffer[sent:]

    def handle_read(self):
        data = self.recv(8192)
        self.logger.debug('handle_read() -> %d bytes', len(data))
        self.read_buffer.write(data)
