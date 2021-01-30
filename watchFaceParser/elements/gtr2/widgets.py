from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 
from watchFaceParser.elements.gtr2.widget import Widget 

class Widgets:
    definitions = { 
        1: { 'Name': 'Widget', 'Type': [Widget] },   
        2: { 'Name': 'Mask1ImageIndex', 'Type': 'long' },   
        3: { 'Name': 'Mask2ImageIndex', 'Type': 'long' },   
        4: { 'Name': 'Unknown4', 'Type': 'long' },    
    }