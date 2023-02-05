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
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f", "--file", help="Specify a file to be processed.", type=Path
    )
    group.add_argument("--folder", help="Specify a folder to be processed.", type=Path)
    args = parser.parse_args()

    # Run the SatelliteTempMonitor pipeline and produce output on terminal screen
    if args.file:
        if not isfile(args.file):
            print("ERROR: file not found: ", args.file)
            return
        stm = SatelliteTempMonitor(args.file)
        stm.run_pipeline()
    elif args.folder:  # Warning: will run ALL files in folder
        if not isdir(args.folder):
            print("ERROR: folder not found: ", args.folder)
            return
        for f in listdir(args.folder):
            print("Running file: ", f)
            if isfile(f):
                file_name = join(args.folder, f)
                stm = SatelliteTempMonitor(file_name)
                stm.run_pipeline()
            print(
                "--------------------------------------------------------------",
                end="\n\n",
            )
    else:
        print("No file/s specified, using default: 'test_input_provided.txt'")
        print(
            "--------------------------------------------------------------", end="\n\n"
        )
        stm = SatelliteTempMonitor()
        stm.run_pipeline()


if __name__ == "__main__":
    main()
