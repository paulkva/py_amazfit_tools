import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class ActivityElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._steps = None
        self._calories = None
        self._pulse = None
        self._pai = None
        self._standUp = None
        self._distance = None
        self._unknown7 = None
        super(ActivityElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.activity.stepsElement import StepsElement
            self._steps = StepsElement(parameter = parameter, parent = self, name = 'Steps')
            return self._steps
        elif parameterId == 2:
            pass
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.activity.caloriesElement import CaloriesElement
            self._calories = CaloriesElement(parameter = parameter, parent = self, name = 'Calories')
            return self._calories
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.activity.pulseElement import PulseElement
            self._pulse = PulseElement(parameter = parameter, parent = self, name = 'HeartRate')
            return self._pulse
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.activity.distanceElement import DistanceElement
            self._distance = DistanceElement(parameter = parameter, parent = self, name = 'Distance')
            return self._distance
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.activity.paiElement import PaiElement
            self._pai = PaiElement(parameter=parameter, parent=self, name='PAI')
            return self._pai
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
            self._unknown7 = parameter.getValue()
            return ValueElement(parameter, self, 'UnknownLongValue7')
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.activity.standupElement import StandUpElement
            self._standUp = StandUpElement(parameter = parameter, parent = self, name = 'StandUp')
            return self._standUp
        else:
            return super(ActivityElement, self).createChildForParameter(parameter)

