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
        self.satellite_ids = []
        self.satellite_errors = {}  # id : {component: timestamp}

    def file_ingest(self):
        with open(self.TELEMETRY_DATA_FILE_PATH, "r", encoding="ASCII") as file:
            while line := file.readline().rstrip():
                line_data = line.split("|")
                # print(line_data)
                time = datetime.strptime(
                    line_data[0], "%Y%m%d %H:%M:%S.%f"
                )  # ToDo: use a loop to assign to these data vals
                time = line_data[0]
                id = line_data[1]
                red_high_limit = line_data[2]
                yellow_high_limit = line_data[3]
                yellow_low_limit = line_data[4]
                red_low_limit = line_data[5]
                raw_value = line_data[6]
                component = line_data[7]

                is_error = False
                if component == "BATT":  # care if under red low
                    if raw_value < red_low_limit:
                        is_error = True
                elif component == "TSTAT":
                    if raw_value > red_high_limit:
                        is_error = True
                if is_error:
                    if id not in self.satellite_errors:
                        self.satellite_errors[id] = {component: [time]}
                    elif component not in self.satellite_errors[id]:
                        self.satellite_errors[id][component] = [time]
                    else:
                        self.satellite_errors[id][component].append(time)

            print(self.satellite_errors)

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
                pass

    def output_alert_message(self):
        pass
        """ex: {
        "satelliteId": 1234,
        "severity": "severity",
        "component": "component",
        "timestamp": "timestamp"
        }"""
