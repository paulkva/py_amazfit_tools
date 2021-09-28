import logging

from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement

class ShortcutsElement(ContainerElement):
    def __init__(self, parameter, parent = None, name = None):
        self._shortcuts = []
        super(ShortcutsElement, self).__init__(parameters = None, parameter = parameter, parent = parent, name = name)

    def draw3(self, drawer, images, state):
        if self._shortcuts:
            for s in self._shortcuts:
                s.draw3(drawer, images, state)

    def createChildForParameter(self, parameter):
        parameterId = parameter.getId()
        if parameterId == 1:
            from watchFaceParser.models.gts2mini.elements.shortcut.shortcutElement import ShortcutElement
            self._shortcuts.append(ShortcutElement(parameter = parameter, parent = self, name = 'Shortcut'))
            return self._shortcuts
        else:
            return super(ShortcutsElement, self).createChildForParameter(parameter)