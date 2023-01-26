from bc.tools import curry2, validator, checker

greaterThan = curry2(lambda lhs, rhs: lhs > rhs)
lessThan = curry2(lambda lhs, rhs: lhs < rhs)

v1 = validator("arg must be greater than 10", greaterThan(10))
#print(v1(0))

v2 = validator("arg must be less than 100", lessThan(100))
#print(v2(0))

withinRange = checker(v1, v2)

c = checker(v1, v2)

print(c(101))