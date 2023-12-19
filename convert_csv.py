import sys
import csv
from collections import defaultdict
import argparse

parser = argparse.ArgumentParser(description='Workforce Analyzer')
parser.add_argument('--input', help='Input file path')

# use the input file path from the command line arguments
args = parser.parse_args()
csv_file_path = args.input

# Data structure to store job openings count
job_openings = {
    "Kauai County": defaultdict(int),
    "Hawaii": defaultdict(int)
}

with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        area = row['Area']
        occupation = row['Occupation']
        openings = int(row['Job Openings'])  # Assuming Job Openings is a numeric field

        # Sum up job openings per occupation for each area
        if area in job_openings:
            job_openings[area][occupation] += openings

# Preparing data for ChartJS
chartjs_data = {
    'labels': list(job_openings['Kauai County'].keys()),  # Occupation names
    'datasets': [
        {
            'label': 'Kauai County',
            'data': list(job_openings['Kauai County'].values()),  # Openings counts
            'backgroundColor': 'rgba(255, 99, 132, 0.2)',  # Example color
            'borderColor': 'rgba(255, 99, 132, 1)',  # Example color
            'borderWidth': 1
        },
        {
            'label': 'Hawaii',
            'data': list(job_openings['Hawaii'].values()),  # Openings counts
            'backgroundColor': 'rgba(54, 162, 235, 0.2)',  # Example color
            'borderColor': 'rgba(54, 162, 235, 1)',  # Example color
            'borderWidth': 1
        }
    ]
}

# This is the data in the format that ChartJS expects for a bar chart
print(chartjs_data)
