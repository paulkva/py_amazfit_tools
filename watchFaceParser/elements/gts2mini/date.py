from watchFaceParser.elements.gts2mini.dateElements.monthAndDay import MonthAndDay

class Date:
    definitions = {
        2: { 'Name': 'Unknown2', 'Type': 'long'},
        4: { 'Name': 'Unknown4', 'Type': 'long'},
        5: { 'Name': 'PaddingZeroDay', 'Type': 'bool'},
        6: { 'Name': 'Unknown6', 'Type': 'long'},
        9: { 'Name': 'MonthAndDay', 'Type': MonthAndDay},
    }

