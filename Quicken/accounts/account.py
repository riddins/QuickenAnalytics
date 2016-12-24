"""This module defines the account class"""

import abc

#    [Id] INT NOT NULL PRIMARY KEY IDENTITY
#	,[ParentAccountId] INT NULL
#	,[TypeId] INT NOT NULL
#	,[Name] NVARCHAR(50) NOT NULL
#	,[Description] NVARCHAR(50) NOT NULL

class Account(object, metaclass=abc.ABCMeta):
    """Account Class"""

    __slots__ = ["_id", "_parent_account_id", "_account_name",
                 "_account_description"]

    def __init__(self, account_id, parent_account_id, account_name,
                 account_description):
        self._id = account_id
        self._parent_account_id = parent_account_id
        self._account_name = account_name
        self._account_description = account_description

    @property
    @classmethod
    def account_type(cls):
        '''property returning type of account'''
        return cls._account_type

    @account_type.setter
    @classmethod
    def account_type(cls, account_type):
        '''need to add docstring'''
        cls._account_type = account_type

    @property
    def account_id(self):
        '''property returns the value of id for the instance'''
        return self._id

    @property
    def parent_account_id(self):
        '''property returns the value of parent account id for the instance'''
        return self._parent_account_id

    @property
    def account_name(self):
        '''property returns string for the name of the account'''
        return self._account_name

    @property
    def account_description(self):
        '''property returns string describing the account'''
        return self._account_description

    @property
    @abc.abstractmethod
    def account_balance(self):
        '''property returns double for accumulated sum of tranactions
           in the account'''
        raise NotImplementedError('must define read-only property \
                                    "account_balance" to use this base class')
