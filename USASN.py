import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Fetch the webpage content
url = 'https://bgp.he.net/country/US'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract content from tbody table where td[2] is not empty or td[3] is not 0
# Replace "AS" with "IP-ASN,"
table = soup.find('tbody')
selected_data = []
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) > 2 and (columns[1].text.strip() or columns[2].text.strip() != '0'):
        selected_data.append(columns[0].text.strip().replace("AS", "IP-ASN,"))

# Write the scraped content to the file with timestamp at the beginning
timestamp = datetime.now().strftime('%H:%M:%S %m/%d/%Y')

with open('USASN.list', 'w') as file:
    file.write("# Generated from https://bgp.he.net/country/US at EST " + timestamp + "\n")
    for item in selected_data:
        file.write(item + '\n')
