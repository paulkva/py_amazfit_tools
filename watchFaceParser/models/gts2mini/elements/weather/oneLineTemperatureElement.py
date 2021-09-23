#semi identical to oneLineYearElement
import logging

from watchFaceParser.models.elements.basic.compositeElement import CompositeElement
from watchFaceParser.utils.parametersConverter import uint2int


class OneLineTemperatureElement(CompositeElement):
    def __init__(self, parameter, parent, name = None):
        self._number = None
        self._delimiterImageIndex = None
        super(OneLineTemperatureElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)


    def getNumber(self):
        return self._number

    def getDelimiterImageIndex(self):
        return self._delimiterImageIndex

    def draw3(self, drawer, resources, state):
        print("draw3 (OneLineTemperatureElement)")
        assert(type(resources) == list)
        #year = self._parent
        images = []

        appendDegreeForBoth = self._parent.getAppendDegreesForBoth()
        getSymbols = self._parent._parent.getSymbols()

        temperature = state.getCurrentTemperature()
        temperature2 = temperature
        if not temperature:
            if getSymbols:
                if getSymbols.getNoDataImageIndex():
                    images.append(resources[getSymbols.getNoDataImageIndex()])
        else:
            temperature = int(temperature)
            temperature2 = temperature - 3
            if temperature < 0:
                temperature = -temperature
            print ("TEMP",temperature)
            #print ("draw3",state.getTime().year)
            images = self.getNumber().getImagesForNumber(resources, temperature, 2)
			
        #print ("draw3",images)
        if appendDegreeForBoth and getSymbols:
            if getSymbols.getDegreesImageIndex():
                images.append(resources[getSymbols.getDegreesImageIndex()])
		
        if self.getDelimiterImageIndex():
            images.append(resources[self.getDelimiterImageIndex().getValue()])

        if not temperature2:
            if getSymbols:
                if getSymbols.getNoDataImageIndex():
                    images.append(resources[getSymbols.getNoDataImageIndex()])
        else:
            print ("TEMP2",temperature2)
            temperature2 = int(temperature2)
            if temperature2 < 0:
                temperature2 = -temperature2
            print ("TEMP2bis",temperature2)

            for image in self.getNumber().getImagesForNumber(resources, temperature2, 2 ):#if monthAndDay.getTwoDigitsDay() else 1):
                images.append(image)

        if appendDegreeForBoth and getSymbols:
            if getSymbols.getDegreesImageIndex():
                images.append(resources[getSymbols.getDegreesImageIndex()])

        from watchFaceParser.helpers.drawerHelper import DrawerHelper
        DrawerHelper.drawImages(drawer, images, uint2int(self.getNumber().getSpacing()), self.getNumber().getAlignment(), self.getNumber().getBox())


    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.elements.common.numberElement import NumberElement
            self._number = NumberElement(parameter = parameter, parent = self, name = 'Number')
            return self._number
        elif parameterId == 2:
            from watchFaceParser.models.elements.basic.valueElement import ValueElement
            self._delimiterImageIndex = ValueElement(parameter = parameter, parent = self, name = 'DelimiterImageIndex')
            return self._delimiterImageIndex
        else:
            print ("Unknown OneLineTemperatureElement",parameterId)
            return super(OneLineTemperatureElement, self).createChildForParameter(parameter)
