import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class DigitalCommonDigitElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._type = None
        self._combingMode = None
        self._digit = None
        self._separator = None
        super(DigitalCommonDigitElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getType(self):
        return self._type

    def getCombingMode(self):
        return self._combingMode

    def getDigit(self):
        return self._digit

    def getSeparator(self):
        return self._separator

    def draw4(self, drawer, images, number, numberMin = None, numberMax = None, minimumDigits = 1, unit = ''):
        assert(type(images) == list)

        number = numberMax if self._type == 2 else numberMin if self._type == 1 else number

        if self.getSeparator():
            self.getSeparator().draw3(drawer, images, None)
        if self.getDigit():
            self.getDigit().draw4(drawer, images, number, minimumDigits, followxy = None, padding_zero = None, unit=unit)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._type = parameter.getValue()
            return ValueElement(parameter, self, 'Type')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._combingMode = parameter.getValue()
            return ValueElement(parameter, self, 'CombingMode')
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.common.textElement import TextElement
            self._digit = TextElement(parameter = parameter, parent = self, name = 'Digit')
            return self._digit
        elif parameterId == 4:
            from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement
            self._separator = ImageCoordsElement(parameter = parameter, parent = self, name = 'Separator')
            return self._separator
        else:
            super(DigitalCommonDigitElement, self).createChildForParameter(parameter)
