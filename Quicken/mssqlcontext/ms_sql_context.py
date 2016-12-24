'''module implements dbcontext using mssql library'''

import _mssql
from db_context import DbContext

class MsSqlContext(DbContext):
    """description of class"""

    _db = None

    def __init__(self, connection_string):
        #self._db = pyodbc.connect(connection_string)
        self._connection_string = connection_string
        super().__init__()

    @property
    def connection(self):
        return self._db

    @property
    def connection_string(self):
        return self._connection_string

    def get_connection(self):
        raise NotImplementedError('must define getConnection to use this base class')

    def account_create(self, type_id, name, description, parent_account_id=None):
        raise NotImplementedError('must define AccountCreate to use this base class')

    def account_read(self, account_id=None, name=None, type_id=None, parent_account_id=None):
        raise NotImplementedError('must define AccountRead to use this base class')

    def account_type_create(self, account_type):
        #raise NotImplementedError('must define AccountTypeCreate to use this base class')
        stored_proc = self.__get_connection().init_procedure('cuspAccountTypeCreate')
        stored_proc.bind(value=self.account_type, dbtype='SQLVARCHAR', name='@AccountType')
        return stored_proc.execute()

    def account_type_read(self, account_type_id=None, account_type=None):
        raise NotImplementedError('must define AccountTypeRead to use this base class')

    def transaction_create(self, account_id, to_account_id, date, amount, payee, reimbursable_expense,
                           split_parent=None, num=None, cleared=None, memo=None,
                           address=None, catagory=None):
        raise NotImplementedError('must define TransactionCreate to use this base class')

    def transaction_read(self, transaction_id=None, account_id=None, to_account_id=None, split_parent=None,
	                        date=None, num=None, amount=None, cleared=None, payee=None,
	                        memo=None, address=None, catagory=None, reimbursable_expense=None):
        raise NotImplementedError('must define TransactionRead to use this base class')

    def __get_connection(self):
        if not isinstance(self._db, _mssql.MSSQLConnection):
            self._db = _mssql.connect(server='iddins.database.windows.net')
        return self._db
