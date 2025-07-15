import numpy as np


def FastInvSqrtSum(x, y, z=1):
    """
    This code compute inverse square root of a sum of 3 numbers like so

    .. math::

       v = \\frac{1}{\sqrt{x^2+y^2+z^2}}

    Parameters
    ==========
    x : int or float
        The first number
    y : int or float
        The second number
    z : int or float, optional, default: 1
        The kast number

    Returns
    =======
    v : float
    """

    return 1/np.sqrt(x**2+y**2+z**2)
