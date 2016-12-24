'''need docstring'''

#from qifparse.parser import QifParser

#import account
#from .pyodbccontext.py_odbc_context import *
#from mssqlcontext.ms_sql_context import *
#from .db_context import *
from quicken_factory import QuickenFactory
from transactions.transaction import Transaction
from pyodbccontext.py_odbc_context import PyOdbcContext


CONNECTION_STRING = (r'DRIVER={SQL Server Native Client 11.0};'
                     r'SERVER=(localdb)\ProjectsV13;PORT=1433;'
                     r'DATABASE=DbQuicken;Trusted_Connection=yes;'
                     r'MARS_Connection=yes')
print(CONNECTION_STRING)

QIF_TYPES = {'Cash':'Asset', 'Bank':'Asset', 'CCard':'Liability',
             'Oth A':'Asset', 'Invst':'Asset', 'Oth L':'Liability',
             'Port':'Asset', '401(k)/403(b)':'Asset'}

DB = PyOdbcContext(CONNECTION_STRING)
FACTORY = QuickenFactory(DB)
Transaction.data_bindings = FACTORY.get_transaction_data_bindings(Transaction.data_binding_names)




#Transaction._data_bindings['transaction_create']



#qif = QifParser.parse(open(r'c:\users\riddi\Documents\Sort\Quicken Project\Riddins Quicken Data4.qif'))
#for acct in qif.get_accounts():
#    typ = FACTORY.account_types[QIF_TYPES[acct.account_type]]
#    #print(r'Qif Type: {} typ: {} Name: {} Description {}'.format(acct.account_type, typ.account_type_name, acct.name, acct.description))
#    acc = FACTORY.get_account(account_type = typ, name = acct.name, description = acct.description)

#for cat in qif.get_categories():
#    qif_typ = 'Expense' if cat.expense else 'Income' if cat.income else ''
#    name_vals = cat.name.split(':')
#    #print ('typ: {} Exp: {} Inc: {}'.format(qif_typ, cat.expense, cat.income))
#    typ = FACTORY.account_types[qif_typ]
    
#    if len(name_vals) > 1:
#        parent_id = FACTORY.get_account(account_type = typ, name = name_vals[0]).account_id
#    else:
#        parent_id = None
#    #print(r'Qif Type: {} Typ: {} Name: {} Description {}'.format(qif_typ, typ.account_type_name, cat.name, cat.description))
#    acc = FACTORY.get_account(account_type = typ, name = cat.name, description = cat.description, parent_id = parent_id)


#for a in qif.get_accounts():
#    b=a.get_transactions()
#    print(len(b))

params = ({'TransactionId':1, 'AccountId':1, 'DebitCredit':'c', 'Date': '1/1/2017', 'Num': None, 'Amount': 100, 'Cleared': None, 'Payee': 'someone', 'Memo': None, 'Address': None, 'Catagory': None, 'ReimbursableExpense': False}
          ,{'TransactionId':1, 'AccountId':1, 'DebitCredit':'c', 'Date': '1/1/2017', 'Num': None, 'Amount': 100, 'Cleared': None, 'Payee': 'someone', 'Memo': None, 'Address': None, 'Catagory': None, 'ReimbursableExpense': False}
          )
 #   @ int,
	#@ int, 
	#@ char(1),
	#@ date,
	#@ nvarchar(10) = NULL,
	#@ decimal(10,2),
	#@ nvarchar(1) = NULL,
	#@ nvarchar(50),
	#@ nvarchar(100) = NULL,
	#@ nvarchar(100) = NULL,
	#@ nvarchar(50) = NULL,
	#@ bit

#a = []
#a = a.append(':'.join(k, v) for k, v in params)


res = DB.transaction_detail_create(params)
print (res)
#print(type(acc))

    #acct_type = factory.account_types['Asset']
#qif.get_transactions(recursive=True)

#for x in qif.get_transactions(recursive=True):
#    for y in x:
#        print(y)

#from mssqlcontext.ms_sql_context import *
#from mssqlcontext.py_odbc_context import *
#import pyodbc

#CONNECTION_STRING = r'DRIVER={SQL Server Native Client 11.0};SERVER=(localdb)\ProjectsV13;PORT=1433;DATABASE=DbQuicken;Trusted_Connection=yes'
#_mssql.connect(server = 'iddins.database.windows.net')





#print(Asset.account_type.account_type_name)
#print(type(db.account_type_create('Asset')))
#c = db.account_type_read()
#db.get_connection().commit()
#c = db.account_type_read()
#row = c.fetchone()

#print (db.CONNECTION_STRING)


#r = db.account_type_create(account_type = 'test')

