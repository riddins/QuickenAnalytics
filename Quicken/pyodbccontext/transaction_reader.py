from transaction import Transaction

class TransactionWriter(object):
    '''need docstring'''

    def __init__(self, context):
        '''need docstring'''
        self._db = context
    
    def write_transaction(self, transaction):
        
        cursor = self._db.connection.cursor
        if transaction.id is None:
            self._db.write_transaction()
        
