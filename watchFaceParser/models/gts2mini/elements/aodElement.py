import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class AodElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._timeExt = None
        self._dateOneLine = None
        self._week = None
        self._steps = None
        self._date = None
        super(AodElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if state.getScreenIdle() is None:
            return 

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.aod.timeExtendedElement import TimeExtendedElement
            self._timeExt = TimeExtendedElement(parameter = parameter, parent = self, name ='TimeExtended')
            return self._timeExt
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.aod.dateOneLineElement import DateOneLineElement
            self._dateOneLine = DateOneLineElement(parameter = parameter, parent = self, name ='DateOneLine')
            return self._dateOneLine
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.aod.weekDayElement import WeekDayElement
            self._week = WeekDayElement(parameter = parameter, parent = self, name ='Week')
            return self._week
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.aod.stepsElement import StepsElement
            self._steps = StepsElement(parameter = parameter, parent = self, name ='Steps')
            return self._steps
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.aod.dateElement import DateElement
            self._date = DateElement(parameter = parameter, parent = self, name ='Date')
            return self._date
        else:
            print ("Unknown AodElement",parameterId)
            return super(AodElement, self).createChildForParameter(parameter)

