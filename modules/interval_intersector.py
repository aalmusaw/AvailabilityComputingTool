from .interval import Interval
from .intervals import Intervals


class IntervalIntersector:
    def __init__(self, intervals_list):
        self.__intervals_list = intervals_list

    def getResult(self):
        result = Intervals([Interval.getInfiniteInterval()])
        for intervals in self.__intervals_list:
            result = result.intersect(intervals)
        return result
