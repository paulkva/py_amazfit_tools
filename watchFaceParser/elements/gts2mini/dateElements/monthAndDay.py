from watchFaceParser.elements.gts2mini.dateElements.separateMonthAndDay import SeparateMonthAndDay
from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet

class MonthAndDay:
    definitions = {
        2: { 'Name': 'Month', 'Type': Number},
        3: { 'Name': 'Day', 'Type': Number},
        4: {'Name': 'Unknown4', 'Type': 'long'},
        5: {'Name': 'Unknown5', 'Type': 'long'},
        6: {'Name': 'Month1', 'Type': ImageSet},
        7: {'Name': 'Month2', 'Type': ImageSet},
        12: {'Name': 'DateDelimiterImageIndex', 'Type': 'long'},
        13: {'Name': 'UnknownImageIndex13', 'Type': 'long'},
    }
