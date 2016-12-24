'''need docstring'''

class AccountType(object):
    '''AccountType class'''

    __slots__ = ["_id", "_account_type_name"]

    def __init__(self, account_type_id, account_type_name):
        self._id = account_type_id
        self._account_type_name = account_type_name

    @property
    def account_type_id(self):
        ''' property returning integer identifier for the type'''
        return self._id

    @property
    def account_type_name(self):
        '''property returning string for name of type'''
        return self._account_type_name
        