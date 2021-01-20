#from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.gtr2.basicElements.image import Image 

class Text:
    definitions = { 
        1: { 'Name': 'Image', 'Type': Image},
        5: { 'Name': 'PaddingZeroCheck', 'Type': 'long'}, 
    }
