from watchFaceParser.elements.gtr2.basicElements.imageAngle import ImageAngle 
from watchFaceParser.models.color import Color
 
class CircleProgress:
    definitions = { 
        1: { 'Name': 'AngleSettings', 'Type': ImageAngle},
        3: { 'Name': 'ImageIndex', 'Type': 'long'},
        4: { 'Name': 'Color', 'Type': Color},   
        5: { 'Name': 'Width', 'Type': 'long'},   
        6: { 'Name': 'Flatness', 'Type': 'long'}, #0 - flat, 90, triangle, 180 - arc 
        8: { 'Name': 'ImageIndex', 'Type': 'long'},
    }
