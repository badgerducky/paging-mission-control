import os
from datetime import datetime

# Input: satellite data as an ASCII file with pipe delimited records.
# Output: satellite id, severity of incident, related component, and timestamp.
class SatelliteTempMonitor:
    def __init__(self, filename=None) -> None:

        INPUT_FILE = "test_input_provided.txt"
        if filename:
            INPUT_FILE = filename
        self.TELEMETRY_DATA_FILE_PATH = os.getcwd() + "//" + INPUT_FILE
        self.EXPECTED_FIELDS = [
            "timestamp",
            "satellite-id",
            "red-high-limit",
            "yellow-high-limit",
            "yellow-low-limit",
            "red-low-limit",
            "raw-value",
            "component",
        ]
        self.satellite_data = {}

    def file_ingest(self):
        with open(self.TELEMETRY_DATA_FILE_PATH, "r", encoding="ASCII") as file:
            while line := file.readline().rstrip():
                line_values = line.split("|")
                data_line = self.map_fields(line_values)
                id = data_line.pop("satellite-id")
                timestamp = data_line.pop("timestamp")

                if id in self.satellite_data:
                    self.satellite_data[id][timestamp] = data_line
                else:
                    self.satellite_data[id] = {timestamp: data_line}

        # print(self.satellite_data.values())

        # <timestamp>|<satellite-id>|<red-high-limit>|<yellow-high-limit>|<yellow-low-limit>|<red-low-limit>|<raw-value>|<component>

        # ToDo: read data, need to hold first timestamp for each satellite's component

    # Method to take a line of data and a list of expected field names and turn it into easy to use data
    def map_fields(self, line):
        data = {}
        for i, j in zip(self.EXPECTED_FIELDS, line):
            data[i] = j

        return data

    def find_violations(self):
        ## Requirements
        # Ingest status telemetry data and create alert messages for the following violation conditions:
        # - If for the same satellite there are three battery voltage readings that are under the red low limit within a five minute interval.
        # - If for the same satellite there are three thermostat readings that exceed the red high limit within a five minute interval.
        sat_ids = self.satellite_data.keys()
        for id in self.satellite_data.keys():
            for time in self.satellite_data[id]:
                time_val = datetime.strptime(time, "%Y%m%d %H:%M:%S.%f")
                red_high = self.satellite_data[id][time]["red-high"]
                yellow_high_limit = self.satellite_data[id][time]["yellow-high-limit"]
                yellow_low_limit = self.satellite_data[id][time]["yellow-low-limit"]
                red_low_limit = self.satellite_data[id][time]["red-low-limit"]
                raw_value = self.satellite_data[id][time]["raw-value"]
                component = self.satellite_data[id][time]["component"]

    def output_alert_message(self):
        pass
        """ex: {
        "satelliteId": 1234,
        "severity": "severity",
        "component": "component",
        "timestamp": "timestamp"
        }"""
