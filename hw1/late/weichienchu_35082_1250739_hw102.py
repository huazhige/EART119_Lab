#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:17:52 2019

@author: charity
"""

import numpy as np


def PolygonSort(corners):
    n = len(corners)
    cx = float(sum(x for x, y in corners)) / n
    cy = float(sum(y for x, y in corners)) / n
    cornersWithAngles = []
    for x, y in corners:
        an = (np.arctan2(y - cy, x - cx) + 2.0 * np.pi) % (2.0 * np.pi)
        cornersWithAngles.append((x, y, an))
    cornersWithAngles.sort(key = lambda tup: tup[2])
    return map(lambda (x, y, an): (x, y), cornersWithAngles)

def PolygonArea(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area
"""
# rectangle area
corners = [(0,0), (2,0), (2,3), (0,3)]
"""
"""
# triangle area
corners = [(3,1), (2,3), (0,1)]
"""

# five-sided polygon area
corners = [(0, 0), (3, 0), (2, 10), (3, 4), (1, 5)]
corners_sorted = PolygonSort(corners)
area = PolygonArea(corners_sorted)

x = [corner[0] for corner in corners_sorted]
y = [corner[1] for corner in corners_sorted]

print(area)