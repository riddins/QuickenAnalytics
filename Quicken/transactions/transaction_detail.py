'''need docstring'''

from .transaction_meta import TransactionMeta, DEBIT_CREDIT_VALUES

class TransactionDetail(metaclass=TransactionMeta):
    '''need docstring'''

    _data_binding_names = [
        'transaction_detail_create',
        'transaction_detail_read'
        ]

    def __new__(cls, name, bases, attrs):
        if (not attrs['transaction_detail_id'] is None
                and not attrs['parent_transaction'].transaction_id is None):
            if attrs['record'] is None:
                record = (super(TransactionMeta, cls)
                          .data_bindings['transaction_detail_read']
                          .binding_function(id=attrs['transaction_detail_id']))
                attrs['record'] = record[0] if len(record) > 0 else None
            if attrs['record'] is None:
                raise LookupError('transaction detail record not found')
            elif (attrs['parent_transaction']
                  .transaction_id == attrs['record'].TransactionId):
                instance = super().__new__(name, bases, attrs)
            else:
                raise ValueError('transaction detail record does not'
                                 'match parent transaction object')
        else:
            message = ('parent_transaction object '
                       'or transaction_detail_id invalid')
            raise ValueError(message, attrs['transaction_detail_id'],
                             attrs['parent_transaction'])
        return instance

    def __init__(self, parent_transaction, transaction_detail_id, record=None):
        if record.TransactionId == transaction_detail_id:
            self._transaction_detail_id = record.Id
            self._transaction = parent_transaction
            self._account = record.Account
            self._debit_credit = record.DebitCredit
            self._date = record.Date
            self._num = record.Num
            self._amount = record.Amount
            self._cleared = record.Cleared
            self._payee = record.Payee
            self._memo = record.Memo
            self._address = record.Address
            self._catagory = record.Catagory
            self._reimbursable_expense = record.ReimbursableExpense

    @classmethod
    def create_new(cls, query_params, cursor):
        '''need docstring'''
        func = (super(TransactionMeta, cls)
                .data_bindings['transaction_detail_create']
                .binding_function)
        cursor = func(query_params, cursor)
        return cursor


    @staticmethod
    def param_mapping(parent_transaction, account, debit_credit, date, amount,
                      **kwargs):
        '''need docstring'''
        if debit_credit in DEBIT_CREDIT_VALUES:
            query_params = {'TransactionId':parent_transaction.transaction_id,
                            'AccountId':account.account_id,
                            'DebitCredit':debit_credit,
                            'Date':date,
                            'Amount':amount,
                            'Payee':kwargs.get('payee', None),
                            'ReimbursableExpense':
                                kwargs.get('ReimbursableExpense', None),
                            'Num':kwargs.get('Num', None),
                            'Cleared':kwargs.get('Cleared', None),
                            'Memo':kwargs.get('Memo', None),
                            'Address':kwargs.get('Address', None),
                            'Catagory':kwargs.get('Catagory', None)
                           }
        else:
            query_params = None
        return query_params
