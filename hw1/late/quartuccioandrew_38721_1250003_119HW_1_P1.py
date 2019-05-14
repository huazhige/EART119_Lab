#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:31:15 2019

    Problem 1: Computees the area of a rectangle and triangle
    given the base and the height
    
@author: andrewquartuccio
"""

#=================================================================
#                    Imports
#=================================================================

import math

#=================================================================
#                    Parameters
#=================================================================
#   Rect
b_rect = 2
c_rect = 5
#   Tri
hb_tri = 3
b_tri = 8

#=================================================================
#                    Function Definitions
#=================================================================

def area_rect_and_tri(b_rect, c_rect, hb_tri, b_tri):
    A_rect = b_rect * c_rect
    A_tri = (0.5) * hb_tri * b_tri
    return A_rect, A_tri

#=================================================================
#                    User Input & Function Calls
#=================================================================

A_rect, A_tri = area_rect_and_tri(b_rect, c_rect, hb_tri, b_tri)

print A_rect, A_tri