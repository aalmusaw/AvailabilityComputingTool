# AvailabilityComputingTool
This tool takes weekly availabilities from multiple people in the form of json files and returns all the common availabilities rounded to the nearest fifteen minutes.

# How to use:

- Clone the repository
- Ensure you use Python 3
- Populate the data directory with json-formatted schedules with names: `<anything>_<anything>.json`. Preferrably, do not use underscores in `<anything>`.
- Navigate to AvailabilityComputingTool.
- Run the command `python3 main.py input=<data_dir> output=<output_file_name>`
- You can omit the `input` and `output` args, but this will use the default input `AvailabilityComputingTool/data` and default output `AvailabilityComputingTool/availability.txt`.

# Sample JSON Schedule 1: 
ali_schedule.json
```
{
        "mon":["08:00 - 10:00", "16:00 - 20:00"],
        "tue":[],
        "wed":["16:00 - 20:00"],
        "thu":[],
        "fri":["16:00 - 20:00"],
        "sat":["14:00 - 21:00"],
        "sun":["14:00 - 21:00"]
}
```

# Sample JSON Schedule 2: 
mark_schedule.json
```
{
        "mon":["5:00 pm - 9:00 pm"],
        "tue":[],
        "wed":["7:00 am - 2:00 pm"],
        "thu":[],
        "fri":[],
        "sat":[],
        "sun":["11:00 am - 9:00 pm"]
}
```
