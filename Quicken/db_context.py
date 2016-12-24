'''doc string needed'''

import abc

class DbContext(metaclass=abc.ABCMeta):
    '''doc string needed'''

    @abc.abstractmethod
    def __init__(self, connection_string):
        self._connection_string = connection_string

    @property
    @abc.abstractmethod
    def connection(self):
        '''doc string needed'''
        raise NotImplementedError('must define read-only property connection to use this base class')

    @property
    @abc.abstractmethod
    def connection_string(self):
        '''doc string needed'''
        raise NotImplementedError('must define read-only property connection_string to use this base class')

    @abc.abstractmethod
    def get_connection(self):
        '''doc string needed'''
        raise NotImplementedError('must define getConnection to use this base class')

    @abc.abstractmethod
    def account_create(self, type_id, name, description, parent_account_id=None):
        '''doc string needed'''
        raise NotImplementedError('must define AccountCreate to use this base class')

    @abc.abstractmethod
    def account_read(self, account_id=None, name=None, type_id=None, parent_account_id=None):
        '''doc string needed'''
        raise NotImplementedError('must define AccountRead to use this base class')

    @abc.abstractmethod
    def account_type_create(self, account_type):
        '''doc string needed'''
        raise NotImplementedError('must define AccountTypeCreate to use this base class')

    @abc.abstractmethod
    def account_type_read(self, account_type_id=None, account_type=None):
        '''doc string needed'''
        raise NotImplementedError('must define AccountTypeRead to use this base class')

    @abc.abstractmethod
    def transaction_create(self, description=None):
        '''doc string needed'''
        raise NotImplementedError('must define TransactionCreate to use this base class')

    @abc.abstractmethod
    def transaction_read(self, transaction_id=None, status=None, transaction_description=None):
        '''doc string needed'''
        raise NotImplementedError('must define TransactionRead to use this base class')

    @abc.abstractmethod
    def transaction_detail_create(self, query_params, cur):
        '''doc string needed'''
        raise NotImplementedError('must define TransactionCreate to use this base class')

    @abc.abstractmethod
    def transaction_detail_read(self, query_params):
        '''doc string needed'''
        raise NotImplementedError('must define TransactionRead to use this base class')
