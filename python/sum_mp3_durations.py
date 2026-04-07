import os
import sys
import time
from datetime import timedelta
from pathlib import Path
import librosa

# the folder to scan is passed in as an argument
folder = Path(sys.argv[1])


def sum_mp3_durations(directory):
    '''this will take a directory and sum the durations of all the 
    mp3s in it and all subdirectories'''
    # check if dir is a dir
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    # used to calculate the execution time of the function
    start = time.monotonic()
    # the sum of the mp3 durations
    total_duration = 0
    # get the info on the directory
    for root, dirs, files in os.walk(directory):
        # loop through all the files
        for name in files:
            # if the file is an mp3 add the duration to the total
            if name.endswith('.mp3'):
                file_path = Path(root, name)
                total_duration += librosa.get_duration(path=str(file_path))
    # calculate the execution duration
    end = time.monotonic()
    exec_dur = timedelta(seconds=end-start)
    print(f"execution duration: {exec_dur}")

    return round(total_duration)


sum_seconds = sum_mp3_durations(folder)

minutes, s = divmod(sum_seconds, 60)
hours, m = divmod(minutes, 60)
days, h = divmod(hours, 24)

print("The total duration of the mp3s in the scanned folder:")
print(f"{days} days, {h} hours, {m} minutes, {s} seconds")
