from watchFaceParser.models.color import Color

class PointerScale:
    definitions = {
        1: { 'Name': 'CenterX', 'Type': 'long'},
        2: { 'Name': 'CenterY', 'Type': 'long'},
        3: { 'Name': 'RangeFrom', 'Type': 'int'},
        4: { 'Name': 'RangeTo', 'Type': 'int'},
        5: { 'Name': 'PointerImageIndex', 'Type': 'long'},
        6: { 'Name': 'PointerCenterOfRotationY', 'Type': 'long'},
    }
