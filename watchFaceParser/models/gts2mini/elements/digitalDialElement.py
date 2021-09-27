import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement


class DigitalDialElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._hours = None
        self._hoursdelimiter = None
        self._delimiter3 = None
        self._delimiter_hours = None
        self._time = None
        super(DigitalDialElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        assert(type(images) == list)

        hours = state.getTime().hour

        followxy = None

        if self._hours:
            followxy = self._hours.draw4(drawer, images, hours, 2, True)
            if self._hoursdelimiter:
                temp = images[self._hoursdelimiter].getBitmap()
                if followxy:
                    drawer.paste(temp, (followxy[0], followxy[1]), temp)
                    followxy = followxy[0] + temp.size[0], followxy[1]
            elif self._delimiter_hours:
                temp = images[self._delimiter_hours].getBitmap()
                if followxy:
                    drawer.paste(temp, (followxy[0], followxy[1]), temp)
                    followxy = followxy[0] + temp.size[0], followxy[1]

        if self._time:
            self._time.draw_time_element(drawer, images, state, followxy)

    def createChildForParameter(self, parameter):
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement

        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.common.numberElement import NumberElement
            self._hours = NumberElement(parameter = parameter, parent = self, name = 'Hours')
            return self._hours
        elif parameterId == 2:
            self._hoursdelimiter = parameter.getValue()
            return ValueElement(parameter, self, 'HoursDelimiterImageIndex')
        elif parameterId == 3:
            pass
        elif parameterId == 4:
            self._delimiter_hours = parameter.getValue()
            return ValueElement(parameter, self, 'DelimiterHours')
        elif parameterId == 5:
            pass
        elif parameterId == 6:
            pass
        elif parameterId == 7:
            pass
        elif parameterId == 8:
            from watchFaceParser.models.gts2mini.elements.time.timeElement import  TimeElement
            self._time = TimeElement(parameter = parameter, parent = self, name = 'Time')
            return self._time
        else:
            print ("Unknown TimeElement",parameterId)
            return super(DigitalDialElement, self).createChildForParameter(parameter)

