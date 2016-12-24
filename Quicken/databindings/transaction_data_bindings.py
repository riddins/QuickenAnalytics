'''need docstring'''

from collections import Mapping
from .data_binding import DataBinding

class TransactionDataBindings(Mapping):
    '''need docstring'''

    @classmethod
    def _binding_not_implemented(cls):
        raise NotImplementedError('data binding not implemented')

    def __init__(self, bindings, data_binding_names):

        for binding_name in data_binding_names:
            if not binding_name in bindings:
                bindings[binding_name] = DataBinding(binding_name, self._binding_not_implemented)
        for binding in bindings.copy():
            if not binding in data_binding_names:
                del bindings[binding]
        self._bindings = bindings
        super().__init__()

    def __len__(self):
        return len(self._bindings)

    def __getitem__(self, key):
        for i in self._bindings:
            if i == key:
                binding = self._bindings[i]
                break
        else: binding = super().__getitem__(key)

        return binding

    def __iter__(self):
        for i in self._bindings:
            yield self._bindings[i]
        return super().__iter__()
