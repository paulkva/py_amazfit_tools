import logging

from watchFaceParser.models.gts2mini.elements.common.scaleElement import ScaleElement


class BatteryScaleElement(ScaleElement):
    def __init__(self, parameter, parent, name = None):
        super(BatteryScaleElement, self).__init__(parameter = parameter, parent = parent, name = name)


    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        super(BatteryScaleElement, self).draw4(drawer, resources, state.getBatteryLevel(), 100)

