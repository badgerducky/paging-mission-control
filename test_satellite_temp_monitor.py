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


class TestSatteliteMonitor(unittest.TestCase):
    def test_ingest(self):
        stm = SatelliteTempMonitor()
        stm.file_ingest()
        # for i in sample_data_list:
        #     val = i.split("|")
        #     # Check that all satellite id's have made it into data dictionary
        #     self.assertIn(
        #         val[1],
        #         stm.satellite_data.keys(),
        #         "all satellite id's should be reflected as keys",
        #     )
        # Check that all timestamps have made it into data dictionary
        # self.assertIn(val[0], stm.satellite_data[val[1]].keys())

    # def test_message_gen(self):
    #     stm = SatelliteTempMonitor()
    #     stm.file_ingest()
    #     stm.find_violations()


if __name__ == "__main__":
    unittest.main()
