from watchFaceParser.elements.gtr2.digitalDialFace import DigitalDialFace
from watchFaceParser.elements.gtr2.analogDialFace import AnalogDialFace 

class ScreenNormal:
    definitions = {  
        1: { 'Name': 'DigitalDialFace', 'Type': DigitalDialFace},
        2: { 'Name': 'AnalogDialFace', 'Type': AnalogDialFace}, 
    }
