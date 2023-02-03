import os

from datetime import datetime
from pprint import pprint

# Input: satellite data as an ASCII file with pipe delimited records.
# Output: satellite id, severity of incident, related component, and timestamp.
class SatelliteTempMonitor:
    def __init__(self, filename=None, full_path=False) -> None:

        INPUT_FILE = "test_input_provided.txt"
        if filename:
            INPUT_FILE = filename
        self.DATA_FILE_PATH = os.getcwd() + "//" + INPUT_FILE
        if full_path:
            self.DATA_FILE_PATH = INPUT_FILE

        self.satellite_errors = {}  # id : {component: timestamp}
        self.satellite_error_output = []

    def file_ingest(self):
        # main method, this will ingest data from file and display resulting alerts
        with open(self.DATA_FILE_PATH, "r", encoding="ASCII") as file:
            while line := file.readline().rstrip():
                line_fields = line.split("|")
                time = line_fields[0]
                id = line_fields[1]
                red_high_limit = line_fields[2]
                # yellow_high_limit = line_fields[3]
                # yellow_low_limit = line_fields[4]
                red_low_limit = line_fields[5]
                raw_value = line_fields[6]
                component = line_fields[7]

                if self.is_error(component, raw_value, red_low_limit, red_high_limit):
                    if id not in self.satellite_errors:
                        self.satellite_errors[id] = {component: [time]}
                    elif component not in self.satellite_errors[id]:
                        self.satellite_errors[id][component] = [time]
                    else:
                        self.satellite_errors[id][component].append(time)
                        first = datetime.strptime(
                            self.satellite_errors[id][component][0],
                            "%Y%m%d %H:%M:%S.%f",
                        )
                        current = datetime.strptime(time, "%Y%m%d %H:%M:%S.%f")
                        time_difference = (
                            current - first
                        ).total_seconds() / 60  # convert to minutes
                        if time_difference <= 5:
                            if len(self.satellite_errors[id][component]) >= 3:
                                severity = self.find_severity(component)
                                timestamp = (
                                    datetime.isoformat(first, timespec="milliseconds")
                                    + "Z"
                                )
                                self.create_alert(
                                    id,
                                    severity,
                                    component,
                                    timestamp,
                                )
                                self.satellite_errors[id].pop(component)
            self.output_alerts()

    def is_error(self, component, raw_value, red_low_limit, red_high_limit):
        # Ingest status telemetry data and create alert messages for the following violation conditions:
        # - If for the same satellite there are three battery voltage readings that are under the red low limit within a five minute interval.
        # - If for the same satellite there are three thermostat readings that exceed the red high limit within a five minute interval.
        if component == "BATT":
            if float(raw_value) < float(red_low_limit):
                return True
        elif component == "TSTAT":
            if float(raw_value) > float(red_high_limit):
                return True
        return False

    def find_severity(self, component):
        # Determine severity based on component
        if component == "BATT":
            severity = "RED LOW"
        elif component == "TSTAT":
            severity = "RED HIGH"
        return severity

    def create_alert(self, satellite_id, severity, component, timestamp):
        # Generate alert as dict and append to list of alerts
        error_message = {}
        error_message["satelliteId"] = satellite_id
        error_message["severity"] = severity
        error_message["component"] = component
        error_message["timestamp"] = timestamp

        self.satellite_error_output.append(error_message)

    def output_alerts(self):
        # Output list of alerts
        pprint(self.satellite_error_output)
