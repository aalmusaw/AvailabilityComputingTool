from .interval import Interval


class Intervals:
    def __init__(self, intervals):
        self.__intervals = intervals

    def compress(self):
        self.__intervals = sorted(self.__intervals, reverse=True)
        if len(self.__intervals) > 0:
            if self.__intervals[0].isInfinite():
                self.__intervals = [self.__intervals[0]]
                return
        newArray = []
        for i in range(len(self.__intervals)-1):
            if self.__intervals[i] in self.__intervals[i+1]:
                self.__intervals[i] = Interval.getEmptyInterval()
        for i in range(len(self.__intervals)-1, -1, -1):
            if not self.__intervals[i].isEmpty():
                newArray.append(self.__intervals[i])
        self.__intervals = newArray

    def intersect(self, other):
        result = []
        for int_i in self.__intervals:
            for int_j in other.getIntervals():
                intersection = int_i.intersect(int_j)
                if not intersection.isEmpty():
                    result.append(intersection)
        intervals_result = Intervals(result)
        intervals_result.compress()
        return intervals_result

    def getIntervals(self):
        return list(self.__intervals)
    
    def __str__(self):
        res = '['
        for i in range(len(self.__intervals)):
            res += str(self.__intervals[i])
            if i+1 != len(self.__intervals):
                res += ', '
        res += ']'
        return res
