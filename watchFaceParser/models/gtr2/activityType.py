class ActivityType:
    Battery = 1
    Steps = 2
    Calories = 3
    HeartRate = 4
    PAI = 5
    Distance = 6
    UnknownActivity7 = 7
    Weather = 8
    UnknownActivity9 = 9
    AirQuality = 10
    Humidity = 11
   
    Converter = {
        Battery : "Battery",
        Steps : "Steps", 
        Calories : "Calories", 
        HeartRate : "HeartRate", 
        Distance : "Distance", 
        Weather : "Weather",  
        PAI : "PAI",  
        UnknownActivity7 : "UnknownActivity7",  
        UnknownActivity9 : "UnknownActivity9",  
        AirQuality : "AirQuality",  
        Humidity : "Humidity",  
    }

    def __init__(self, flag):
        self._flag = flag

    def hasFlag(self, flag):
        return (self._flag & flag) != 0

    def toJSON(self):
        if self._flag == None:
            self._flag = 0
        return ActivityType.Converter[self._flag]

    @staticmethod
    def fromJSON(strFlag):
        for flag in ActivityType.Converter:
            if strFlag == ActivityType.Converter[flag]:
                return flag
        return 0
