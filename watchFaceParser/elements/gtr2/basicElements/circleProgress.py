from watchFaceParser.elements.gtr2.basicElements.imageAngle import ImageAngle 
from watchFaceParser.models.color import Color
 
class CircleProgress:
    definitions = { 
        1: { 'Name': 'AngleSettings', 'Type': ImageAngle},
        2: { 'Name': 'Unknown2', 'Type': 'long'},
        3: { 'Name': 'ForegroundImageIndex', 'Type': 'long'},
        4: { 'Name': 'Color', 'Type': Color},   
        5: { 'Name': 'Width', 'Type': 'long'},   
        6: { 'Name': 'Flatness', 'Type': 'long'}, #0 - flat, 90, triangle, 180 - arc 
        7: { 'Name': 'Unknown7', 'Type': 'long'},
        8: { 'Name': 'BackgroundImageIndex', 'Type': 'long'},
    }
