import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class SystemElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._status = None
        self._date = None
        self._activity = []
        super(SystemElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getStatus(self):
        return self._status


    def getDate(self):
        return self._date


    def getActivity(self):
        return self._activity


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.statusElement import StatusElement
            self._status = StatusElement(parameter = parameter)
            return self._status
        elif parameterId == 2:
            pass
            # from watchFaceParser.models.gtr2.elements.dateElement import DateElement
            # self._date = DateElement(parameter = parameter)
            # return self._date
        elif parameterId == 3:
            pass
            # from watchFaceParser.models.gtr2.elements.activityElement import ActivityElement
            # self._activity.append(ActivityElement(parameter = parameter))
            # return self._activity
        else:
            print ("Unknown SystemElement",parameterId)
            return super(SystemElement, self).createChildForParameter(parameter)

