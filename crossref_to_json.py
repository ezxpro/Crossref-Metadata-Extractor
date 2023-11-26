import requests
import json
import time

json_name = "your_json_name.json"
# Define the base URL
issn="your_ISSN"
url = f"https://api.crossref.org/journals/{issn}/works"

# Define the headers
headers = {
    # they want you to identify yourself when you use the API. Don't be an asshole and follow the guidelines
    # they can be found here: https://github.com/CrossRef/rest-api-doc#good-manners--more-reliable-service
    "User-Agent": "YOUR_USER_AGENT (YOUR_WEBSITE_ADDRESS; YOUR_EMAIL_HERE)"
}

# Define the parameters
params = {
    "rows": 1000,  # Change this to the number of records you want per page
    "mailto": "YOUR_EMAIL_HERE",
    "select": "DOI,author,title,issue,issued",
    "sort": "published",
    "order": "asc",
    "cursor": "*"  # Start with cursor set to *
}

# Initialize a list to store all items
all_items = []

while True:
    # Send the GET request with the parameters
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    # Get the items from the response
    items = data['message']['items']

    # Check if any items were returned
    if not items:
        # No items, break the loop
        break

    # Add the items to the list and print them
    for item in items:
        print(f"DOI: {item['DOI']}, Title: {item['title'][0]}, Issue: {item.get('issue', 'N/A')}, Issued: {item['issued']['date-parts'][0]}")
        all_items.append(item)

    # Write the items to a JSON file
    with open(json_name, 'w') as f:
        json.dump(all_items, f, indent=4)

    # Update the cursor parameter for the next page
    params['cursor'] = data['message']['next-cursor']

    # Pause for 10 seconds to be polite to the server. 
    print("Waiting 10 seconds...")
    time.sleep(10)

print(f"Total items retrieved: {len(all_items)}")