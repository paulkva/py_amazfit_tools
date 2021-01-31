from watchFaceParser.elements.gtr2.basicElements.imageCoord import ImageCoord 
from watchFaceParser.elements.gtr2.widgetElement import WidgetElement 

class Widget:
    definitions = { 
        1: { 'Name': 'X', 'Type': 'long' },   
        2: { 'Name': 'Y', 'Type': 'long' },   
        3: { 'Name': 'Width', 'Type': 'long' },   
        4: { 'Name': 'Height', 'Type': 'long' },   
        5: { 'Name': 'WidgetElement', 'Type': [WidgetElement] },   
        6: { 'Name': 'Unknown6', 'Type': 'long' },   
        7: { 'Name': 'Unknown7', 'Type': 'long' },   
        8: { 'Name': 'DescriptionImageBackground', 'Type': ImageCoord },   
        9: { 'Name': 'DescriptionWidthCheck', 'Type': 'long' },   
    }