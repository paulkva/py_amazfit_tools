import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class WeatherElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._icon = None
        self._temperature = None
        self._humidity = None
        self._uv = None
        super(WeatherElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.weather.weatherIconElement import WeatherIconElement
            self._icon = WeatherIconElement(parameter = parameter, parent = self, name = 'Icon')
            return self._icon
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.weather.temperatureElement import TemperatureElement # temp.
            self._temperature = TemperatureElement(parameter = parameter, parent = self, name = 'Temperature')
            return self._temperature
        elif parameterId == 4:
            from watchFaceParser.models.gts2mini.elements.weather.humidityElement import HumidityElement
            self._humidity = HumidityElement(parameter = parameter, parent = self, name = 'Humidity')
            return self._humidity
        elif parameterId == 6:
            from watchFaceParser.models.gts2mini.elements.weather.uvindexElement import UvindexElement
            self._uv = UvindexElement(parameter = parameter, parent = self, name = 'UVindex')
            return self._uv
        else:
            print ("Unknown WeatherElement",parameterId)
            return super(WeatherElement, self).createChildForParameter(parameter)

