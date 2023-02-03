from satellite_temp_monitor import SatelliteTempMonitor


def main():
    stm = SatelliteTempMonitor("test_input_extended_longer.txt")
    stm.run_pipeline()


if __name__ == "__main__":
    main()
