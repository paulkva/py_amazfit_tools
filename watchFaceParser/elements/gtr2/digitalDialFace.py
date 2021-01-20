from watchFaceParser.elements.gtr2.digitalDialFaceElements.digitalDigit import DigitalDigit
from watchFaceParser.elements.gtr2.timeElements.amPm import AmPm

class DigitalDialFace:
    definitions = {
        1: { 'Name': 'Time', 'Type': [DigitalDigit]}, 
        2: { 'Name': 'AM', 'Type': AmPm}, 
        3: { 'Name': 'PM', 'Type': AmPm}, 
    }

