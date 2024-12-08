import requests
import pandas as pd

years = [2018, 2019, 2020]

# The Base URL of API
base_url = "https://educationdata.urban.org/api/v1/schools/ccd/directory/"

data_records = []

for year in years:
    print(f"Fetching data for year {year}...")
    url = f"{base_url}{year}/?state=CA"
    
    while url:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Extract relevant fields
            for result in data.get('results', []):
                data_records.append({
                    'year': result.get('year'),
                    'school_id': result.get('school_id'),
                    'school_name': result.get('school_name'),
                    'total_students': result.get('enrollment'),
                    'teachers_fte': result.get('teachers_fte')
                })
            
            # Get next page URL
            url = data.get('next')
            print(f"Processed {len(data.get('results', []))} records. Next URL: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break

# Convert data to DataFrame
df = pd.DataFrame(data_records)
print(f"Total records fetched: {len(df)}")

df['school_name'] = df['school_name'].str.upper()

# Aggregating(max value as aggregation) duplicate school names in the same year
aggregated_data = (
    df.groupby(["school_name", "year"])
    .agg({
        'total_students': 'max',
        'teachers_fte': 'max'
    })
    .reset_index()
)

# Get the latest school_id for each school_name
latest_school_id = df.groupby("school_name")['school_id'].last().reset_index()

# Merge the latest school_id with the aggregated data
aggregated_data = pd.merge(aggregated_data, latest_school_id, on="school_name", how="left")

# Convert the aggregated data back into the required format
df = aggregated_data[["school_id", "school_name", "year", "total_students", "teachers_fte"]]

# Convert data into wide format
students_wide = df.pivot(index=["school_id", "school_name"], columns="year", values="total_students").add_prefix("students_")
teachers_wide = df.pivot(index=["school_id", "school_name"], columns="year", values="teachers_fte").add_prefix("teachers_")

# Merge wide tables
result = pd.concat([students_wide, teachers_wide], axis=1).reset_index()
result = result.fillna(0)


# Save the final result
result.to_csv("Final_results.csv", index=False)
print("Final aggregated data saved to 'Final_results.csv'.")
