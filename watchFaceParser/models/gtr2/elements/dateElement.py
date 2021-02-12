import logging

from watchFaceParser.models.elements.basic.containerElement import ContainerElement

class DateElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._monthAndDay = None
        self._weekDay = None
        self._year = None
        self._weekDayProgress = None		
        super(DateElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getMonthAndDay(self):
        #print ("DEBUG: getMonthAndDay")
        return self._monthAndDay

    def getWeekDay(self):
        #print ("DEBUG: getWeekDay")
        return self._weekDay

    def getYear(self):
        #print ("DEBUG: getYear")
        return self._year

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.date.monthAndDayElement import MonthAndDayElement
            self._monthAndDay = MonthAndDayElement(parameter = parameter, parent = self, name = 'MonthAndDay')
            return self._monthAndDay
        elif parameterId == 2:
            from watchFaceParser.models.elements.date.weekDayElement import WeekDayElement
            self._weekDay = WeekDayElement(parameter = parameter, parent = self, name = 'WeekDay')
            return self._weekDay
        elif parameterId == 5:
            from watchFaceParser.models.elements.date.yearElement import YearElement
            self._year = YearElement(parameter = parameter, parent = self, name = 'Year')
            return self._year
        elif parameterId == 6:
            from watchFaceParser.models.elements.date.weekDayProgressElement import WeekDayProgressElement
            self._weekDayProgress = WeekDayProgressElement(parameter = parameter, parent = self, name = 'WeekDayProgress')
            #import jsonpickle
            #import json
            #print ("self._weekDayProgress",json.dumps(json.loads(jsonpickle.encode(self._weekDayProgress.__dict__)), indent=4))
            #print ("DATELELEMENT6")
            return self._weekDayProgress
        else:
            return super(DateElement, self).createChildForParameter(parameter)
