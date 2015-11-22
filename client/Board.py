#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: Paweł Pęksa
"""


class Board:
    """Class which is board for game"""
    def __init__(self):
        xml_board = 0

    def print_board(self):
        for i in range(0,3):
            for j in range(0,3):
                print("x",end="") # here should be put proper sign, o, x or space
                if j != 2:
                    print("|",end="")
            print("")

