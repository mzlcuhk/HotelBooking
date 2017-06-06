# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 18:49:44 2017

@author: Ma
"""

with open("models.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)