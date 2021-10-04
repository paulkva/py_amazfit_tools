from watchFaceParser.elements.gts2mini.dateElements.monthAndDay import MonthAndDay
from watchFaceParser.elements.gts2mini.dateElements.oneLineMonthAndDay import OneLineMonthAndDay
from watchFaceParser.elements.gts2mini.dateElements.oneLineYearMonthAndDay import OneLineYearMonthAndDay
from watchFaceParser.elements.gts2mini.dateElements.monthAndDayAlt import MonthAndDayAlt

class Date:
    definitions = {
        1: { 'Name': 'MonthAndDayAlt', 'Type': MonthAndDayAlt}, # alternate date
        2: { 'Name': 'OneLineMonthAndDay', 'Type': OneLineMonthAndDay},
        3: { 'Name': 'OneLineYearMonthAndDay', 'Type': OneLineYearMonthAndDay},
        4: { 'Name': 'PaddingZeroMonth', 'Type': 'bool'},
        5: { 'Name': 'PaddingZeroDay', 'Type': 'bool'},
        6: { 'Name': 'Unknown6', 'Type': 'long'},
        9: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
    }

