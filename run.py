#!/usr/bin/env python
# coding: utf-8
from __future__ import absolute_import, unicode_literals

from ping_pong import ping_pong


def main():
    for i in xrange(1, 101):
        print 'ping_pong({}) = {}'.format(i, ping_pong(i))

if __name__ == '__main__':
    main()
