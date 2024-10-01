#!/usr/bin/env python3

import requests
import pandas as pd
from tqdm import tqdm

# Function to check the status code of a URL
def check_url_status(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        is_not_500 = status_code != 500
        return status_code, is_not_500
    except requests.exceptions.RequestException:
        # If the request fails, return None and False
        return None, False

def main(input_csv, output_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Prepare a list to store the results
    results = []

    # Progress bar setup
    for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing URLs"):
        url = row.iloc[0]
        status_code, is_not_500 = check_url_status(url)
        results.append([url, status_code, is_not_500])

    # Create a DataFrame with the results
    result_df = pd.DataFrame(results, columns=["URL", "Status Code", "Not 500"])

    # Save the results to a new CSV file
    result_df.to_csv(output_csv, index=False)

    print(f"Results saved to {output_csv}")

    # **Additional Step: Check for any False values in the "Not 500" column**
    failed_urls = result_df[result_df["Not 500"] == False]
    if not failed_urls.empty:
        print("\nSome URLs returned status code 500 or failed:")
        print(failed_urls)
    else:
        print("\No URLs return status code 500.")

if __name__ == "__main__":
    input_csv = "input_urls.csv"  # Path to the input CSV file
    output_csv = "output_results.csv"  # Path to save the output CSV file
    main(input_csv, output_csv)
