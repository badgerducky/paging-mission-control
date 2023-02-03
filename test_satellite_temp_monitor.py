import unittest
from satellite_temp_monitor import SatelliteTempMonitor

sample_data_list = [
    "20180101 23:01:05.001|1001|101|98|25|20|99.9|TSTAT",
    "20180101 23:01:09.521|1000|17|15|9|8|7.8|BATT",
    "20180101 23:01:26.011|1001|101|98|25|20|99.8|TSTAT",
    "20180101 23:01:38.001|1000|101|98|25|20|102.9|TSTAT",
    "20180101 23:01:49.021|1000|101|98|25|20|87.9|TSTAT",
    "20180101 23:02:09.014|1001|101|98|25|20|89.3|TSTAT",
    "20180101 23:02:10.021|1001|101|98|25|20|89.4|TSTAT",
    "20180101 23:02:11.302|1000|17|15|9|8|7.7|BATT",
    "20180101 23:03:03.008|1000|101|98|25|20|102.7|TSTAT",
    "20180101 23:03:05.009|1000|101|98|25|20|101.2|TSTAT",
    "20180101 23:04:06.017|1001|101|98|25|20|89.9|TSTAT",
    "20180101 23:04:11.531|1000|17|15|9|8|7.9|BATT",
    "20180101 23:05:05.021|1001|101|98|25|20|89.9|TSTAT",
    "20180101 23:05:07.421|1001|17|15|9|8|7.9|BATT",
]
sample_BATT_errors = [
    "20180101 23:01:09.521|1000|17|15|9|8|7.8|BATT",
    "20180101 23:02:11.302|1000|17|15|9|8|7.7|BATT",
    "20180101 23:04:11.531|1000|17|15|9|8|7.9|BATT",
    "20180101 23:05:07.421|1001|17|15|9|8|7.9|BATT",
]


class TestSatteliteMonitor(unittest.TestCase):
    def test_output(self):
        stm = SatelliteTempMonitor()
        stm.file_ingest()

    def test_error_detection(self):
        stm = SatelliteTempMonitor()
        stm.file_ingest()
        timestamps = []
        for i in sample_data_list:
            val = i.split("|")
            timestamps.append(val[0])
        for i in stm.satellite_errors:
            for j in stm.satellite_errors[i]:
                for k in stm.satellite_errors[i][j]:
                    self.assertIn(
                        k, timestamps, "expected timestamp not found in errors"
                    )


if __name__ == "__main__":
    unittest.main()
