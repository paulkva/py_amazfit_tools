from watchFaceParser.elements.timeElements.twoDigits import TwoDigits

class Time:
    definitions = {
        1: {'Name': 'Hours', 'Type': TwoDigits},
        2: {'Name': 'Minutes', 'Type': TwoDigits},
        3: {'Name': 'Seconds', 'Type': TwoDigits},
        7: {'Name': 'Unknown7', 'Type': 'long?'},
        8: {'Name': 'Unknown8', 'Type': 'long?'},
    }

class TimeSeparateDigits:
    definitions = {
        1: {'Name': 'Time', 'Type': Time},
    }

