# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 15:45:54 2021

@author: Amund
"""

import math
pi = math.pi
def polysum(n, s):
    """
    Parameters
    ----------
    n : Number of sides. Int or Float
        
    s : Each sides length. Int or Float

    Returns
    -------
    The polysum(Sum of area and perimeter squared)
    """
    area = (0.25*n*s**2)/(math.tan(pi/n))
    perimeter = n * s
    return round(area + perimeter**2, 4)

