# -*- coding: utf-8 -*-

"""
    - converts a date to decimal years
    :input
    YR = year
    MO = month
    DY = day
    HR = hour
    MN = minutes
    SC = second
    
    :output
    DecYear = decimal years
"""
def date_to_dec(YR, MO, DY, HR, MN, SC):
    DecYear = YR + (MO-1)/12 + (DY-1)/365.25 + HR/(365.25*24) 
    + MN/(365.25*24*60) + SC/(365.25*24*3600)
    return DecYear