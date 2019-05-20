# -*- coding: utf-8 -*-
#python 2.7
"""
Function that takes in year, month, days, minutes, hours, and seconds and converts it into a 
decimal year, i.e year 2000.5 instead of June 2000 for example.
"""

def dec_year(yr, mo, dy, hr, mn, sec):
    return(yr + (mo - 1) / 12. + (dy - 1) / 365.25 + hr / (365.25 * 24) + 
           mn / (365.25 * 24 * 60) + sec / (365.25 * 24 * 3600))