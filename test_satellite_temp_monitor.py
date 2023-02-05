import json

from pathlib import Path
from satellite_temp_monitor import SatelliteTempMonitor


class TestSatteliteMonitor:
    def test_error_output(self):
        # Will pass if the file provided to class initializer produces the output contained in "EXPECTED_OUTPUT_FILE"

        EXPECTED_OUTPUT_FILE = Path(
            "output_files/test_output_extended_longer.txt"
        )  # Default: "output_files/test_output_provided.txt"
        stm = SatelliteTempMonitor(
            "input_files/test_input_extended_longer.txt"
        )  # Defaults to: "input_files/test_input_provided.txt"
        stm.file_ingest()
        with open(EXPECTED_OUTPUT_FILE) as f:
            expected = json.load(f)
        assert stm.satellite_error_output == expected
