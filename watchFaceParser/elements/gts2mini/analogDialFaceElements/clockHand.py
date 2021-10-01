from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates
from watchFaceParser.elements.gts2mini.basicElements.image import Image

class ClockHand:
    definitions = {
        1: { 'Name': 'ImageIndex', 'Type': 'long'},
        2: { 'Name': 'PointerCenterOfRotationY', 'Type': 'long'},
        3: { 'Name': 'CenterCoordinates', 'Type': Coordinates},
        4: { 'Name': 'CoverImage', 'Type': Image},
    }

