
# Requirements:
* Python 3.10.9
* Pip packages in requirements.txt file

# Instructions for Environment Setup:
### Depending on your environment, "python3" may need to be substituted for "python" and "pip3" for "pip"
1. Open terminal
1. Navigate to "paging-mission-control-master" (this project)
1. Create a virtual environment: 'python -m venv .venv'
1. Activate virtual environment: 'source .venv/bin/activate'
    1. For Windows: '.\\.venv\Scripts\activate.bat'
1. Install project dependencies: 'pip install -r requirements.txt'


# Instructions for Running This Project:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Activate virtual environment: 'source .venv/bin/activate'
    1. For Windows: '.\\.venv\Scripts\activate.bat'
1. Determine file or directory to submit:
    1. To submit a file specify -f: 'python main.py -f /path/filename.txt'
        * Specify path if file is not within top level project folder
    1. Submit a folder with --folder flag: 'python main.py --folder /path/folder'
        * All files in specified folder will be run, but not subfolders
    1. Use submission from README.md with: 'python main.py'
    * Use -h or --help to get help menu
1. Output will display in terminal

# Instruction to Run Tests:
1. Open terminal
1. Navigate to "paging-mission-control-master"
1. Activate virtual environment: 'source .venv/bin/activate'
    1. For Windows: '.\\.venv\Scripts\activate.bat'
1. Run existing tests with command 'pytest'
