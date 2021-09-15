from .interval import Interval


class TimeInterval:
    def __init__(self, *args):
        if len(args) == 1:
            self.__intervalConstructor(args[0])
        else:
            start = args[0].lower()
            end = args[1].lower()
            if ("a" in start or "p" in start) and ("a" in end or "p" in end):
                self.__twelveHourConstructor(start, end)
            else:
                self.__twentyFourHourConstructor(start, end)

    def __intervalConstructor(self, interval):
        self.__startHour = interval.getLow()
        self.__endHour = interval.getHigh()

    def __twelveHourConstructor(self, start, end):
        self.__startHour = self.__parse12(start, True)
        self.__endHour = self.__parse12(end, False)

    def __twentyFourHourConstructor(self, start, end):
        self.__startHour = self.__parse24(start, True)
        self.__endHour = self.__parse24(end, False)

    def __parse12(self, hr, start):
        cutoff = hr.find("a")
        if cutoff == -1:
            cutoff = hr.find("p")
            if cutoff == -1:
                raise ValueError(
                    "A 12-hour system entry must be of the form NN:NN (a|A|p|P)[.](m|M)[.]")
        prefix = hr[:cutoff]
        suffix = hr[cutoff:]
        prefix_parts = prefix.split(":")
        if len(prefix_parts) != 2:
            raise ValueError(
                "The time format must be NN:NN where N is a digit")
        try:
            hour = float(prefix_parts[0])
        except(ValueError):
            raise ValueError("Hours must be numeric, got " + prefix_parts[0])
        if hour < 0 or hour > 12:
            raise ValueError(
                "Hours must be in the range 1 <= hour <= 12, got " + str(hour))
        if start:
            (minute, carry) = self.__roundStart(prefix_parts[1])
            hour = hour + carry
            if hour > 12:
                raise ValueError("Start time cannot be after 11:45 pm (23:45)")
        else:
            minute = self.__roundEnd(prefix_parts[1])
        if "a" in suffix:
            return hour + minute/60
        else:
            return 12.0 + hour + minute/60

    def __parse24(self, hr, start):
        hr_parts = hr.split(":")
        if len(hr_parts) != 2:
            raise ValueError(
                "A 24-hour system entry must be of the form XX:YY where 0 <= XX <= 23")
        try:
            hour = float(hr_parts[0])
        except(ValueError):
            raise ValueError("Hours must be numeric, got " + hr_parts[0])
        if hour < 0 or hour > 23:
            raise ValueError("Hours must be in the range 0 <= hour <= 23")
        if start:
            (minute, carry) = self.__roundStart(hr_parts[1])
            hour = hour + carry
            if hour > 24:
                raise ValueError(
                    "Start time cannot be after 11:45 pm (23:45)")
        else:
                minute = self.__roundEnd(hr_parts[1])
        return hour + minute/60

    def __roundStart(self, minute):
        try:
            result = int(minute)
        except(ValueError):
            raise ValueError("Minutes must be numeric, got " + minute)
        if result < 0 or result > 59:
            raise ValueError(
                "Minutes must be in the range 0 <= minute <= 59, got " + minute)
        if result in [0, 15, 30, 45]:
            return (result, float(0))
        elif result < 15:
            return (15, float(0))
        elif result < 30:
            return (30, float(0))
        elif result < 45:
            return (45, float(0))
        elif result < 60:
            return (0, float(1))

    def __roundEnd(self, minute):
        try:
            result = int(minute)
        except(ValueError):
            raise ValueError("Minutes must be numeric, got " + minute)
        if result < 0 or result > 59:
            raise ValueError(
                "Minutes must be in the range 0 <= x <= 59, got " + minute)
        if result in [0, 15, 30, 45]:
            return result
        elif result < 15:
            return 0
        elif result < 30:
            return 15
        elif result < 45:
            return 30
        elif result < 60:
            return 45

    def toInterval(self):
        return Interval(self.__startHour, self.__endHour)

    def __str__(self):
        s_hour = self.__realToHour(self.__startHour)
        e_hour = self.__realToHour(self.__endHour)
        return s_hour + " - " + e_hour

    def __realToHour(self, real):
        pm = False
        if real > 12:
            pm = True
            real = real - 12
        h = int(real)
        m = int(60*(real - h))
        if 0 <= h <= 9:
            str_h = "0" + str(h)
        else:
            str_h = str(h)
        if m == 0:
            str_m = "00"
        else:
            str_m = str(m)
        if pm:
            suffix = "pm"
        else:
            suffix = "am"
        return str_h + ":" + str_m + " " + suffix


#    def __minuteToReal(self, minute):
#        if minute == 0
#            return 0.0
#        elif minute == 15:
#            return 0.25
#        elif minute == 30:
#            return 0.50
#        else:
#            return 0.75
