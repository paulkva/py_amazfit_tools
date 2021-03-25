import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.helpers.drawerHelper import DrawerHelper

class TextElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._image = None
        self._systemFont = None
        self._alignment = None
        self._spacing = None
        self._paddingZero = None
        self._displayFormAnalog = None
        super(TextElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getImage(self):
        return self._image

    def getSystemFont(self):
        return self._systemFont

    def getAlignment(self):
        return self._alignment

    def getSpacing(self):
        return self._spacing

    def getPaddingZero(self):
        return self._paddingZero

    def getDisplayFormAnalog(self):
        return self._displayFormAnalog

    def draw4(self, drawer, images, number, minimumDigits = 1):
        stringNumber = str(number)
        if self.getPaddingZero():
            stringNumber = str(number).zfill(minimumDigits)
        if self.getImage():
            self.getImage().draw4(
                drawer, 
                images, 
                stringNumber, 
                self._alignment, 
                self._spacing, 
                minimumDigits, 
                self._displayFormAnalog)
        elif self.getSystemFont():
            return

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.common.imageElement import ImageElement
            self._image = ImageElement(parameter, self, name='Image')
            return self._image
        elif parameterId == 2:
            # SystemFont
            # TODO: SystemFont implement
            pass
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._alignment = parameter.getValue()
            return ValueElement(parameter, self, 'Alignment')
        elif parameterId == 4:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._spacing = parameter.getValue()
            return ValueElement(parameter, self, 'Spacing')
        elif parameterId == 5:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._paddingZero = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZero')
        elif parameterId == 6:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._displayFormAnalog = parameter.getValue()
            return ValueElement(parameter, self, 'DisplayFormAnalog')
        else:
            super(TextElement, self).createChildForParameter(parameter)
