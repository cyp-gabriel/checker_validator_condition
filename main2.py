from functools import partial
from bc.tools import curry2, validator, checker, condition, curry1, _identity
from pymonad.reader import Compose

def sqr(n):
    return n * n

is_positive = lambda n: n > 0
is_not_zero = lambda n: n != 0

greaterThan = curry2(lambda lhs, rhs: lhs > rhs)
lessThan = curry2(lambda lhs, rhs: lhs < rhs)

try:
    # pre-condition(s)
    pre = condition(
        validator("arg must be positive", is_positive),
        validator("arg must not be zero", is_not_zero))

    #create_cmd = partial(pre, _identity)

    sqr_cmd = partial(pre, sqr)

    post = condition(
        validator("result must be greater than 10", greaterThan(10)),
        validator("result must be less than 100", lessThan(100)))

    c = (Compose(sqr_cmd).then(partial(post, _identity)))

    print(c(3))
except Exception as ex:
    print(ex)