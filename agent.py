#!/usr/bin/env python

from executor import Executor

if __name__ == "__main__":
    executor = Executor(json_file_name="commands.json")
    while True:
        executor.exec_command()




# /hostnames -> fetch the unique hostnames from mongo and send in resp in json format
# /data/system?hostname=<hostname> -> Retrieve system object from mongo by searching with url param hostname
# /data/live?hostname=<hostname>&from=<from-epoch-timestamp>&to=<to-epoch-timestamp>
# -> run filter query with tag name host along with time filters to fetch all objects in that timeframe serially ordered