from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class MonthAndDayAlt:
    definitions = {
        1: {'Name': 'Month', 'Type': Number},
        4: {'Name': 'Day', 'Type': Number},
    }
