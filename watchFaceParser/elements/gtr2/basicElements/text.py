from watchFaceParser.elements.gtr2.basicElements.image import Image 
from watchFaceParser.models.gtr2.textAlignment import TextAlignmentGTR2

class Text:
    definitions = { 
        1: { 'Name': 'Image', 'Type': Image},
        3: { 'Name': 'Alignment', 'Type': TextAlignmentGTR2},
        4: { 'Name': 'Spacing', 'Type': 'long'}, 
        5: { 'Name': 'PaddingZero', 'Type': 'long'},
        6: { 'Name': 'Unknown6', 'Type': 'long'}, 
    }
