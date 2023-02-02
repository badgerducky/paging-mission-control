# Function to take a line of data and a list of expected field names and turn it into easy to use data
def map_fields(expected_fields, line):
    data = {}
    for i, j in zip(expected_fields, line):
        data[i] = j

    return data


import os

# Input: satellite data as an ASCII file with pipe delimited records.
# Output: satellite id, severity of incident, related component, and timestamp.
class satellite_temp_monitor:
    def __init__(self) -> None:
        INPUT_FILE = "test_input_provided.txt"
        TELEMETRY_DATA_FILE_PATH = os.getcwd() + "//" + INPUT_FILE
        EXPECTED_FIELDS = [
            "timestamp",
            "satellite-id",
            "red-high-limit",
            "yellow-high-limit",
            "yellow-low-limit",
            "red-low-limit",
            "raw-value",
            "component",
        ]

    def file_ingest(self):

        satellite_data = {}

        # Read in from file
        with open(self.TELEMETRY_DATA_FILE_PATH, "r", encoding="ASCII") as file:
            while line := file.readline().rstrip():
                print(line.split("|"))
                line_values = line.split("|")
                data_line = map_fields(self.expected_fields, line_values)
                id = data_line.pop("satellite-id")
                timestamp = data_line.pop("timestamp")

                if id in satellite_data:
                    satellite_data[id][timestamp] = data_line
                else:
                    satellite_data[id] = {timestamp: data_line}

        print(satellite_data.values())

        # <timestamp>|<satellite-id>|<red-high-limit>|<yellow-high-limit>|<yellow-low-limit>|<red-low-limit>|<raw-value>|<component>

        # ToDo: read data, need to hold first timestamp for each satellite's component
        #     Process

        #     Display

    def find_violations(self, satellite_data):
        ## Requirements
        # Ingest status telemetry data and create alert messages for the following violation conditions:
        # - If for the same satellite there are three battery voltage readings that are under the red low limit within a five minute interval.
        # - If for the same satellite there are three thermostat readings that exceed the red high limit within a five minute interval.
        print(satellite_data)
        pass

    def output_alert_message(self):
        pass
        """ex: {
        "satelliteId": 1234,
        "severity": "severity",
        "component": "component",
        "timestamp": "timestamp"
        }"""
