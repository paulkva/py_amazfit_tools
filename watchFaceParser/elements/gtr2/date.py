from watchFaceParser.elements.gtr2.digitalElements.digitalDateDigit import DigitalDateDigit
from watchFaceParser.elements.gtr2.digitalElements.digitalCommonDigit import DigitalCommonDigit

class Date:
    definitions = {
        1: { 'Name': 'DateDigits', 'Type': [DigitalDateDigit] },
        2: { 'Name': 'Weeks', 'Type': DigitalCommonDigit },
    }

