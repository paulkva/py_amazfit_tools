﻿from watchFaceParser.models.elements.common.circularProgressElement import CircularProgressElement

class KcalProgressElement(CircularProgressElement):
    def __init__(self, parameter, parent, name = 'None'):
        super(KcalProgressElement, self).__init__(parameter, parent, name)

    def draw3(self, drawer, resources, state):
        assert(type(resources) == list)
        if state.getGoal():
            self.draw4(drawer, resources, state.getGoal(), 100)
