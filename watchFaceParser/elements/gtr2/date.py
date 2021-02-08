from watchFaceParser.elements.gtr2.digitalElements.digitalDateDigit import DigitalDateDigit
from watchFaceParser.elements.gtr2.digitalElements.digitalCommonDigit import DigitalCommonDigit
from watchFaceParser.elements.gtr2.basicElements.image import Image 
<<<<<<< HEAD
from watchFaceParser.elements.gtr2.progress import Progress  
from watchFaceParser.elements.gtr2.dowProgress import DOWProgress  
=======
from watchFaceParser.elements.gtr2.progress import Progress 
from watchFaceParser.elements.gtr2.dowProgress import DOWProgress

>>>>>>> 315ce16af10bfe8ea9ec3d0b49a29f9269e385a7
class Date:
    definitions = {
        1: { 'Name': 'DateDigits', 'Type': [DigitalDateDigit] },
        2: { 'Name': 'WeeksDigits', 'Type': DigitalCommonDigit },
        3: { 'Name': 'DateProgress', 'Type': Progress},
<<<<<<< HEAD
        4: { 'Name': 'DOWProgress', 'Type': DOWProgress},
=======
		4: { 'Name': 'DOWProgress', 'Type': DOWProgress},
>>>>>>> 315ce16af10bfe8ea9ec3d0b49a29f9269e385a7
    }

