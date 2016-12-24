'''need docstring'''

class DataBinding(object):
    '''need docstring'''

    __slots__ = {'_binding_name', '_binding_function'}

    def __init__(self, name, function):
        self._binding_name = name
        self._binding_function = function

    @property
    def binding_name(self):
        '''need docstring'''
        return self._binding_name

    @property
    def binding_function(self):
        '''need docstring'''
        return self._binding_function

    def __call__(self):
        return self.binding_function
