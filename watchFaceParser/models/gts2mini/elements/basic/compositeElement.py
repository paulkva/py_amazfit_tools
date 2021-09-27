import logging

from watchFaceParser.models.gts2mini.elements.basic.element import Element

class CompositeElement(Element):
    def __init__(self, parameters, parameter, parent, name):
        self._child = []
        if parameters is not None:
            for parameterChild in parameters:
                self._child.append(self.createChildForParameter(parameterChild))
        else:
            super(CompositeElement, self).__init__(parameter = parameter, parent = parent, name = name)
            if parameter.getChildren():
                for parameterChild in parameter.getChildren():
                    self._child.append(self.createChildForParameter(parameterChild))


    def getChildren(self):
        return self._child


    def createChilds(self, parameters):
        assert(type(parameters) == list)
        for parameterChild in parameters:
            self._child.append(self.createChildForParameter(parameterChild))


    def createChildForParameter(self, parameter):
        if parameter.hasChildren():
            from watchFaceParser.models.gts2mini.elements.basic.containerElement import ContainerElement
            return ContainerElement(parameters = None, parameter = parameter, parent = self, name = '')
        from watchFaceParser.models.gts2mini.elements.basic.valueElement import ValueElement
        return ValueElement(parameter = parameter, parent = self, name = '')


    def getDrawableChildren(self):
        t = []
        for child in self._child:
            try:
                getattr(child, 'draw3')
                t.append(child)
            except AttributeError:
                pass
        return t
