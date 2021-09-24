from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.time import Time

class TimeDigital:
    definitions = {
        1: {'Name': 'Hours', 'Type': Number},
        2: {'Name': 'DelimiterImageIndex', 'Type': 'long'},
        3: {'Name': 'Unknown3', 'Type': 'long'},
        4: {'Name': 'DelimiterImageIndex', 'Type': 'long'},
        5: {'Name': 'Unknown2', 'Type': 'long?'},
        6: {'Name': 'Unknown6', 'Type': 'long'},
        7: {'Name': 'Unknown2', 'Type': 'long?'},
        8: {'Name': 'Time', 'Type': Time},
    }

