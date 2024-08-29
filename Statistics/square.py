def square(x):
    return x*x

print(square(5))

do_square= lambda x: x*x
print(do_square(6))

from functools import partial
square= partial(pow, exp=2)
print(square(7))

import numpy as np
print(np.square(8))