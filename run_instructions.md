
# Requirements:
* Python 3.10.9
* Pip packages in requirements.txt file

# Instructions for Environment Setup:
### Depending on your environment, "python3" may need to be substituted for "python" and "pip3" for "pip"
1. Open terminal
1. Navigate to "paging-mission-control-master" (this project)
1. Create a virtual environment: `python -m venv .venv`
1. Activate virtual environment: `source .venv/bin/activate`
    1. For Windows: `.\.venv\Scripts\Activate.ps1`
1. Install project dependencies: `pip install -r requirements.txt`


# Instructions for Running This Project:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Activate virtual environment: `source .venv/bin/activate`
    1. For Windows: `.\.venv\Scripts\Activate.ps1`
1. Determine file to submit:
    1. Submit a file: `python main.py /path/filename.txt`
        * Specify path if file is not within top level project folder
    * Use -h or --help to get help menu
1. Output will display in terminal

# Instruction to Run Tests:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Activate virtual environment: `source .venv/bin/activate`
    1. For Windows: `.\.venv\Scripts\Activate.ps1`
1. Run existing tests with command `pytest`
