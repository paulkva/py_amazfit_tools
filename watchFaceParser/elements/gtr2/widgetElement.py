from watchFaceParser.elements.gtr2.basicElements.multilangImage import MultilangImage 
from watchFaceParser.elements.gtr2.activity import Activity
from watchFaceParser.elements.gtr2.date import Date 

class WidgetElement:
    definitions = {
       1: { 'Name': 'Preview', 'Type': [MultilangImage] },  
       2: { 'Name': 'Date', 'Type': Date }, 
       3: { 'Name': 'Activity', 'Type': [Activity] },  
    }