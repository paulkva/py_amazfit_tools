class CombingModeType:
    Single = 1
    Follow = 0

    Converter = {
        Single : "Single",
        Follow : "Follow", 
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return CombingModeType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in CombingModeType.Converter:
            if strFlag == CombingModeType.Converter[flag]:
                return flag
        return 0
