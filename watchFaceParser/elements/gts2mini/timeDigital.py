from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.time import Time

class TimeDigital:
    definitions = {
        1: {'Name': 'Hours', 'Type': Number},
        2: {'Name': 'HoursDataTypeImageIndex', 'Type': 'long'}, #probably HoursDataTypeImageIndex
        3: {'Name': 'PaddingZeroHours', 'Type': 'bool'},
        4: {'Name': 'DelimiterHours', 'Type': 'long'},
        5: {'Name': 'DelimiterMinutes', 'Type': 'long'},
        6: {'Name': 'HoursFollowPosition', 'Type': 'bool'}, # should be checked on watch, what does this do
        7: {'Name': 'Unknown7', 'Type': 'long?'},
        8: {'Name': 'Time', 'Type': Time},
    }

