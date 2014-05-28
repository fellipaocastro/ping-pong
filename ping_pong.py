#!/usr/bin/env python
# coding: utf-8


def ping_pong(n):
    if ((n % 3 == 0) and (n % 5 == 0)):
        return 'ping-pong'
    elif n % 3 == 0:
        return 'ping'
    elif n % 5 == 0:
        return 'pong'
    else:
        return n


def main():
    for i in range(1, 101):
        print 'ping_pong(%i) = %s' % (i, ping_pong(i))

if __name__ == '__main__':
    main()
