from watchFaceParser.elements.gtr2.basicElements.text import Text 
from watchFaceParser.models.gtr2.dateType import DateType
from watchFaceParser.models.gtr2.combingModeType import CombingModeType
from watchFaceParser.models.gtr2.digitType import DigitType
from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 

class DigitalCommonDigit:
    definitions = { 
        1: { 'Name': 'Type', 'Type': DigitType},
        2: { 'Name': 'CombingMode', 'Type': CombingModeType},
        3: { 'Name': 'Digit', 'Type': Text}, 
        4: { 'Name': 'Separator', 'Type': ImageCoord}, 
    }

