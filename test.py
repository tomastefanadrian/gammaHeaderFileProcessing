# -*- coding: utf-8 -*-
"""
Created on Tue May  4 16:11:34 2021

@author: Stefan
"""
from headerFileProcessing import headerFileProcessing as hfp

headerFile=hfp("header.txt")

aa=headerFile.readData()
dd=headerFile.getDays()
qq=headerFile.getReferencePoint()