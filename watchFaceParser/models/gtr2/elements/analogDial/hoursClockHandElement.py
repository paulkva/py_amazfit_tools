from watchFaceParser.models.gtr2.elements.common.clockHandElement import ClockHandElement

class HoursClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(HoursClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        value = state.getTime().hour % 12 + state.getTime().minute / 60.
        maxvalue = 12
        super(HoursClockHandElement, self).draw4(drawer, resources, value, maxvalue)
