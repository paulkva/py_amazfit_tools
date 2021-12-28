from watchFaceParser.elements.gts2mini.basicElements.imageSet import ImageSet
from watchFaceParser.elements.gts2mini.basicElements.image import Image
from watchFaceParser.elements.gts2mini.date import Date
from watchFaceParser.elements.gts2mini.timeElements.amPmIcon import AmPmIcon
from watchFaceParser.elements.gts2mini.progress import Progress

class DateBlock:
    definitions = {
        1: { 'Name': 'Date', 'Type': Date},
        2: { 'Name': 'AmPm', 'Type': AmPmIcon},
        3: { 'Name': 'Unknown3', 'Type': 'long?'},
        4: { 'Name': 'Weekday', 'Type': ImageSet},
        5: { 'Name': 'WeekdayChinese', 'Type': ImageSet},
        6: { 'Name': 'WeekdayKorean', 'Type': ImageSet},
        7: { 'Name': 'WeekdayProgress', 'Type': Progress},
    }


class WeekDayImages:
    definitions = {
        1: {'Name': 'Monday', 'Type': Image},
        2: {'Name': 'Tuesday', 'Type': Image},
        3: {'Name': 'Wednesday', 'Type': Image},
        4: {'Name': 'Thursday', 'Type': Image},
        5: {'Name': 'Friday', 'Type': Image},
        6: {'Name': 'Saturday', 'Type': Image},
        7: {'Name': 'Sunday', 'Type': Image},
    }