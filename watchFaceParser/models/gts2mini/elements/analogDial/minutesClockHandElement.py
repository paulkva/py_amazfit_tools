from watchFaceParser.models.gts2mini.elements.common.clockHandElement import ClockHandElement


class MinutesClockHandElement(ClockHandElement):
    def __init__(self, parameter, parent = None, name = None):
        super(MinutesClockHandElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def draw4(self, drawer, resources, state, center):
        assert (type(resources) == list)

        self._center = center
        self.draw3(drawer, resources, state)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(MinutesClockHandElement, self).draw4(drawer, resources, state.getTime().minute, 60)
