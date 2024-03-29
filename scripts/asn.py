import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Define the URL to scrape
url = 'https://bgp.he.net/country/CN'

# Define the header with the User-Agent for the latest macOS Safari browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'
}

# Make the request with the specified headers
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract content from tbody table where td[2] is not empty or td[3] is not 0
# Replace "AS" with "IP-ASN,"
table = soup.find('tbody')
selected_data = []
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) > 2 and (columns[1].text.strip() or columns[2].text.strip() != '0') and columns[0].text.strip().startswith("AS"):
        selected_data.append(columns[0].text.strip().replace("AS", "IP-ASN,"))

# Check if the result contains more than 300 lines, if so, write to file
if len(selected_data) > 300:
    # Write the scraped content to the file with timestamp at the beginning
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('CNASN.list', 'w') as file:
        file.write("# Generated from https://bgp.he.net/country/CN at UTC " + timestamp + "\n")
        for item in selected_data:
            file.write(item + '\n')
else:
    print("Result has less than 300 lines. Not writing to file.")
