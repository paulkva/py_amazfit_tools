import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class AnalogDialElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._minutes = None
        self._seconds = None
        super(AnalogDialElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getHours(self):
        return self._hours

    def getMinutes(self):
        return self._minutes

    def getSeconds(self):
        return self._seconds

    def draw3(self, drawer, resources, state):
        if self.getSeconds():
            self.getSeconds().draw3(drawer, resources, state)
        if self.getHours():
            self.getHours().draw3(drawer, resources, state)
        if self.getMinutes():
            self.getMinutes().draw3(drawer, resources, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.analogDial.hoursClockHandElement import HoursClockHandElement
            self._hours = HoursClockHandElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.analogDial.minutesClockHandElement import MinutesClockHandElement
            self._minutes = MinutesClockHandElement(parameter = parameter, parent = self, name = 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.analogDial.secondsClockHandElement import SecondsClockHandElement
            self._seconds = SecondsClockHandElement(parameter = parameter, parent = self, name = 'Seconds')
            return self._seconds
        else:
            return super(AnalogDialElement, self).createChildForParameter(parameter)