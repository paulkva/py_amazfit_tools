class DateType:
    Year = 0
    Month = 1
    Day = 2 

    Converter = {
        Year : "Year",
        Month : "Month",
        Day : "Day", 
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return DateType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in DateType.Converter:
            if strFlag == DateType.Converter[flag]:
                return flag
        return 0
