import logging

class IconSet:
    def __init__(self, v):
        self.firstimageindex = v[0].getValue()
        #print ("FirstImageIndex",self.firstimageindex)
        #print ("Coordinates",len(v[1::]))
        self.coordinates = [ {"X":c.getChildren()[0].getValue(), "Y":c.getChildren()[1].getValue()} for c in v[1::] ]
        #self.r = (v & 0xff000000) >> 24
        #self.g = (v & 0xff0000) >> 16
        #self.b = (v & 0xff00) >> 8
        #self.a = (v & 0xff)
        pass


    def toJSON(self):
        return {"FirstImageIndex":self.firstimageindex, "Coordinates":self.coordinates }


    @staticmethod
    def fromJSON(strValue):
        #print ("FROMJSON",strValue)
        # = int(strValue, 16)
        return strValue

