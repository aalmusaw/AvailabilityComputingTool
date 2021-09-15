from .time_interval import TimeInterval

class Person:
    def __init__(self, name, schedule):
        self.__name = name
        self.__schedule = schedule

    def getSchedule(self):
        return self.__schedule

    def getName(self):
        return self.__name

    def __str__(self):
        formatter_dict = {
            "mon": "MONDAY   ",
            "tue": "TUESDAY  ",
            "wed": "WEDNESDAY",
            "thu": "THURSDAY ",
            "fri": "FRIDAY   ",
            "sat": "SATURDAY ",
            "sun": "SUNDAY   "}
        subject = "SUBJECT: " + self.__name + "\n\n"
        days = []
        for key in self.__schedule:
            day = formatter_dict[key] + ":" + \
                str([str(TimeInterval(x)) for x in self.__schedule[key].getIntervals()])
            days.append(day)
        days_str = ""
        n = len(days)
        for i in range(n):
            days_str = days_str + days[i]
            if i < n-1:
                days_str = days_str + "\n"
        return subject + days_str
