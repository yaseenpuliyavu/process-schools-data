# Project Overview
This project fetches school data from the Common Core of Data (CCD) Schools API and transforms it into an easily analyzable format.

# Features
- Fetch school directory data from the Urban Institute API for multiple years(2018,2019,2020).
- Data Aggregation:
    1. Aggregate duplicate school names within the same year using max values for total_students and teachers_fte.
    2.  Retrieve the latest school_id for each school name.
- Data Transformation:
    Convert data into wide format using pandas pivot tables for better analysis.
- Generate CSV Outputs:
    Save the final aggregated data to Final_results.csv.
# Instructions
- Prerequisites
    1. Python 3.x installed.
    2. Required libraries: requests, pandas. You can install them using:

        pip install -r requirements.txt

# Setup
1. Clone the repository or download the script.
2. Ensure you are in the correct Python environment (preferably using virtual       environments):

    # For Windows
    .\venv\Scripts\activate

    # For macOS/Linux
    source venv/bin/activate

# Run the Script
Open a terminal and navigate to the directory where your script is located.

    python3 process_schools_data.py

# Script Details
## Data Collection
    - retrieves school data from the Common Core of Data (CCD) Schools API for the years (2018, 2019, 2020) and transforms it into an easily analyzable format.
    
    - API Endpoint: https://educationdata.urban.org/api/v1/schools/ccd/directory/.
## Data Processing
1. Extract Relevant Fields:
    year, school_id, school_name, total_students, and teachers_fte.
2. Normalize school_name: Convert school_name to uppercase for uniformity.
3. Aggregate Data:
    - Aggregate data by school_name and year using max aggregation function.
    - Get the latest school_id for each school_name.
    - Merge the latest school_id with aggregated data.
## Data Transformation
- Convert data into wide format using pandas.pivot_table.
- Create students_wide and teachers_wide pivot tables.
- Merge the pivot tables on school_id and school_name.
## Output
- Save the final aggregated data to Final_results.csv.

# Output Files
## Final_results.csv: 
    - Contains the final aggregated data with school_id, school_name, students_2018,students_2019,students_2020, teachers_2018,teachers_2019 and teachers_2020 columns.
# Troubleshooting
If you encounter ModuleNotFoundError, ensure that requests and pandas are installed:

    pip install requests pandas

# Performance Note
The script may take some time to execute due to API request delays and data processing steps. If performance is a concern, consider optimizing API request handling or reducing the number of requests.