import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class WidgetsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._widget = None
        super(WidgetsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getWidget(self):
        return self._widget

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.statusElement import StatusElement
            self._status = StatusElement(parameter = parameter)
            return self._status
        else:
            print ("Unknown WidgetsElement",parameterId)
            return super(WidgetsElement, self).createChildForParameter(parameter)

