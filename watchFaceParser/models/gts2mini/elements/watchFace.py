import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class WatchFace(ContainerElement):
    def __init__(self, parameters):
        self._background = None
        self._time_separate_digits = None
        self._activity = None
        self._date = None
        self._weather = None
        self._stepsProgress = None
        self._caloriesProgress = None
        self._hearthProgress = None
        self._standUpProgress = None
        self._daysProgress = None
        self._status = None
        self._battery = None
        self._animation = None
        self._analogDial = None
        self._shorcuts = None
        self._digitalTime = None
        self._weather = None
        self._activity_separate_digits = None
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        logging.debug(f'>>>>>>>>>>>> {parameterId} {parameter}')
        if parameterId == 0:
            pass
        elif parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.backgroundElement import BackgroundElement
            self._background = BackgroundElement(parameter)
            return self._background
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.timeSeparateDigitsContainerElement import TimeSeparateDigitsContainerElement
            self._time_separate_digits = TimeSeparateDigitsContainerElement(parameter)
            return self._time_separate_digits
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.activityElement import ActivityElement
            self._activity = ActivityElement(parameter)
            return self._activity
        elif parameterId == 5:
            from watchFaceParser.models.gts2mini.elements.dateBlockElement import DateBlockElement
            self._date = DateBlockElement(parameter)
            return self._date
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.weatherElement import WeatherElement
            self._weather = WeatherElement(parameter)
            return self._weather
        elif parameterId == 7:
            from watchFaceParser.models.gts2mini.elements.activity.stepProgressElement import StepProgressElement
            self._stepsProgress = StepProgressElement(parameter)
            return self._stepsProgress
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.statusElement import StatusElement
            self._status = StatusElement(parameter)
            return self._status
        elif parameterId == 9:
            from watchFaceParser.models.gts2mini.elements.batteryElement import BatteryElement
            self._battery = BatteryElement(parameter)
            return self._battery
        elif parameterId == 10:
            pass
        elif parameterId == 11: # animation
            from watchFaceParser.models.gts2mini.elements.animationContainerElement import AnimationContainerElement
            self._animation = AnimationContainerElement(parameter)
            return self._animation
        elif parameterId == 12: # hearth progress
            from watchFaceParser.models.gts2mini.elements.activity.pulseProgressElement import PulseProgressElement
            self._hearthProgress = PulseProgressElement(parameter)
            return self._hearthProgress
        elif parameterId == 13: #
            pass
        elif parameterId == 14: #
            pass
        elif parameterId == 15: # calories progress
            from watchFaceParser.models.gts2mini.elements.activity.caloriesProgressElement import CaloriesProgressElement
            self._caloriesProgress = CaloriesProgressElement(parameter)
            return self._caloriesProgress
        elif parameterId == 16:  #
            pass
        elif parameterId == 17:  #
            pass
        elif parameterId == 18:  #
            pass
        elif parameterId == 19: #
            from watchFaceParser.models.gts2mini.elements.shortcutsElement import ShortcutsElement
            self._shorcuts = ShortcutsElement(parameter)
            return self._shorcuts
        elif parameterId == 20:
            from watchFaceParser.models.gts2mini.elements.analogDialElement import AnalogDialElement
            self._analogDial = AnalogDialElement(parameter)
            return self._analogDial
        elif parameterId == 21:
            from watchFaceParser.models.gts2mini.elements.digitalDialElement import DigitalDialElement
            self._digitalTime = DigitalDialElement(parameter)
            return self._digitalTime
        elif parameterId == 21:  #
            pass
        elif parameterId == 22: #
            pass
        elif parameterId == 23: #
            pass
        elif parameterId == 24:  # standup progress
            from watchFaceParser.models.gts2mini.elements.activity.standupProgressElement import StandUpProgressElement
            self._standUpProgress = StandUpProgressElement(parameter)
            return self._standUpProgress
        elif parameterId == 25:  #
            pass
        elif parameterId == 26:  #
            pass
        elif parameterId == 27:  #
            pass
        elif parameterId == 28: #
            pass
        elif parameterId == 29: #
            pass
        elif parameterId == 30: #
            from watchFaceParser.models.gts2mini.elements.activity.activitySeparateDigitsElement import ActivitySeparateDigitsElement
            self._activity_separate_digits = ActivitySeparateDigitsElement(parameter)
            return self._activity_separate_digits
        else:
            print ("Unknown WatchFace",parameterId)
            return super(WatchFace, self).createChildForParameter(parameter)
