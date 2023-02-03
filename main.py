from satellite_temp_monitor import SatelliteTempMonitor


def main():
    # run the SatelliteTempMonitor pipeline and produce output on terminal screen

    # SatelliteTempMonitor("file.txt") will use file.txt if found in this directory
    # SatelliteTempMonitor("/home/file.txt", True) will use file.txt from path provided
    stm = SatelliteTempMonitor("test_input_extended_longer.txt")
    stm.run_pipeline()


if __name__ == "__main__":
    main()
