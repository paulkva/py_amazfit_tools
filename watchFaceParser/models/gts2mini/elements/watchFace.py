import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class WatchFace(ContainerElement):
    def __init__(self, parameters):
        self._background = None
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
        self._analogDial = None
        self._digitalTime = None
        self._weather = None
        super(WatchFace, self).__init__(parameters, parameter = None, parent = None, name = '')


    def getBackground(self):
        return self._background


    def getTime(self):
        print ("GETTIME")
        return self._digitalTime


    def getActivity(self):
        return self._activity


    def getDate(self):
        return self._date


    def getWeather(self):
        return self._weather


    def getStepsProgress(self):
        return self._stepsProgress


    def getDaysProgress(self):
        return self._daysProgress


    def getStatus(self):
        return self._status


    def getBattery(self):
        return self._battery


    def getAnalogDial(self):
        return self._analogDial

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
            pass
        elif parameterId == 4:
            pass
            # from watchFaceParser.models.gts2mini.elements.activityElement import ActivityElement
            # self._activity = ActivityElement(parameter)
            # return self._activity
        elif parameterId == 5:
            pass
            # from watchFaceParser.models.gts2mini.elements.dateElement import DateElement
            # self._date = DateElement(parameter)
            # return self._date
        elif parameterId == 6:
            pass
            # from watchFaceParser.models.gts2mini.elements.weatherElement import WeatherElement
            # self._weather = WeatherElement(parameter)
            # return self._weather
        elif parameterId == 7:
            pass
            # from watchFaceParser.models.gts2mini.elements.progressElement import ProgressElement
            # self._stepsProgress = ProgressElement(parameter)
            # return self._stepsProgress
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.statusElement import StatusElement
            self._status = StatusElement(parameter)
            return self._status
        elif parameterId == 9:
            pass
            # from watchFaceParser.models.gts2mini.elements.batteryElement import BatteryElement
            # self._battery = BatteryElement(parameter)
            # return self._battery
        elif parameterId == 10:
            pass
        elif parameterId == 11: # animation
            pass
        elif parameterId == 12: # hearth progress
            pass
            # from watchFaceParser.models.gts2mini.elements.progressElement import ProgressElement
            # self._hearthProgress = ProgressElement(parameter)
            # return self._hearthProgress
        elif parameterId == 13: #
            pass
        elif parameterId == 14: #
            pass
        elif parameterId == 15: # calories progress
            pass
            # from watchFaceParser.models.gts2mini.elements.progressElement import ProgressElement
            # self._caloriesProgress = ProgressElement(parameter)
            # return self._caloriesProgress
        elif parameterId == 16:  #
            pass
        elif parameterId == 17:  #
            pass
        elif parameterId == 18:  #
            pass
        elif parameterId == 19: #
            pass
        elif parameterId == 20:
            from watchFaceParser.models.gts2mini.elements.analogDialElement import AnalogDialElement
            self._analogDial = AnalogDialElement(parameter)
            return self._analogDial
        elif parameterId == 21:
            pass
            # from watchFaceParser.models.gts2mini.elements.digitalDialElement import DigitalDialElement
            # self._digitalTime = DigitalDialElement(parameter)
            # return self._digitalTime
        elif parameterId == 21:  #
            pass
        elif parameterId == 22: #
            pass
        elif parameterId == 23: #
            pass
        elif parameterId == 24:  # standup progress
            pass
            # from watchFaceParser.models.gts2mini.elements.progressElement import ProgressElement
            # self._standUpProgress = ProgressElement(parameter)
            # return self._standUpProgress
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
        else:
            print ("Unknown WatchFace",parameterId)
            return super(WatchFace, self).createChildForParameter(parameter)
