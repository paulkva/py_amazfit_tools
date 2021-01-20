class TimeType:
    Hour = 0
    Minute = 1
    Second = 2 

    Converter = {
        Hour : "Hour",
        Minute : "Minute",
        Second : "Second", 
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return TimeType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in TimeType.Converter:
            if strFlag == TimeType.Converter[flag]:
                return flag
        return 0
