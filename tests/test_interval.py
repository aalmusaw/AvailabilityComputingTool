#!/usr/bin/env python3

import unittest
from ..modules.interval import Interval

class TestInterval(unittest.TestCase):
    def test_init(self):
        interval = Interval(1.0, 2.0)
        self.assertEqual(1.0, interval.getLow())
        self.assertEqual(2.0, interval.getHigh())
        interval2 = Interval(interval)
        self.assertEqual(1.0, interval2.getLow())
        self.assertEqual(2.0, interval2.getHigh())

    def test_isEmpty(self):
        interval = Interval(1.0, 2.0)
        self.assertFalse(interval.isEmpty())
        interval = Interval(1.0, 0.0)
        self.assertTrue(interval.isEmpty())

    def test_intersect(self):
        empty = Interval.getEmptyInterval()
        other = Interval(2.0, 3.0)
        self.assertEqual(empty, empty.intersect(other))
        self.assertEqual(empty, other.intersect(empty))
        infinite = Interval.getInfiniteInterval()
        self.assertEqual(other, infinite.intersect(other))
        self.assertEqual(other, other.intersect(infinite))
        x = Interval(2.0, 3.0)
        y = Interval(1.0, 3.0)
        z = Interval(4.0, 5.0)
        w = Interval(2.5, 4.0)
        self.assertEqual(x, x.intersect(y))
        self.assertTrue(x.intersect(z).isEmpty())
        self.assertEqual(x.intersect(w), Interval(2.5, 3.0))

    def test_in(self):
        x = Interval(2.0, 3.0)
        y = Interval(1.0, 3.0)
        z = Interval(2.0, 2.5)
        self.assertTrue(z in x)
        self.assertFalse(y in x)
    
if __name__ == '__main__':
    unittest.main()