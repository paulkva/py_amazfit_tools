from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.date import Date
from watchFaceParser.elements.gts2mini.timeElements.amPmIcon import AmPmIcon

class DateBlock:
    definitions = {
        1: { 'Name': 'Date', 'Type': Date},
        2: { 'Name': 'AmPm', 'Type': AmPmIcon},
        4: { 'Name': 'Weekday1', 'Type': ImageSet},
        5: { 'Name': 'Weekday2', 'Type': ImageSet},
        6: { 'Name': 'Weekday3', 'Type': ImageSet},
    }

