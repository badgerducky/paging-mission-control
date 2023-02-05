
# Requirements:
* Python 3.10.9
* Pip requirements located in requirements.txt

# Instructions to setup environment:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Create a virtual environment: 'python -m venv .venv'
1. Activate virtual environment: 'source .venv/bin/activate'
    1. For Windows: '.\.venv\Scripts/activate.bat'
1. Install project dependencies: 'pip install -r requirements.txt'


# Instructions for Running This Project:
### depending on your environment, "python3" may need to be substituted for "python" and "pip3" for "pip"
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Activate virtual environment: 'source .venv/bin/activate'
    1. For Windows: '.\.venv\Scripts/activate.bat'
1. Determine file to submit:
    1. You will need to modify main.py to select a file for submission
    1. Modify the SatelliteTempMonitor class initialization arguments to specify file or full filepath
    1. To submit a file with full windows filepath you will need to add extra "\" manually : 'SatelliteTempMonitor(C:\\\Users\\\path\\\to\\\my_file.txt)'
    1. To submit a file that is present in this project folder: 'SatelliteTempMonitor(my_file.txt)'
    1. If no file is specified the provided example from the README will be used
1. Run code: 'python main.py'
1. Output will display in terminal

# Instruction to Run Tests:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Activate virtual environment: 'source .venv/bin/activate'
    1. For Windows: '.\.venv\Scripts/activate.bat'
1. Determine file to submit
    1. To use input example from "README.md", skip indented steps
    1. Open file "test_satellite_temp_monitor.py"
    1. Modify the SatelliteTempMonitor class initialization arguments to specify file in this folder or full filepath
    1. To submit a file with full windows filepath you will need to add extra "\" manually : 'SatelliteTempMonitor(C:\\\Users\\\path\\\to\\\my_file.txt)'
    1. To submit a file that is present in this project folder: 'SatelliteTempMonitor(my_file.txt)' (line 13)
    1. Assign the expected output file to the variable: "EXPECTED_OUTPUT_FILE" for your test (line 10)
1. run test: 'python test_satellite_temp_monitor.py'
