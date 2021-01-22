from watchFaceParser.elements.gtr2.basicElements.text import Text 
from watchFaceParser.models.gtr2.dateType import DateType
from watchFaceParser.models.gtr2.combingModeType import CombingModeType
from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 

class DigitalDateDigit:
    definitions = { 
        1: { 'Name': 'DateType', 'Type': DateType},
        2: { 'Name': 'CombingMode', 'Type': CombingModeType},
        3: { 'Name': 'Digit', 'Type': Text}, 
        4: { 'Name': 'Separator', 'Type': ImageCoord}, 
    }

