import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
#from watchFaceParser.models.elements.basic.containerElement import ContainerElement
from watchFaceParser.utils.parametersConverter import uint2int


class TodayElement(CompositeElement):
#class TodayElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._separate = None
        self._oneLine = None
        self._appendDegreesForBoth = None
        super(TodayElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getOneLine(self):
        return self._oneLine

    def getAppendDegreesForBoth(self):
        return self._appendDegreesForBoth
		
    #def getSymbols(self):
    #    return self._symbols


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
    #    images = []

        #temperature = state.getCurrentTemperature()
        #if not temperature:
        #    if self.getSymbols().getNoDataImageIndex():
        #        images.append(resources[self.getSymbols().getNoDataImageIndex()])
        #else:
        #    temperature = int(temperature)
        #    if temperature < 0:
        #        temperature = -temperature
        #        if self.getSymbols().getMinusImageIndex():
        #            images.append(resources[self.getSymbols().getMinusImageIndex()])
		#
        #    if self.getCurrent():
        #        images.extend(self.getCurrent().getImagesForNumber(resources, temperature))
		#
        #    if self.getSymbols().getDegreesImageIndex():
        #        images.append(resources[self.getSymbols().getDegreesImageIndex()])
		#
        #if self.getCurrent():
        #    from watchFaceParser.helpers.drawerHelper import DrawerHelper
        #    DrawerHelper.drawImages(drawer, images, uint2int(self.getCurrent().getSpacing()), self.getCurrent().getAlignment(), self.getCurrent().getBox())
        if self.getOneLine():
            self.getOneLine().draw3(drawer, resources, state)


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()

        #if parameterId == 1:
            #separate
        #    from watchFaceParser.models.elements.common.numberElement import NumberElement
        #    self._current = NumberElement(parameter, self, '?_current?')
        #    return self._current
        #el
        if parameterId == 2:
        # oneline
#       #     #print ("TodayElement: (Temperature->Today)", parameterId)
#       #     pass
            from watchFaceParser.models.elements.weather.oneLineTemperatureElement import OneLineTemperatureElement
            self._oneLine = OneLineTemperatureElement(parameter = parameter, parent = self, name = 'OneLineTemperature')
            return self._oneLine
        elif parameterId == 3:
        #AppendDegreesForBoth
            self._appendDegreesForBoth = parameter.getValue()
            print ("_appendDegreesForBoth",self._appendDegreesForBoth)
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            return ValueElement(parameter = parameter, parent = self, name = '?_appendDegreesForBoth?')
        else:
            print ("Unknown TodayElement",parameterId)
            super(TodayElement, self).createChildForParameter(parameter)

