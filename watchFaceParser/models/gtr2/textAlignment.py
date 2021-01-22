class TextAlignmentGTR2:
    Left = 0
    Center = 1
    Right = 2

    Converter = { 
        Left : "Left",
        Right : "Right",
        Center : "Center",
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return TextAlignmentGTR2.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in TextAlignmentGTR2.Converter:
            if strFlag == TextAlignmentGTR2.Converter[flag]:
                return flag
        return 0
