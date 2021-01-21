from watchFaceParser.elements.gtr2.basicElements.text import Text 
from watchFaceParser.models.gtr2.timeType import TimeType
from watchFaceParser.models.gtr2.combingModeType import CombingModeType
from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 

class DigitalDigit:
    definitions = { 
        1: { 'Name': 'TimeType', 'Type': TimeType},
        2: { 'Name': 'CombingMode', 'Type': CombingModeType},
        3: { 'Name': 'Digits', 'Type': Text}, 
        4: { 'Name': 'Separator', 'Type': ImageCoord}, 
    }

