from watchFaceParser.elements.gtr2.digitalElements.digitalTimeDigit import DigitalTimeDigit
from watchFaceParser.elements.gtr2.timeElements.amPm import AmPm

class DigitalDialFace:
    definitions = {
        1: { 'Name': 'Digits', 'Type': [DigitalTimeDigit]}, 
        2: { 'Name': 'AM', 'Type': AmPm}, 
        3: { 'Name': 'PM', 'Type': AmPm}, 
    }

