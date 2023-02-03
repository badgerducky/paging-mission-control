from satellite_temp_monitor import SatelliteTempMonitor


def main():
    # run the SatelliteTempMonitor pipeline and produce output on terminal screen

    # SatelliteTempMonitor("file.txt") will use file.txt if found in this directory
    stm = SatelliteTempMonitor()
    stm.run_pipeline()


if __name__ == "__main__":
    main()
