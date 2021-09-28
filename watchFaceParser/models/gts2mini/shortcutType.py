class ShortcutType:
    Unknown0 = 0
    Unknown1 = 1
    Unknown2 = 2
    Unknown3 = 3
    Unknown4 = 4
    Calories = 5
    Unknown6 = 6
    Unknown7 = 7
    Unknown8 = 8
    Unknown9 = 9
    Unknown10 = 10
    Unknown11 = 11
    Unknown12 = 12
    Unknown13 = 13
    Unknown14 = 14
    Unknown15 = 15
    Weather = 16
    Unknown17 = 17
    Unknown18 = 18
    Unknown19 = 19
    Unknown20 = 20
    Unknown21 = 21
    Unknown22 = 22
    Unknown23 = 23
    Unknown24 = 24
    Pulse = 25

    Converter = {
        Unknown0: "Unknown0",
        Unknown1: "Unknown1",
        Unknown2: "Unknown2",
        Unknown3: "Unknown3",
        Unknown4: "Unknown4",
        Calories : "Calories",
        Unknown6: "Unknown6",
        Unknown7: "Unknown7",
        Unknown8: "Unknown8",
        Unknown9: "Unknown9",
        Unknown10: "Unknown10",
        Unknown11: "Unknown11",
        Unknown12: "Unknown12",
        Unknown13: "Unknown13",
        Unknown14: "Unknown14",
        Unknown15: "Unknown15",
        Weather  : "Weather",
        Unknown17: "Unknown17",
        Unknown18: "Unknown18",
        Unknown19: "Unknown19",
        Unknown20: "Unknown20",
        Unknown21: "Unknown21",
        Unknown22: "Unknown22",
        Unknown23: "Unknown23",
        Unknown24: "Unknown24",
        Pulse: "Pulse",
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
