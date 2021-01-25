from watchFaceParser.elements.gtr2.digitalElements.digitalTimeDigit import DigitalTimeDigit
from watchFaceParser.elements.gtr2.basicElements.multilangImageCoord import MultilangImageCoord

class DigitalDialFace:
    definitions = {
        1: { 'Name': 'Digits', 'Type': [DigitalTimeDigit]}, 
        2: { 'Name': 'AM', 'Type': MultilangImageCoord}, 
        3: { 'Name': 'PM', 'Type': MultilangImageCoord}, 
    }

