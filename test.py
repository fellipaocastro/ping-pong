#!/usr/bin/env python
# coding: utf-8
import unittest

from ping_pong import ping_pong


class PingPongTestCase(unittest.TestCase):
    def test_multiple_of_3_and_5_should_return_ping_pong(self):
        self.assertEqual(ping_pong(15), 'ping-pong')

    def test_multiple_of_3_should_return_ping(self):
        self.assertEqual(ping_pong(9), 'ping')

    def test_multiple_of_5_should_return_pong(self):
        self.assertEqual(ping_pong(20), 'pong')

    def test_not_multiple_of_3_nor_5_should_return_itself(self):
        self.assertEqual(ping_pong(7), 7)

if __name__ == '__main__':
    unittest.main()
