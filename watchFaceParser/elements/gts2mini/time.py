from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.image import Image

class Time:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': 'long'},
        2: { 'Name': 'Minutes', 'Type': Number},
        3: { 'Name': 'Hours', 'Type': Number},
        4: { 'Name': 'Unknown4', 'Type': 'long'},
        5: { 'Name': 'Unknown5', 'Type': 'long'},
        8: { 'Name': 'Unknown8', 'Type': 'long'},
        9: { 'Name': 'Unknown9', 'Type': 'long'},
    }

