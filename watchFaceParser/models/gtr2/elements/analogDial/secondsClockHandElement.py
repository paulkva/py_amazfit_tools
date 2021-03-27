from watchFaceParser.models.gtr2.elements.common.clockHandElement import ClockHandElement


class SecondsClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(SecondsClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        value = state.getTime().second
        maxvalue = 60
        super(SecondsClockHandElement, self).draw4(drawer, resources, value, maxvalue)
