class LangCodeType: 
    Zh = 0
    ZhHant = 1 
    All = 2

    Converter = {
        Zh : "Zh",
        ZhHant : "ZhHant", 
        All : "All",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return LangCodeType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in LangCodeType.Converter:
            if strFlag == LangCodeType.Converter[flag]:
                return flag
        return 0
