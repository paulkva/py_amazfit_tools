import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class DateBlockElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._date = None
        self._ampm = None
        self._weekDay = None
        super(DateBlockElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.dateElement import DateElement
            self._date = DateElement(parameter = parameter, parent = self, name = 'Date')
            return self._date
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.date.ampmElement import AmPmElement
            self._ampm = AmPmElement(parameter = parameter, parent = self, name = 'AmPm')
            return self._ampm
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.date.weekDayElement import WeekDayElement
            self._weekDay = WeekDayElement(parameter = parameter, parent = self, name = 'Weekday')
            return self._weekDay
        elif parameterId == 5: # WeekdayChinese
            pass
        elif parameterId == 6: # WeekdayKorean
            pass
        else:
            return super(DateBlockElement, self).createChildForParameter(parameter)
