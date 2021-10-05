import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class AnalogDialElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._center = None
        super(AnalogDialElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._hours:
            self._hours.draw4(drawer, images, state, self._center)
        if self._minutes:
            self._minutes.draw4(drawer, images, state, self._center)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._center = CoordinatesElement(parameter=parameter, parent=self, name='CenterCoordinates')
            return self._center
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.analogDial.hoursClockHandElement import HoursClockHandElement
            self._hours = HoursClockHandElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.analogDial.minutesClockHandElement import MinutesClockHandElement
            self._minutes = MinutesClockHandElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        else:
            return super(AnalogDialElement, self).createChildForParameter(parameter)