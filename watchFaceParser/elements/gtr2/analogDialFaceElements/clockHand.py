from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 
from watchFaceParser.elements.gtr2.basicElements.multilangImageCoord import MultilangImageCoord 

class ClockHand:
    definitions = { 
        1: { 'Name': 'X', 'Type': 'long'},
        2: { 'Name': 'Y', 'Type': 'long'},
        3: { 'Name': 'Scale', 'Type': MultilangImageCoord},
        4: { 'Name': 'Pointer', 'Type': ImageCoord},
        5: { 'Name': 'Cover', 'Type': ImageCoord},
        6: { 'Name': 'Unknown6', 'Type': 'long'},
        7: { 'Name': 'Unknown7', 'Type': 'long'},
        16: { 'Name': 'Unknown16', 'Type': 'long'},
    }

