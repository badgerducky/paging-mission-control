from satellite_temp_monitor import SatelliteTempMonitor


def main():
    stm = SatelliteTempMonitor()
    stm.file_ingest()


if __name__ == "__main__":
    main()
