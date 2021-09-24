from watchFaceParser.models.gts2mini.elements.common.switchElement import SwitchElement


class UnlockedElement(SwitchElement):
    def __init__(self, parameter, parent, name = None):
        super(UnlockedElement, self).__init__(parameter = parameter, parent = parent, name = name)

    def switchState(self, state):
        return state.getUnlocked()
