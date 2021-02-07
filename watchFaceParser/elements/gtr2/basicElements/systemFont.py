from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 
from watchFaceParser.elements.basicElements.coordinates import Coordinates
from watchFaceParser.models.color import Color 
from watchFaceParser.elements.gtr2.basicElements.fontUnknown import FontUnknown 

class SystemFont:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': FontUnknown}, 
        2: { 'Name': 'Coordinates', 'Type': Coordinates}, 
        3: { 'Name': 'Angle', 'Type': 'long'}, 
        4: { 'Name': 'Size', 'Type': 'long'},
        5: { 'Name': 'Color', 'Type': Color},
        6: { 'Name': 'ShowUnitCheck', 'Type': 'long'},
    }