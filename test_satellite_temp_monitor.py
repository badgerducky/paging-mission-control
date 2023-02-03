import unittest
import json
from satellite_temp_monitor import SatelliteTempMonitor


class TestSatteliteMonitor(unittest.TestCase):
    def test_error_output(self):
        # Will pass if the file provided to class initializer produces the output contained in "EXPECTED_OUTPUT_FILE"

        EXPECTED_OUTPUT_FILE = (
            "test_output_provided.txt"  # Default: "test_output_provided.txt"
        )
        stm = SatelliteTempMonitor()  # Defaults to: "test_input_provided.txt"
        stm.file_ingest()
        with open(EXPECTED_OUTPUT_FILE) as f:
            expected = json.load(f)
        self.assertEqual(stm.satellite_error_output, expected)


if __name__ == "__main__":
    unittest.main()
