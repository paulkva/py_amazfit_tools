import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeSeparatedDigitsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._separator = None
        self._padding_zero_hours = None

        super(TimeSeparatedDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        hours = state.getTime().hour

        if self._hours and self._hours.getTens():
            if self._padding_zero_hours or int(hours % 100 / 10) > 0:
                self._hours.getTens().draw3(drawer, images, int(hours % 100 / 10))
        if self._hours and self._hours.getOnes():
            self._hours.getOnes().draw3(drawer, images, hours % 10)

        if self._minutes and self._minutes.getTens():
            self._minutes.getTens().draw3(drawer, images, int(state.getTime().minute % 100 / 10))
        if self._minutes and self._minutes.getOnes():
            self._minutes.getOnes().draw3(drawer, images, state.getTime().minute % 10)

        if self._separator:
            self._separator.draw3(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.twoDigitsElement import TwoDigitsElement
            self._hours = TwoDigitsElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.twoDigitsElement import TwoDigitsElement
            self._minutes = TwoDigitsElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.imageElement import ImageElement
            self._separator = ImageElement(parameter = parameter, parent = self, name ='Separator')
            return self._separator
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._padding_zero_hours = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroHours')
        else:
            print ("Unknown TimeSeparatedDigitsElement",parameterId)
            return super(TimeSeparatedDigitsElement, self).createChildForParameter(parameter)

