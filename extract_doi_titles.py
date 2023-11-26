import json
import argparse
import os

# Create the parser and add the arguments
parser = argparse.ArgumentParser()
parser.add_argument('json_file', help='The JSON file to parse')
parser.add_argument('-o', '--output', help='The output file (optional)')
args = parser.parse_args()

# Load the data from the JSON file
with open(args.json_file, 'r') as f:
    data = json.load(f)

# Determine the output filename
if args.output:
    output_file = args.output + '.txt'
else:
    # Use the name of the JSON file as the default output filename
    base_name = os.path.basename(args.json_file, encoding)
    output_file = os.path.splitext(base_name)[0] + '.txt'

# Open the output file
with open(output_file, 'w', encoding='utf-8') as f:
    # Iterate over each publication in the data
    for publication in data:
        # Get the DOI and the first title
        doi = publication['DOI']
        title = publication['title'][0] if publication['title'] else ''
        # Write the DOI and title to the file
        f.write(f'https://doi.org/{doi}, {title}\n')
