# coding: utf-8
"""
Created on 7.02.20
Edited 03.05.20

:author: Solovov Channel
:version: 1.0.3
"""


def of_num(number: float, percent: float) -> float:
    """
    Function calculates 'PERCENT' percents of 'NUMBER'.
    """
    return number / 100 * percent


def num_of_num(first_number: float, second_number: float) -> float:
    """
    Function calculates what percentage of the
    'FIRST_NUMBER' is the 'SECOND_NUMBER'.
    """
    return round( second_number / ( first_number / 100 ))


def add_to_num(number: float, percent: float) -> float:
    """
    Function adds to 'NUMBER' 'PERCENT' percents.\n
    Also works with negative percentages
    """
    return number + ( number / 100 * percent )


def dif_num_of_num(first_number: float, second_number: float) -> float:
    """
    Function calculates percentage difference between
    'first_number' and 'second_number'.
    """
    return ( first_number - second_number ) / (( first_number + second_number ) / 2 ) * 100
