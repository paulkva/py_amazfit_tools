import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class ScreenIdleElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._screennormal = None
        self._date = None
        self._activity = None
        super(ScreenIdleElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getScreenNormal(self):
        return self._screennormal


    def getDate(self):
        return self._date


    def getActivity(self):
        return self._activity


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.screenNormalElement import ScreenNormalElement
            self._screennormal = ScreenIdleElement(parameter = parameter)
            return self._screennormal
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.dateElement import DateElement
            self._date = DateElement(parameter = parameter)
            return self._date
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.activityElement import ActivityElement
            self._activity = ActivityElement(parameter = parameter)
            return self._activity
        else:
            print ("Unknown ScreenIdleElement",parameterId)
            return super(ScreenIdleElement, self).createChildForParameter(parameter)

