class Interval:
    def __init__(self, *args):
        if len(args) == 2:
            self.__buildFromEndpoints(args[0], args[1])
        elif len(args) == 1:
            self.__clone(args[0])
        else:
            raise NotImplementedError()

    def __buildFromEndpoints(self, low, high):
        self.__low = low
        self.__high = high

    def __clone(self, other):
        self.__buildFromEndpoints(other.getLow(), other.getHigh())

    def intersect(self, other):
        if self.isEmpty():
            return Interval(self)
        elif other.isEmpty():
            return Interval(other)
        else:
            return Interval(max(self.__low, other.getLow()), min(self.__high, other.getHigh()))

    def isEmpty(self):
        return self.__low > self.__high

    def isInfinite(self):
        return self.__low == float("inf") and self.__high == float("inf")

    def __in__(self, other):
        if self.isEmpty() or other.isEmpty():
            raise ValueError("Cannot compare against an empty interval")
        return self.__low >= other.getLow() and self.__high <= other.getHigh()

    def getLow(self):
        return self.__low

    def getHigh(self):
        return self.__high

    def __lt__(self, other):
        if self.isEmpty() or other.isEmpty():
            raise ValueError("Cannot compare against an empty interval")
        if self.__low < other.getLow():
            return True
        elif self.__low > other.getLow():
            return False
        else:
            if self.__high < other.getHigh():
                return True
            else:
                return False

    def __eq__(self, other):
        if self.isEmpty() or other.isEmpty():
            raise ValueError("Cannot compare against an empty interval")
        return self.__low == other.getLow() and self.__high == other.getHigh()

    def __gt__(self, other):
        return not(self < other and self == other)

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

    @staticmethod
    def getEmptyInterval():
        return Interval(1.0, 0.0)

    @staticmethod
    def getInfiniteInterval():
        return Interval(float("-inf"), float("inf"))
