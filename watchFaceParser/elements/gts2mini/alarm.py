from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image

class AlarmTime:
    definitions = {
        1: { 'Name': 'Hours', 'Type': Number},
        2: { 'Name': 'Minutes', 'Type': Number},
        5: { 'Name': 'DelimiterMinutes', 'Type': 'long'},
        7: { 'Name': 'PaddingZeroHours', 'Type': 'bool'},
        8: { 'Name': 'PaddingZeroMinutes', 'Type': 'bool'},
        11: { 'Name': 'Unknown11', 'Type': 'bool'},
    }

class Alarm:
    definitions = {
        3: {'Name': 'NoAlarmImage', 'Type': Image},
        5: {'Name': 'AlarmImage', 'Type': Image},
        7: {'Name': 'Minutes', 'Type': AlarmTime},
    }

