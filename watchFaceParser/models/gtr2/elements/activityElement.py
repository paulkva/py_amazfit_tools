import logging
import random

from watchFaceParser.models.elements.basic.containerElement import ContainerElement


class ActivityElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._type = None
        self._pointerProgress = None
        self._progressBar = None
        self._imageProgress = None
        self._digits = []
        self._icon = None
        super(ActivityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getType(self):
        return self._type

    def getPointerProgress(self):
        return self._pointerProgress

    def getProgressBar(self):
        return self._progressBar

    def getImageProgress(self):
        return self._imageProgress

    def getDigits(self):
        return self._digits

    def getIcon(self):
        return self._icon

    def draw3(self, drawer, images, state):
        if self.getIcon():
            self.getIcon().draw3(drawer, images, None)
        number = None
        maxNumber = None
        maxNumberLength = 1
        imageProgressState = None
        if self.getType() == 1 and state.getBatteryLevel() is not None:
            number = state.getBatteryLevel()
            maxNumber = 100
            maxNumberLength = 3
            imageProgressState = ( number, maxNumber)
        elif self.getType() == 2 and state.getSteps() is not None:
            number = state.getSteps()
            maxNumber = state.getGoal()
            maxNumberLength = 5
            imageProgressState = (number, maxNumber)
        elif self.getType() == 3 and state.getCalories() is not None:
            number = state.getCalories()
            maxNumber = 700
            maxNumberLength = 4
            imageProgressState = (number, maxNumber)
        elif self.getType() == 4 and state.getPulse() is not None:
            number = state.getPulse()
            maxNumber = 250
            maxNumberLength = 3
            imageProgressState = (number, maxNumber)
        elif self.getType() == 5 and state.getCalories() is not None: # PAI
            number = state.getCalories() 
            maxNumber = 700
            maxNumberLength = 3
            imageProgressState = (number, maxNumber)
        elif self.getType() == 6 and state.getDistance() is not None: # Distance
            number = state.getDistance() 
            maxNumber = state.getGoal() / 1000
            maxNumberLength = 4
        elif self.getType() == 7: # StandUp
            number = random.randint(0, 12)
            maxNumber = 12
            maxNumberLength = 2
            imageProgressState = (number, maxNumber)
        elif self.getType() == 8: # Weather
            # state.getCurrentWeather()
            # state.getCurrentTemperature()
            # number = state.getCurrentTemperature() 
            # maxNumber = 99
            imageProgressState = (state.getCurrentWeather(), 29)
            maxNumberLength = 2
        elif self.getType() == 9: # UVindex
            number = random.randint(0, 12)
            maxNumber = 12
            maxNumberLength = 2
        elif self.getType() == 10: # AirQuality
            number = random.randint(0, 500)
            maxNumber = 500
            maxNumberLength = 3
        elif self.getType() == 11: # Humidity
            number = random.randint(0, 100)
            maxNumber = 100
            maxNumberLength = 3
        #TODO: other Activity implement
        
        if number is not None:
            if self.getDigits():
                for d in self.getDigits():
                    d.draw4(drawer, images, number, maxNumberLength)
            if self.getPointerProgress():
                self.getPointerProgress().draw4(drawer, images, number, maxNumber)
            if self.getImageProgress():
                self.getImageProgress().draw3(drawer, images, imageProgressState)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gtr2.elements.basic.valueElement import ValueElement
            self._type = parameter.getValue()
            return ValueElement(parameter, self, 'Type')
        elif parameterId == 2:
            from watchFaceParser.models.gtr2.elements.common.clockHandElement import ClockHandElement
            self._pointerProgress = ClockHandElement(parameter = parameter, parent = self, name = 'PointerProgress')
            return self._pointerProgress
        elif parameterId == 3:
            # ProgressBar
            pass
        elif parameterId == 4:
            from watchFaceParser.models.gtr2.elements.common.imageProgressElement import ImageProgressElement
            self._imageProgress = ImageProgressElement(parameter=parameter, parent=self, name='ImageProgress')
            return self._imageProgress
        elif parameterId == 5:
            from watchFaceParser.models.gtr2.elements.common.digitalCommonDigitElement import DigitalCommonDigitElement
            self._digits.append(DigitalCommonDigitElement(parameter = parameter, parent = self, name = 'Digits'))
            return self._digits
        elif parameterId == 7:
            from watchFaceParser.models.gtr2.elements.common.imageCoorsElement import ImageCoordsElement
            self._icon = ImageCoordsElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        else:
            return super(ActivityElement, self).createChildForParameter(parameter)

