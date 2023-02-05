import argparse
from os import listdir
from os.path import isdir, isfile, join
from pathlib import Path
from satellite_temp_monitor import SatelliteTempMonitor


def main():
    # Handle input from cmd, using "Path" so that full filepath on Windows will work
    parser = argparse.ArgumentParser(
        description="A monitoring and alert application to process data from satellites and generate alert messages for limit violations."
    )
    parser.add_argument("file", help="Specify a file to be processed.", type=Path)
    args = parser.parse_args()

    # Run the SatelliteTempMonitor pipeline and produce output on terminal screen
    if args.file:
        if not isfile(args.file):
            print("ERROR: file not found: ", args.file)
            return
        stm = SatelliteTempMonitor(args.file)
        stm.run_pipeline()


if __name__ == "__main__":
    main()
