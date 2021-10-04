import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._minutes = None
        self._seconds = None
        self._padding_zero_minutes = None
        self._padding_zero_seconds = None
        self._minutes_data_type = None
        self._seconds_data_type = None
        self._minutes_follow_hours = False
        self._seconds_follow_minutes = False
        self._hours_data_type_coordinates = None
        self._minutes_data_type_coordinates = None
        self._seconds_data_type_coordinates = None
        super(TimeElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def getHoursDataTypeCoordinates(self):
        return self._hours_data_type_coordinates

    def draw_time_element(self, drawer, images, state, followxy, delimiter_minutes=None, delimiter_seconds=None):
        assert(type(images) == list)

        if self._minutes:
            followxy = self._minutes.draw4(drawer,
                                           images,
                                           state.getTime().minute,
                                           minimumDigits = 2,
                                           force_padding = self._padding_zero_minutes,
                                           followxy = followxy if self._minutes_follow_hours else None,
                                           suffix = delimiter_minutes)
            if self._minutes_data_type_coordinates and self._minutes_data_type:
                self.drawDelimiter(drawer, images, self._minutes_data_type, self._minutes_data_type_coordinates)

        if self._seconds:
            followxy = self._seconds.draw4(drawer,
                                           images,
                                           state.getTime().second,
                                           minimumDigits = 2,
                                           force_padding = self._padding_zero_seconds,
                                           followxy = followxy if self._seconds_follow_minutes else None,
                                           suffix = delimiter_seconds)
            if self._seconds_data_type_coordinates and self._seconds_data_type:
                self.drawDelimiter(drawer, images, self._seconds_data_type, self._seconds_data_type_coordinates)

    def drawDelimiter(self, drawer, images, index, coordinates):
        temp = images[index].getBitmap()
        drawer.paste(temp, (coordinates._x, coordinates._y), temp)
        return coordinates._x + temp.size[0], coordinates._y

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()

        if parameterId == 1:
            pass
        elif parameterId == 2:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._minutes = NumberElement(parameter, self, 'Minutes')
            return self._minutes
        elif parameterId == 3:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._seconds = NumberElement(parameter, self, 'Seconds')
            return self._seconds
        elif parameterId == 4:
            self._padding_zero_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroMinutes')
        elif parameterId == 5:
            self._padding_zero_seconds = parameter.getValue()
            return ValueElement(parameter, self, 'PaddingZeroSeconds')
        elif parameterId == 6:
            self._minutes_data_type = parameter.getValue()
            return ValueElement(parameter, self, 'MinutesDataTypeImageIndex')
        elif parameterId == 7:
            self._seconds_data_type = parameter.getValue()
            return ValueElement(parameter, self, 'SecondsDataTypeImageIndex')
        elif parameterId == 8:
            self._minutes_follow_hours = parameter.getValue()
            return ValueElement(parameter, self, 'MinutesFollowHours')
        elif parameterId == 9:
            self._seconds_follow_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'SecondsFollowMinutes')
        elif parameterId == 10:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._hours_data_type_coordinates = CoordinatesElement(parameter = parameter, parent = self, name ='HoursDataTypeCoordinates')
            return self._hours_data_type_coordinates
        elif parameterId == 11:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._minutes_data_type_coordinates = CoordinatesElement(parameter = parameter, parent = self, name ='MinutesDataTypeCoordinates')
            return self._minutes_data_type_coordinates
        elif parameterId == 12:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._seconds_data_type_coordinates = CoordinatesElement(parameter = parameter, parent = self, name ='SecondsDataTypeCoordinates')
            return self._seconds_data_type_coordinates
        else:
            super(TimeElement, self).createChildForParameter(parameter)
