from Crypto.Cipher import AES
import base64
from binascii import b2a_hex, a2b_hex

class AESCipher:
    def __init__(self,key):
        self.key = key
        self.mode = AES.MODE_CBC
     
    def encrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')

        length = 16
        count = len(text)
        if count < length:
            add = (length-count)
            #\0 backspace
            text = text + ('\0' * add)
        elif count > length:
            add = (length-(count % length))
            text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)

        return b2a_hex(self.ciphertext)
     
    def decrypt(self,text):
        cryptor = AES.new(self.key,self.mode,b'0000000000000000')
        plain_text  = cryptor.decrypt(a2b_hex(text))
        return plain_text.rstrip('\0')
