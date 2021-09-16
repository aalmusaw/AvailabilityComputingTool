#!/usr/bin/env python3

import json
import os
import sys

from .modules.time_interval import TimeInterval
from .modules.interval import Interval
from .modules.intervals import Intervals
from .modules.interval_intersector import IntervalIntersector
from .modules.person import Person

DEFAULT_INPUT_PATH = "data"
DEFAULT_OUTPUT_PATH = "availability.txt"
DAYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
CONFIG_INPUT = "input"
CONFIG_OUTPUT = "output"


def main():
    config = parseCommandlineArgs()
    data_path = getDataPath(config)
    output_path = getOutputPath(config)
    persons = []
    for file_name in os.listdir(data_path):
        if file_name.endswith(".json"):
            days = {}
            person_name = file_name[:file_name.find("_")].strip().upper()
            f = open(os.path.join(data_path, file_name))
            data = json.load(f)
            f.close()
            for key in DAYS:
                days[key] = parseDay(data[key])
            persons.append(Person(person_name, days))
    result = Person("Availability", computeAvailability(persons))
    f = open(output_path, "w")
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

def getDataPath(config):
    if CONFIG_INPUT in config:
        return config[CONFIG_INPUT]
    else:
        return DEFAULT_INPUT_PATH

def getOutputPath(config):
    if CONFIG_OUTPUT in config:
        return config[CONFIG_OUTPUT]
    else:
        return DEFAULT_OUTPUT_PATH

def parseCommandlineArgs():
    config = {}
    if len(sys.argv) == 1:
        return config
    else:
        for arg in sys.argv[1:]:
            pair = arg.split("=")
            config[pair[0].lower()] = pair[1]
        return config

if __name__ == "__main__":
    main()
