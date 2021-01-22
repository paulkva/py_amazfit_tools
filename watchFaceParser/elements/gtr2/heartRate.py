from watchFaceParser.elements.gtr2.digitalElements.digitalTimeDigit import DigitalTimeDigit

class HeartRate:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': 'long' }, 
        5: { 'Name': 'Digits', 'Type': DigitalTimeDigit },   
    }