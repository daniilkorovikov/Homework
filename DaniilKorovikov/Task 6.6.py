class Money():
    exchange_rate = {
        "EUR": 0.96,
        "BYN": 2.53,
        "USD": 1,
        "RUB": 64.25,
    }

    def __init__(self, value, currency='USD'):
        self._value = value
        self._currency = currency
        self.curr_conv = 'USD'

    def convert(self):
        return round(self._value / self.exchange_rate[self._currency], 2)

    def __str__(self):
        return f'{self._value} {self._currency}'

    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self._value + other, self._currency)
        return Money(round(self.convert() + other.convert(), 2), self.curr_conv)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self._value - other, self._currency)
        return Money(round(self.convert() - other.convert(), 2), self.curr_conv)

    __rsub__ = __sub__

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self._value * other, self._currency)
        return Money(round(self.convert() * other.convert(), 2), self.curr_conv)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Money(self._value / other, self._currency)
        return Money(round(self.convert() / other.convert(), 2), self.curr_conv)

    __rtruediv__ = __truediv__

    def __eq__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._value == other
        return self.convert() == other.convert()

    def __ne__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._value != other
        return self.convert() != other.convert()

    def __gt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._value > other
        return self.convert() > other.convert()

    def __ge__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._value >= other
        return self.convert() >= other.convert()

    def __lt__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._value < other
        return self.convert() < other.convert()

    def __le__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self._value <= other
        return self.convert() <= other.convert()


x = Money(10, "BYN")
y = Money(11)  # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8)  # result in “USD”

lst = [Money(10, "BYN"), Money(11), Money(12.01, "EUR")]
s = sum(lst)
print(s)  # result in “USD”
