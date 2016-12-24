'''need docstring'''

from .account import Account

class Liability(Account):
    '''Liability class \n\n extends Account'''

    @property
    def account_balance(self):
        raise NotImplementedError('method not yet implemented')
