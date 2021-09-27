#identical to OneLineMonthAndDay
from watchFaceParser.elements.gts2mini.basicElements.number import Number

class OneLine:
    definitions = {
        1: { 'Name': 'Number', 'Type': Number},
        2: { 'Name': 'MinusImageIndex', 'Type': 'long'},
        3: { 'Name': 'DelimiterImageIndex', 'Type': 'long'},
        4: { 'Name': 'Unknown4', 'Type': 'long?'},
        5: { 'Name': 'DegreesImageIndex', 'Type': 'long'},
    }
