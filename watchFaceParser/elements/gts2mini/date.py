from watchFaceParser.elements.gts2mini.dateElements.monthAndDay import MonthAndDay

class Date:
    definitions = {
        4: { 'Name': 'PaddingZeroMonth', 'Type': 'long'},
        5: { 'Name': 'PaddingZeroDay', 'Type': 'bool'},
        6: { 'Name': 'Unknown6', 'Type': 'long'},
        9: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
    }

