from watchFaceParser.elements.gtr2.digitalDialFace import DigitalDialFace
from watchFaceParser.elements.gtr2.analogDialFace import AnalogDialFace 
from watchFaceParser.elements.gtr2.progressDialFace import ProgressgDialFace 

class ScreenNormal:
    definitions = {  
        1: { 'Name': 'DigitalDialFace', 'Type': DigitalDialFace},
        2: { 'Name': 'AnalogDialFace', 'Type': AnalogDialFace}, 
        3: { 'Name': 'ProgressDialFace', 'Type': ProgressgDialFace}, 
    }
