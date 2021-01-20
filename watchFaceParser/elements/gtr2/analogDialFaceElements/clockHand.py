from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 

class ClockHand:
    definitions = { 
        1: { 'Name': 'X', 'Type': 'long'},
        2: { 'Name': 'Y', 'Type': 'long'},
        4: { 'Name': 'Pointer', 'Type': ImageCoord},
        5: { 'Name': 'Cover', 'Type': ImageCoord},
        7: { 'Name': 'Unknown7', 'Type': 'long'},
        16: { 'Name': 'Unknown16', 'Type': 'long'},
    }

