
# Requirements:
* Python 3.10.9 with no external dependencies


# Instructions for Windows:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Determine file to submit:
    1. You will need to modify main.py to select a file for submission
    1. Modify the SatelliteTempMonitor class initialization arguments to specify file or full filepath
    1. If you would like to submit a file with full filepath: 'SatelliteTempMonitor(path/to/my_file.txt, True)'
    1. If you would like to submit a file that is present in this project folder: 'SatelliteTempMonitor(my_file.txt)'
    1. If no file is specified the provided example from the README will be used
1. Run code: 'python main.py'
1. Output will display in terminal

# Instruction to Run Tests:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Determine file to submit
    1. To use input example from "README.md", skip indented steps
    1. Open file "test_satellite_temp_monitor.py"
    1. Modify the SatelliteTempMonitor class initialization arguments to specify file in this folder or full filepath
    1. If you would like to submit a file that is present in this project folder: 'SatelliteTempMonitor(my_file.txt)' (line 13)
    1. If you would like to submit a file with full filepath: 'SatelliteTempMonitor(path/to/my_file.txt, True)'
    1. Modify the .txt file in "with open("test_output_provided.txt") as f:" to the expected output .txt file for your test (line 15)
1. run test: 'python test_satellite_temp_monitor.py'
