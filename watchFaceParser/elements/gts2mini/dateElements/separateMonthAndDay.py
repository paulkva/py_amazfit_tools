from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet

class SeparateMonthAndDay:
    definitions = {
        1: { 'Name': 'Month', 'Type': Number},
        2: { 'Name': 'MonthName', 'Type': ImageSet},
        3: { 'Name': 'Day', 'Type': Number},
    }
