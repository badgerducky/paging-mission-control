
# A monitoring and alert application that processes status telemetry data from the satellites and generates alert messages in cases of certain limit violation scenarios.
# Input: An ASCII text file containing pipe delimited records.
# Output: Display alert messages on console
""" ex: {
            "satelliteId": 1234,
            "severity": "severity",
            "component": "component",
            "timestamp": "timestamp"
        }"""




## Requirements
# Ingest status telemetry data and create alert messages for the following violation conditions:

# - If for the same satellite there are three battery voltage readings that are under the red low limit within a five minute interval.
# - If for the same satellite there are three thermostat readings that exceed the red high limit within a five minute interval.
