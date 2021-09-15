from .interval import Interval


class Intervals:
    def __init__(self, intervals):
        self.intervals = intervals

    def __compress(self):
        self.intervals = sorted(self.intervals)
        newArray = []
        for i in range(len(self.intervals)-1, 0, -1):
            if self.intervals[i] in self.intervals[i-1]:
                self.intervals[i] = Interval.getEmptyInterval()
        for i in range(len(self.intervals)):
            if not self.intervals[i].isEmpty():
                newArray.append(self.intervals[i])
        self.intervals = newArray

    def intersect(self, other):
        result = []
        for int_i in self.intervals:
            intersection = Interval.getInfiniteInterval()
            for int_j in other.getIntervals():
                intersection = intersection.intersect(int_i.intersect(int_j))
            if not intersection.isEmpty():
                result.append(intersection)
        intervals_result = Intervals(result)
        intervals_result.__compress()
        return intervals_result

    def getIntervals(self):
        return list(self.intervals)
