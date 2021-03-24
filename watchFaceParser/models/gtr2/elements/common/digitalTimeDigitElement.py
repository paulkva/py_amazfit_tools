import logging

from watchFaceParser.config import Config

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class DigitalTimeDigitElement(ContainerElement):
    def __init__(self, parameter, parent, name=None):
        self._timeType = None
        self._combingMode = None
        self._digit = None
        self._separator = None
        super(DigitalTimeDigitElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getTimeType(self):
        return self._timeType

    def getCombingMode(self):
        return self._combingMode

    def getDigit(self):
        return self._digit

    def getSeparator(self):
        return self._separator

    def draw4(self, drawer, resources, state, ampm):
        assert(type(resources) == list)

        if self.getSeparator():
            self.getSeparator().draw3(drawer, resources, state)
        if self.getDigit():
            if self._timeType == 0:
                hours = state.getTime().hour if not ampm else state.getTime().hour % 12
                self.getDigit().draw4(drawer, resources, hours, 2)
            elif self._timeType == 1:
                self.getDigit().draw4(drawer, resources, state.getTime().minute, 2)
            elif self._timeType == 2:
                self.getDigit().draw4(drawer, resources, state.getTime().second, 2)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._timeType = parameter.getValue()
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
            super(DigitalTimeDigitElement, self).createChildForParameter(parameter)
