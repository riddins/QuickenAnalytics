'''need docstring'''

from accounts import *
#from accounts.account import Account
#from accounts.account_type import AccountType
from databindings.data_binding import DataBinding
from databindings.transaction_data_bindings import TransactionDataBindings

class QuickenFactory(object):
    '''need docstring'''

    def __init__(self, context):
        self._db_context = context
        self._account_types = {}
        self._account_classes = {}
        for cls in Account.__subclasses__():
            cursor = self._db_context.account_type_read(account_type=cls.__name__)
            row = cursor.fetchone()
            if row is None:
                cursor = self._db_context.account_type_create(account_type=cls.__name__)
                row = cursor.fetchone()
                cursor.commit()
                cursor = self._db_context.account_type_read(account_type_id=row.Id)
                row = cursor.fetchone()
            cls.account_type = AccountType(row.Id, row.AccountType)
            self._account_types[cls.account_type.account_type_name] = cls.account_type
            self._account_classes[cls.account_type.account_type_name] = cls

    def get_transaction_data_bindings(self, data_binding_names):
        '''need docstring'''
        data_bindings_dict = {}
        for name in data_binding_names:
            data_bindings_dict[name] = DataBinding(name, getattr(self._db_context, name))
        return TransactionDataBindings(data_bindings_dict, data_binding_names)

    def get_account(self, account_type, account_id=None, name=None, description=None, parent_id=None):
        '''need docstring'''
        if account_id is None and name is None:
            return None
        else:
            cursor = self._db_context.account_read(account_id=account_id, name=name, type_id=account_type.account_type_id, parent_account_id=parent_id)
            row = cursor.fetchone()
            if row is None:
                cursor = self._db_context.account_create(account_type.account_type_id, name, description, parent_id)
                row = cursor.fetchone()
                cursor.commit()
                cursor = self._db_context.account_read(
                    account_id=account_id, name=name, type_id=account_type.account_type_id,
                    parent_account_id=parent_id)
                row = cursor.fetchone()
            cursor = self._db_context.account_type_read(account_type_id=row.TypeId)
            type_row = cursor.fetchone()
            if type_row is None:
                return None
            else:
                return self._account_classes[type_row.AccountType](
                    account_id=row.Id, parent_account_id=row.ParentAccountId,
                    account_name=row.Name, account_description=row.Description)

    @property
    def account_types(self):
        '''need docstring'''
        return self._account_types
