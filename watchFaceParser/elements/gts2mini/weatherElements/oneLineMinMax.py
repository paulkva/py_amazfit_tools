from watchFaceParser.elements.gts2mini.basicElements.number import Number

class OneLineMinMax:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'MinusImageIndex', 'Type': 'long'},
        3: { 'Name': 'DelimiterImageIndex', 'Type': 'long'},
        4: { 'Name': 'UnknownLong4', 'Type': 'long'}, #bool? always 0 except for eddc844402b6157dfb01e2b780b64b0b.bin
        5: { 'Name': 'DegreesImageIndex', 'Type': 'long'},
    }
