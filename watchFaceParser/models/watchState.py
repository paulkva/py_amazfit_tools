import datetime

from watchFaceParser.models.weatherCondition import WeatherCondition


class WatchState:
    def __init__(self, BatteryLevel=67, Pulse=62, Steps=14876, Calories=764, Distance=2367,
                 Bluetooth=True, Unlocked=True, Alarm=True, DoNotDisturb=True,
                 CurrentTemperature=-10, Stand=3, PAI=30, Humidity=50, UVindex=5, AirQuality=5):
        # self._time = datetime.datetime.now().replace(hour = 10, minute = 10, second = 30)
        self._time = datetime.datetime.now()
        self._steps = Steps
        self._goal = 8000
        self._distance = Distance
        self._calories = Calories
        self._pulse = Pulse
        self._batteryLevel = BatteryLevel
        self._bluetooth = Bluetooth
        self._unlocked = Unlocked
        self._alarm = Alarm
        self._doNotDisturb = DoNotDisturb
        self._stand = Stand
        self._pai = PAI
        self._humidity = Humidity
        self._uvindex = UVindex
        self._airquality = AirQuality
        self._screenidle = None
        self._currentWeather = WeatherCondition.PartlyCloudy
        self._currentTemperature = CurrentTemperature

    def getTime(self):
        return self._time

    def setTime(self, _time):
        self._time = _time

    def getSteps(self):
        return self._steps

    def getGoal(self):
        return self._goal

    def getPulse(self):
        return self._pulse

    def getBatteryLevel(self):
        return self._batteryLevel

    def getDistance(self):
        return self._distance

    def getCalories(self):
        return self._calories

    def getBluetooth(self):
        return self._bluetooth

    def getUnlocked(self):
        return self._unlocked

    def getAlarm(self):
        return self._alarm

    def getDoNotDisturb(self):
        return self._doNotDisturb

    def getWeather(self):
        return self._weather

    def getCurrentWeather(self):
        return self._currentWeather

    def getCurrentTemperature(self):
        return self._currentTemperature

    def setCurrentWeather(self, n):
        self._currentWeather = n

    def setCurrentTemperature(self, n):
        self._currentTemperature = n

    def getStand(self):
        return self._stand

    def getPai(self):
        return self._pai

    def getHumidity(self):
        return self._humidity

    def getUVindex(self):
        return self._uvindex

    def getAirQuality(self):
        return self._airquality

    def getScreenIdle(self):
        return self._screenidle

    def setScreenIdle(self, screenIdle):
        self._screenidle = screenIdle

    def toJSON(self):
        return {
            'Time': self.datetimeToJson(),
            'Steps': self._steps,
            'Goal': self._goal,
            'Pulse': self._pulse,
            'BatteryLevel': self._batteryLevel,
            'Distance': self._distance,
            'Calories': self._calories,
            'Bluetooth': self._bluetooth,
            'Unlocked': self._unlocked,
            'Alarm': self._alarm,
            'DoNotDisturb': self._doNotDisturb,
            'CurrentWeather': self._currentWeather,
            'CurrentTemperature': self._currentTemperature,
            'Stand': self._stand,
            'PAI': self._pai,
            'Humidity': self._humidity,
            'UVindex': self._uvindex,
            'AirQuality': self._airquality,
            'ScreenIdle': self._screenidle
        }

    def datetimeToJson(self):
        t = self._time
        return {'Year': t.year, 'Month': t.month, 'Day': t.day, 'Hour': t.hour, 'Minute': t.minute, 'Second': t.second}

    @staticmethod
    def fromJson(j):
        w = WatchState()
        t = j['Time']
        w._time = datetime.datetime.now().replace(
            year=t['Year'],
            month=t['Month'],
            day=t['Day'],
            hour=t['Hour'],
            minute=t['Minute'],
            second=t['Second'])
        w._steps = j['Steps']
        w._goal = j['Goal']
        w._pulse = j['Pulse']
        w._batteryLevel = j['BatteryLevel']
        w._distance = j['Distance']
        w._calories = j['Calories']
        w._bluetooth = j['Bluetooth']
        w._unlocked = j['Unlocked']
        w._alarm = j['Alarm']
        w._doNotDisturb = j['DoNotDisturb']
        w._currentWeather = j['CurrentWeather']
        w._currentTemperature = j['CurrentTemperature']
        w._stand = j['Stand']
        w._pai = j['PAI']
        w._humidity = j['Humidity']
        w._uvindex = j['UVindex']
        w._airquality = j['AirQuality']
        w._screenidle = j['ScreenIdle']
        return w
