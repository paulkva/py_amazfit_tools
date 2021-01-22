from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord

class Status:
    definitions = {
        1: { 'Name': 'Disconnect', 'Type': ImageCoord },  
        2: { 'Name': 'DND', 'Type': ImageCoord },  
        3: { 'Name': 'Lock', 'Type': ImageCoord },  
        4: { 'Name': 'Clock', 'Type': ImageCoord },  
    }