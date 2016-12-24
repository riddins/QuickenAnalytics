'''module implements dbcontext using pyodbc library'''
import pyodbc
from db_context import DbContext

class PyOdbcContext(DbContext):
    """description of class"""

    def __init__(self, connection_string):
        pyodbc.paramstyle = 'name'
        self._db = pyodbc.connect(connection_string)
        self._connection_string = connection_string
        super().__init__(connection_string)

    @staticmethod
    def get_sql_string(proc_name, *args):
        '''return sql string'''
        sql = 'EXEC {}'.format(proc_name)
        sql_params = (' ,'.join(' @{}=?'.format(arg) for arg in args)
                      if len(args) > 0 else '')
        sql += ('{}'.format(sql_params))
        return sql

    @property
    def connection(self):
        return self._db

    @property
    def connection_string(self):
        return self._connection_string

    def get_connection(self):
        return self._db

    def account_create(self, type_id, name, description,
                       parent_account_id=None):
        sql = 'app.cuspAccountCreate ?, ?, ?, ?'
        sql_params = (parent_account_id, type_id, name, description)
        return self.connection.execute(sql, sql_params)

    def account_read(self, account_id=None, name=None,
                     type_id=None, parent_account_id=None):
        sql = 'app.cuspAccountRead ?, ?, ?, ?'
        sql_params = (account_id, name, type_id, parent_account_id)
        return self.connection.execute(sql, sql_params)

    def account_type_create(self, account_type):
        sql = 'app.cuspAccountTypeCreate ?'
        return self.connection.execute(sql, account_type)

    def account_type_read(self, account_type_id=None, account_type=None):
        sql = 'app.cuspAccountTypeRead ?, ?'
        sql_params = (account_type_id, account_type)
        return self.connection.execute(sql, sql_params)

    def transaction_create(self, description=None):
        sql = 'app.cuspTransactionIdCreate @TransactionDescription = ?'
        cur = self.connection.execute(sql, (description))
        res = cur.fetchall()
        cur.commit()
        return res

    def transaction_read(self, transaction_id=None, status=None,
                         transaction_description=None):
        sql = 'app.cuspTransactionIdRead'
        sql_param_keys = ('Id', 'Status', 'TransactionDescription')
        sql = self.get_sql_string(sql, sql_param_keys)
        sql_param_vals = (transaction_id, status, transaction_description)
        cur = self.connection.execute(sql, sql_param_vals)
        return cur.fetchall()

    def transaction_detail_create(self, query_params, cur):
        '''Creates a new transaction detail record in the database.

        Constructs a parameterized SQL string; executes with the
        database cursor object passed from the caller; and returns
        the cursor to the caller.  The caller should evaluate the
        result and call the returned cursor's commit in order to
        commit the transaction to the database.

        Args:
            query_params:  A sequence of mapping objects.  Each mapping
                object in the sequence contains the key value pair for
                parameters to be inserted into a new transaction detail
                row in the database.  Key names and values must match
                the stored procedure parameter names and types in the
                database as follows:
                    MSSQL Stored Procedure Parameters:
                        @TransactionId int
                        @AccountId int
                        @DebitCredit char(1)
                        @Date date
                        @Amount decimal(10,2)
                        @Payee nvarchar(50)
                        @ReimbursableExpense bit
                        @Num nvarchar(10) = NULL
                        @Cleared nvarchar(1) = NULL
                        @Memo nvarchar(100) = NULL
                        @Address nvarchar(100) = NULL
                        @Catagory nvarchar(50) = NULL
            cur:  Optional cursor object

        Returns:
            A cursor object which the caller can use to evaluate
            the query result and commit the transaction.

        Raises:
            Nothing to add here
        '''
        sql = 'app.cuspTransactionDetailCreate'
        sql = self.get_sql_string(sql, *query_params[0].keys())
        lst = []
        for detail_row in query_params:
            lst.append(list(detail_row.values()))
        cur.executemany(sql, lst)
        return cur

    def transaction_detail_read(self, query_params):
        '''Reads transaction detail records from the database.

        Constructs a parameterized SQL string and executes with
        a database cursor object.  Returns a sequence of row objects
        to the caller.

        Args:
            query_params:  A sequence of mapping objects.  Each mapping
                object in the sequence contains the key value pair for
                parameters to be selected from transaction detail
                rows in the database.  Key names and values must match
                the stored procedure parameter names and types in the
                database as follows:
                    MSSQL Stored Procedure Parameters:
                        @Id int = NULL,
                        @TransactionId int = NULL,
                        @AccountId int = NULL,
                        @DebitCredit char(1) = NULL,
                        @Date date = NULL,
                        @Num nvarchar(10) = NULL,
                        @Amount decimal(10,2) = NULL,
                        @Cleared nvarchar(1) = NULL,
                        @Payee nvarchar(50) = NULL,
                        @Memo nvarchar(100) = NULL,
                        @Address nvarchar(100) = NULL,
                        @Catagory nvarchar(50) = NULL,
                        @ReimbursableExpense bit = NULL

        Returns:
            A sequence of row objects

        Raises:
            Nothing to add here
        '''
        sql = 'app.cuspTransactionDetailRead'
        sql = self.get_sql_string(sql, *query_params[0].keys())
        with self.connection.cursor() as cur:
            cur.executemany(sql, query_params)
            return cur.fetchall()
        