import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeSeparateDigitsContainerElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._time = None

        super(TimeSeparateDigitsContainerElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.time.timeSeparateDigitsElement import TimeSeparateDigitsElement
            self._time = TimeSeparateDigitsElement(parameter = parameter, parent = self, name = 'Time')
            return self._time
        else:
            print ("Unknown TimeSeparateDigitsContainerElement",parameterId)
            return super(TimeSeparateDigitsContainerElement, self).createChildForParameter(parameter)

