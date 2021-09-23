from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.time import Time

class TimeDigital:
    definitions = {
        1: {'Name': 'TimeOneLine', 'Type': Number},
        3: {'Name': 'Unknown3', 'Type': 'long'},
        4: {'Name': 'DelimiterImageIndex', 'Type': 'long'},
        6: {'Name': 'Unknown6', 'Type': 'long'},
        8: {'Name': 'Time', 'Type': Time},
    }

