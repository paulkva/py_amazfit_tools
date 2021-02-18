import logging

from watchFaceParser.models.gtr2.elements.basic.containerElement import ContainerElement


class DigitalDialFaceElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._digits = None
        self._am = None
        self._pm = None
        super(DigitalDialFaceElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getDigits(self):
        return self._digits


    def getAm(self):
        return self._am


    def getPm(self):
        return self._pm


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.multilangImageCoordsElement import MultilangImageCoordsElement
            self._am = MultilangImageCoordsElement(parameter = parameter, parent = self, name = 'AM')
            return self._am
        elif parameterId == 3:
            from watchFaceParser.models.gtr2.elements.common.multilangImageCoordsElement import MultilangImageCoordsElement
            self._pm = MultilangImageCoordsElement(parameter=parameter, parent = self, name = 'PM')
            return self._pm
        else:
            print ("Unknown DigitalDialFaceElement",parameterId)
            return super(DigitalDialFaceElement, self).createChildForParameter(parameter)

