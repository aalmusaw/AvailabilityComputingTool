import json
import os

from modules.time_interval import TimeInterval
from modules.interval import Interval
from modules.intervals import Intervals
from modules.interval_intersector import IntervalIntersector
from modules.person import Person

PATH = "C:/Users/0B2721649/Desktop/scheduler/data"
OUT_PATH = "C:/Users/0B2721649/Desktop/scheduler/availability.txt"
DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def main():
    persons = []
    for file_name in os.listdir(PATH):
        if file_name.endswith(".json"):
            days = {}
            person_name = file_name[:file_name.find("_")].strip().upper()
            f = open(PATH + "/" + file_name)
            data = json.load(f)
            f.close()
            for key in DAYS:
                days[key] = parseDay(data[key])
            persons.append(Person(person_name, days))
    result = Person("Availability", computeAvailability(persons))
    f = open(OUT_PATH, "w")
    f.write(str(result))
    f.close()
    print("scheduler: computed availability successfully!")


def parseDay(times):
    intervals = []
    for time in times:
        time_parts = time.split("-")
        if len(time_parts) != 2:
            raise ValueError(
                "Each time block must be of the form 'Start - End'")
        intervals.append(TimeInterval(
            time_parts[0], time_parts[1]).toInterval())
    return Intervals(intervals)


def computeAvailability(persons):
    result = {}
    for day in DAYS:
        per_day = []
        for person in persons:
            per_day.append(person.getSchedule()[day])
        intersector = IntervalIntersector(per_day)
        result[day] = intersector.getResult()
    return result


if __name__ == "__main__":
    main()
