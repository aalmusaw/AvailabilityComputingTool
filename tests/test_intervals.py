#!/usr/bin/env python3

import logging
import sys

import unittest
from ..modules.interval import Interval
from ..modules.intervals import Intervals

class TestIntervals(unittest.TestCase):
    def test_init(self):
        interval_list = [Interval(1.0, 2.0), Interval.getEmptyInterval(), Interval.getInfiniteInterval()]
        intervals = Intervals(interval_list)
        self.assertEqual(interval_list, intervals.getIntervals())

    def test_compress(self):
        # log = logging.getLogger(" test_compress: ")
        interval_list_in = [
            Interval(1.0, 2.0),
            Interval.getEmptyInterval(),
            Interval(0.5, 2.5),
            ]
        intervals = Intervals(list(interval_list_in))
        intervals.compress()
        expected = [Interval(0.5, 2.5)]
        self.assertEqual(intervals.getIntervals(), expected)

        interval_list_in.append(Interval(9.0, 10.0))
        intervals = Intervals(list(interval_list_in))
        intervals.compress()
        expected = [Interval(0.5, 2.5), Interval(9.0, 10.0)]
        self.assertEqual(intervals.getIntervals(), expected)

        interval_list_in.append(Interval.getInfiniteInterval())
        intervals = Intervals(list(interval_list_in))
        expected = [Interval.getInfiniteInterval()]
        intervals.compress()
        self.assertEqual(intervals.getIntervals(), expected)

    
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    unittest.main()