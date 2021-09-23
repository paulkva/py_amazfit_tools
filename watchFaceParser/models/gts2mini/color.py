import logging

class Color:
    def __init__(self, v):
        self.u = (v & 0xffffffff00000000) >> 32
        self.a = (v & 0xff000000) >> 24
        self.b = (v & 0xff0000) >> 16
        self.g = (v & 0xff00) >> 8
        self.r = (v & 0xff)
        #print ("A: %08x" %(v & 0xffffffffffffffffff))
        #print ("u: %02x" %self.u)


    def toJSON(self):
        return f"0x{self.u:08X}{self.a:02X}{self.b:02X}{self.g:02X}{self.r:02X}"


    @staticmethod
    def fromJSON(strValue):
        v = int(strValue, 16)	
        return v

