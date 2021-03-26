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

    from watchFaceParser.models.watchState import WatchState

    def draw3(self, drawer, images, state: WatchState):
        if self.getIcon():
            self.getIcon().draw3(drawer, images, None)
        number = None
        max_number = None
        max_number_length = 1
        image_progress_state = None

        from watchFaceParser.models.gtr2.activityType import ActivityType
        activity_flag = ActivityType(self.getType())

        if activity_flag.hasFlag(ActivityType.Battery) and state.getBatteryLevel() is not None:
            number = state.getBatteryLevel()
            max_number = 100
            max_number_length = 3
            image_progress_state = ( number, max_number)
        elif activity_flag.hasFlag(ActivityType.Steps) and state.getSteps() is not None:
            number = state.getSteps()
            max_number = state.getGoal()
            max_number_length = 5
            image_progress_state = (number, max_number)
        elif activity_flag.hasFlag(ActivityType.Calories) and state.getCalories() is not None:
            number = state.getCalories()
            max_number = 700
            max_number_length = 4
            image_progress_state = (number, max_number)
        elif activity_flag.hasFlag(ActivityType.HeartRate) and state.getPulse() is not None:
            number = state.getPulse()
            max_number = 250
            max_number_length = 3
            image_progress_state = (number, max_number)
        elif activity_flag.hasFlag(ActivityType.PAI) and state.getPai() is not None:
            number = state.getPai()
            max_number = 100
            max_number_length = 3
            image_progress_state = (number, max_number)
        elif activity_flag.hasFlag(ActivityType.Distance) and state.getDistance() is not None:
            number = state.getDistance() 
            max_number = state.getGoal() / 1000
            max_number_length = 4
        elif activity_flag.hasFlag(ActivityType.StandUp) and state.getStand() is not None:
            number = state.getStand()
            max_number = 12
            max_number_length = 2
            image_progress_state = (number, max_number)
        elif activity_flag.hasFlag(ActivityType.Weather):
            number = state.getCurrentTemperature() 
            max_number = 99
            image_progress_state = (state.getCurrentWeather(), 29)
            max_number_length = 2
        elif activity_flag.hasFlag(ActivityType.UVindex):
            number = state.getUVindex()
            max_number = 12
            max_number_length = 2
        elif activity_flag.hasFlag(ActivityType.AirQuality):
            number = random.randint(0, 500)
            max_number = 500
            max_number_length = 3
        elif activity_flag.hasFlag(ActivityType.Humidity):
            number = state.getHumidity()
            max_number = 100
            max_number_length = 3
        elif activity_flag.hasFlag(ActivityType.Sunrise):
            #number = random.randint(1, 2)
            #max_number = 2
            #max_number_length = 1
            image_progress_state = (random.randint(1, 2), 29)
        elif activity_flag.hasFlag(ActivityType.WindForce):
            number = random.randint(1, 12)
            max_number = 12
            max_number_length = 2
        elif activity_flag.hasFlag(ActivityType.AirPressure):
            number = random.randint(1, 999)
            max_number = 999
            max_number_length = 3
        #TODO: other Activity implement

        if number is not None:
            if self.getDigits():
                for d in self.getDigits():
                    d.draw4(drawer, images, number, max_number_length)
            if self.getPointerProgress():
                self.getPointerProgress().draw4(drawer, images, number, max_number)
            if self.getImageProgress():
                self.getImageProgress().draw3(drawer, images, image_progress_state)
            if self.getProgressBar():
                self.getProgressBar().draw4(drawer, images, number, max_number)

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
            from watchFaceParser.models.gtr2.elements.common.progressBarElement import ProgressBarElement
            self._progressBar = ProgressBarElement(parameter = parameter, parent = self, name = 'ProgressBar')
            return self._progressBar
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

