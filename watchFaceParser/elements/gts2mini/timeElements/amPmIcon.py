from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class AmPmIcon:
    definitions = {
        1: { 'Name': 'CommonX', 'Type': 'long'},
        2: { 'Name': 'CommonY', 'Type': 'long'},
        3: { 'Name': 'ImageIndexAMCN', 'Type': 'long'},
        4: { 'Name': 'ImageIndexPMCN', 'Type': 'long'},
        5: { 'Name': 'AmImageIndexEN', 'Type': 'long'},
        6: { 'Name': 'PmImageIndexEN', 'Type': 'long'},
        8: { 'Name': 'CoordinatesAM', 'Type': Coordinates},
        9: { 'Name': 'CoordinatesPM', 'Type': Coordinates},
    }

