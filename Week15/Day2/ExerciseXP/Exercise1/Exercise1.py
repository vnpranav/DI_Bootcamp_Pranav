class Currency:
    def __init__(self,currency,amount):
        self.currency = currency
        self.amount = amount

    def __int__(self):
        return(self.currency)

    def __repr__(self):
        if self.amount > 1:
            return(f'{self.amount} {self.currency}s')
        else:
            return(f'{self.amount} {self.currency}')

    def __str__(self):
        if self.amount > 1:
            return(f'{self.amount} {self.currency}s')
        else:
            return(f'{self.amount} {self.currency}')

    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount + other.amount
        else:
            raise TypeError()

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1 + c3)
