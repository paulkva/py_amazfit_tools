from watchFaceParser.elements.gts2mini.basicElements.number import Number
from watchFaceParser.elements.gts2mini.basicElements.coordinates import Coordinates

class Time:
    definitions = {
        1: { 'Name': 'Unknown1', 'Type': 'long'},
        2: { 'Name': 'Minutes', 'Type': Number},
        3: { 'Name': 'Seconds', 'Type': Number},
        4: { 'Name': 'PaddingZeroMinutes', 'Type': 'bool'},
        5: { 'Name': 'PaddingZeroSeconds', 'Type': 'bool'},
        6: { 'Name': 'DelimiterMinutes', 'Type': 'long'}, #probably MinutesDataTypeImageIndex
        7: { 'Name': 'DelimiterSeconds', 'Type': 'long'}, #probably SecondsDataTypeImageIndex
        8: { 'Name': 'MinutesFollowHours', 'Type': 'bool'},
        9: { 'Name': 'SecondsFollowMinutes', 'Type': 'bool'},
        10: { 'Name': 'DelimiterHoursCoordinates', 'Type': Coordinates}, #probably DataTypeHoursCoordinates
        11: { 'Name': 'DelimiterMinutesCoordinates', 'Type': Coordinates}, #probably DataTypeMinutesCoordinates
        12: { 'Name': 'DataTypeSecondsCoordinates', 'Type': Coordinates},
    }

