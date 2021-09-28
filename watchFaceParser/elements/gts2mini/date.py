from watchFaceParser.elements.gts2mini.dateElements.monthAndDay import MonthAndDay
from watchFaceParser.elements.gts2mini.dateElements.oneLineMonthAndDay import OneLineMonthAndDay

class Date:
    definitions = {
        2: { 'Name': 'OneLineMonthAndDay', 'Type': OneLineMonthAndDay},
        4: { 'Name': 'PaddingZeroMonth', 'Type': 'bool'},
        5: { 'Name': 'PaddingZeroDay', 'Type': 'bool'},
        6: { 'Name': 'Unknown6', 'Type': 'long'},
        9: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
    }

