from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 
   
class MultilangImageCoord:
    definitions = {
        1: { 'Name': 'Coordinates', 'Type': Coordinates},
        2: { 'Name': 'ImageSet', 'Type': [MultilangImage]},
    }
