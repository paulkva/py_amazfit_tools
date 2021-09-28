class ShortcutType:
    Calories = 5
    Music = 16
   
    Converter = {
        Calories : "Calories", 
        Music  : "Music",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return ShortcutType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ShortcutType.Converter:
            if strFlag == ShortcutType.Converter[flag]:
                return flag
        return 0
