import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class DigitalDateDigitElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._dateType = None
        self._combingMode = None
        self._digit = None
        self._separator = None
        super(DigitalDateDigitElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getDateType(self):
        return self._dateType

    def getCombingMode(self):
        return self._combingMode

    def getDigit(self):
        return self._digit

    def getSeparator(self):
        return self._separator
    
    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)

        if self.getSeparator():
            self.getSeparator().draw3(drawer, resources, state)
        if self.getDigit():
            if self._dateType == 0:
                self.getDigit().draw4(drawer, resources, state.getTime().year, 4)
            elif self._dateType == 1:
                self.getDigit().draw4(drawer, resources, state.getTime().month, 2)
            elif self._dateType == 2:
                self.getDigit().draw4(drawer, resources, state.getTime().day, 2)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._dateType = parameter.getValue()
            return ValueElement(parameter, self, 'TimeType')
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
            super(DigitalDateDigitElement, self).createChildForParameter(parameter)
