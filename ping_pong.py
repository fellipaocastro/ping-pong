# coding: utf-8
from __future__ import absolute_import, unicode_literals


def ping_pong(number):
    # 3 and 5
    if __check_number_is_visible_by_15(number):
        return 'ping-pong'
    elif __check_number_is_visible_by_3(number):
        return 'ping'
    elif __check_number_is_visible_by_5(number):
        return 'pong'
    else:
        return number


def __check_number_is_visible_by_15(number):
    return number % 15 == 0


def __check_number_is_visible_by_3(number):
    return number % 3 == 0


def __check_number_is_visible_by_5(number):
    return number % 5 == 0
