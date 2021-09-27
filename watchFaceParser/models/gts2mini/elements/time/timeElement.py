﻿import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class TimeElement(ContainerElement):
    def __init__(self, parameter, parent, name = None):
        self._minutes = None
        self._seconds = None
        self._delimiter_minutes = None
        self._delimiter_seconds = None
        self._minutes_follow_hours = False
        self._seconds_follow_minutes = False
        self._coords10 = None
        self._coords11 = None
        super(TimeElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw_time_element(self, drawer, images, state, followxy):
        assert(type(images) == list)

        print(f"Minutes. followxy = {followxy}")
        if self._minutes:
            followxy = self._minutes.draw4(drawer,
                                           images,
                                           state.getTime().minute,
                                           minimumDights = 2,
                                           force_padding = True,
                                           followxy = followxy if self._minutes_follow_hours else None)
            if self._delimiter_minutes:
                temp = images[self._delimiter_minutes].getBitmap()
                if followxy:
                    drawer.paste(temp, (followxy[0], followxy[1]), temp)
                    followxy = followxy[0] + temp.size[0], followxy[1]
        print(f"Seconds. followxy = {followxy}")
        if self._seconds:
            followxy = self._seconds.draw4(drawer,
                                           images,
                                           state.getTime().second,
                                           minimumDights = 2,
                                           force_padding = True,
                                           followxy = followxy if self._seconds_follow_minutes else None)
            if self._delimiter_seconds:
                temp = images[self._delimiter_seconds].getBitmap()
                if followxy:
                    drawer.paste(temp, (followxy[0], followxy[1]), temp)
                    followxy = followxy[0] + temp.size[0], followxy[1]

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
            pass
        elif parameterId == 5:
            pass
        elif parameterId == 6:
            self._delimiter_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterMinutes')
        elif parameterId == 7:
            self._delimiter_seconds = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterSeconds')
        elif parameterId == 8:
            self._minutes_follow_hours = parameter.getValue()
            return ValueElement(parameter, self, 'MinutesFollowHours')
        elif parameterId == 9:
            self._seconds_follow_minutes = parameter.getValue()
            return ValueElement(parameter, self, 'SecondsFollowMinutes')
        elif parameterId == 10:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._coords10 = CoordinatesElement(parameter = parameter, parent = self, name = 'UnknownCoordinates10')
            return self._coords10
        elif parameterId == 11:
            from watchFaceParser.models.gts2mini.elements.common.coordinatesElement import CoordinatesElement
            self._coords11 = CoordinatesElement(parameter = parameter, parent = self, name = 'UnknownCoordinates11')
            return self._coords11
        else:
            super(TimeElement, self).createChildForParameter(parameter)
