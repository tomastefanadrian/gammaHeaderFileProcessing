# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:11:34 2021

@author: Stefan
"""
from headerFileProcessing import headerFileProcessing as hfp

headerFile=hfp("header.txt")

#read data from header file
headerFile.readData()

#get the list of days (numbers relative to some reference)
#Exemple:
# -10, -5, 0, 5, 10 ....
days=headerFile.getDays()

#get reference point coordinates
referencePoint=headerFile.getReferencePoint()

#get the list of dates - list : [year, month, day, year, month, day, ..]
dates=headerFile.getDates()

#get reference date
#list [year, month, day]
referenceDay=headerFile.getReferenceDate()