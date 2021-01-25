from watchFaceParser.elements.basicElements.image import Image 
from watchFaceParser.models.color import Color
 
class CircleProgress:
    definitions = { 
        1: { 'Name': 'ImageBG', 'Type': Image},
        3: { 'Name': 'Radius', 'Type': 'long'},
        4: { 'Name': 'Color', 'Type': Color},   
        5: { 'Name': 'Width', 'Type': 'long'},   
        6: { 'Name': 'Flatness', 'Type': 'long'}, #0 - flat, 90, triangle, 180 - arc 
        8: { 'Name': 'ImageIndex', 'Type': 'long'},
    }
