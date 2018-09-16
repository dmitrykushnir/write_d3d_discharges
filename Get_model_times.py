import numpy as np
def times(x, y, z):
    a = [x]
    for i in range(z-1):
        x += y
        a.append(x)
    b = np.c_[a]
    return b