'''need docstring'''

from databindings.transaction_data_bindings import TransactionDataBindings

DEBIT_CREDIT_VALUES = [
    'd',
    'c',
    ]

class TransactionMeta(type):
    '''need docstring'''

    def __new__(mcs, name, bases, attrs):
        if '_data_binding_names' not in attrs:
            attrs['_data_binding_names'] = set()
        if '_data_bindings' not in attrs:
            names = attrs['_data_binding_names']
            attrs['_data_bindings'] = TransactionDataBindings({}, names)
        return super(TransactionMeta, mcs).__new__(mcs, name, bases, attrs)

    @property
    def data_bindings(cls):
        '''need docstring'''
        return cls._data_bindings

    @data_bindings.setter
    def data_bindings(cls, data_bindings):
        cls._data_bindings = data_bindings

    @property
    def data_binding_names(cls):
        '''need docstring'''
        return cls._data_binding_names
