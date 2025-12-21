from functools import reduce
import math

numbers = [24, 36, 60]

gcd_result = reduce(math.gcd, numbers)

print(gcd_result)
