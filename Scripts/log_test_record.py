"""
Todo

- path for log file
- Updates the log file in artifact folder everytime test_log() is called
"""
import datetime
import os
import sys



from pathlib import Path

root_path = Path(__file__).resolve()
log_path = root_path/"artifacts"/"test_logs.log"


def write_test_logs(test_name, status, details):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] TEST: {test_name} | STATUS: {status} | DETAILS: {details}\n\n"

    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)

