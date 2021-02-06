class DigitType:
    Min = 1
    Max = 2


    Converter = {
        Min : "Min",
        Max : "Max", 
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return DigitType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in DigitType.Converter:
            if strFlag == DigitType.Converter[flag]:
                return flag
        return 0
