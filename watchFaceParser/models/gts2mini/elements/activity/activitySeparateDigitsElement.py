import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class ActivitySeparateDigitsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._calories = None
        self._battery = None
        self._steps = None
        self._pulse = None
        super(ActivitySeparateDigitsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getCalories(self):
        return self._calories

    def getBattery(self):
        return self._battery

    def getSteps(self):
        return self._steps

    def getPulse(self):
        return self._pulse

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        calories = state.getCalories() % 10000
        if self.getCalories():
            self.getCalories().draw4(drawer, images, calories, padding_zero=False)

        battery = state.getBatteryLevel() % 1000
        if self.getBattery():
            self.getBattery().draw4(drawer, images, battery, padding_zero=False)

        steps = state.getSteps() % 100000
        if self.getSteps():
            self.getSteps().draw4(drawer, images, steps, padding_zero=False)

        pulse = state.getPulse() % 1000
        if self.getPulse():
            self.getPulse().draw4(drawer, images, pulse, padding_zero=False)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.fourDigitsElement import FourDigitsElement
            self._calories = FourDigitsElement(parameter = parameter, parent = self, name = 'Calories')
            return self._calories
        elif parameterId == 2: # bat
            from watchFaceParser.models.gts2mini.elements.common.threeDigitsElement import ThreeDigitsElement
            self._battery = ThreeDigitsElement(parameter=parameter, parent=self, name='Battey')
            return self._battery
        elif parameterId == 3: # steps
            from watchFaceParser.models.gts2mini.elements.common.fiveDigitsElement import FiveDigitsElement
            self._steps = FiveDigitsElement(parameter=parameter, parent=self, name='Steps')
            return self._steps
        elif parameterId == 4: # pulse
            from watchFaceParser.models.gts2mini.elements.common.fourDigitsElement import FourDigitsElement
            self._pulse = FourDigitsElement(parameter=parameter, parent=self, name='Steps')
            return self._pulse
        else:
            print ("Unknown ActivitySeparateDigitsElement",parameterId)
            return super(ActivitySeparateDigitsElement, self).createChildForParameter(parameter)

