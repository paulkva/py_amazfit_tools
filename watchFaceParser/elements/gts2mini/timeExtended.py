from watchFaceParser.elements.gts2mini.timeElements.twoDigits import TwoDigits
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.shortcutsElements.element import Element

class TimeSeparateDigits:
    definitions = {
        1: {'Name': 'Hours', 'Type': TwoDigits},
        2: {'Name': 'Minutes', 'Type': TwoDigits},
        3: {'Name': 'Seconds', 'Type': TwoDigits},
        4: {'Name': 'Unknown4', 'Type': 'long?'},
        5: {'Name': 'Separator', 'Type': Image}, # separator hours ?
        6: {'Name': 'Unknown6', 'Type': Image}, # separator minutes ?
        7: {'Name': 'Unknown7', 'Type': 'long?'}, # separator seconds ?
        8: {'Name': 'Unknown8', 'Type': 'long?'},
    }

class TimeExtended:
    definitions = {
        1: {'Name': 'TimeSeparateDigits', 'Type': TimeSeparateDigits},
        2: {'Name': 'SunsetTimeOneLine', 'Type': Number},
        3: {'Name': 'DelimiterSunsetImageIndex', 'Type': 'long'},
        4: {'Name': 'SunriseTimeOneLine', 'Type': Number},
        5: {'Name': 'DelimiterSunriseImageIndex', 'Type': 'long'},
        6: {'Name': 'SunsetIcon', 'Type': Image},
        7: {'Name': 'SunriseIcon', 'Type': Image},
        8: {'Name': 'SunsetShortcut', 'Type': Element},
        9: {'Name': 'SunriseShortcut', 'Type': Element},
    }

