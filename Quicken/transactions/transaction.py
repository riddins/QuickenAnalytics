'''need docstring'''

from .transaction_meta import TransactionMeta

class Transaction(object, metaclass=TransactionMeta):
    """description of class"""
    """[Id] INT NOT NULL PRIMARY KEY IDENTITY
	,[Status] CHAR(1) NOT NULL DEFAULT 'o'
	,[TransactionDescription] NVARCHAR(50) NULL
    """

    _transaction_status_values = [
        'o',  #     OPEN (DEFAULT):     Can post new TransactionDetail for
              #                             this TransactionId
        'c',  #     CLEARED:            All TransactionDetail has posted and
              #                             Debits = Credits.  No new
              #                             Transaction Detail can be posted
        'v',  #     VOID:               Reserved for voiding the transaction
              #                             and all realted detail
        'r',  #     RECONCILED:         Reserved for reconciliation process
        's',  #     STATIC:             Reserved for system use
              #                             (e.g. unmatched transfers)
    ]

    _data_binding_names = [
        'transaction_create',
        'transaction_read',
    ]

    def __init__(self, transaction_id=None):
        if not transaction_id is None:
            tmp = (super(TransactionMeta, self)
                   .data_bindings['transaction_read']
                   .binding_function(transaction_id))
            if len(tmp) > 0:
                self._id = tmp[0].Id
                self._status = tmp[0].Status
                self._transaction_description = tmp[0].TransactionDescription
                # note to add in _transaction_details
        else:
            self._id = None
            self._status = 'o'
            self._transaction_description = None
            self._transaction_details = set()

    def __str__(self):
        as_string = '(id: {}, status: {}, transaction_description: {})'
        return as_string.format(self._id,
                                self._status,
                                self._transaction_description)

    def commit(self):
        '''need docstring'''
        if self._id is None:
            tmp = (type(self).data_bindings['transaction_create']
                   .binding_function(self._transaction_description))
            if len(tmp) > 0:
                return Transaction(tmp[0].Id)

    @classmethod
    @property
    def transaction_status_values(cls):
        '''need docstring'''
        return cls._transaction_status_values

    @property
    def transaction_details(self):
        '''need docstring'''
        return tuple(self._transaction_details)

    def add_transaction_detail(self, transaction_detail):
        '''need docstring'''
        if self._status in ('o', 's') and self._id is None:
            self._transaction_details.add(transaction_detail)
        elif not self._id is None:
            type(self).data_bindings['transaction_create']()
