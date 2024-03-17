import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Fetch the webpage content
url = 'https://bgp.he.net/country/CN'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract content from tbody table where td[2] is not empty and replace "AS" with "IP-ASN,"
table = soup.find('tbody')
selected_data = []
for row in table.find_all('tr'):
    columns = row.find_all('td')
    if len(columns) > 1 and columns[1].text.strip():
        selected_data.append(columns[0].text.strip().replace("AS", "IP-ASN,"))

# Write the scraped content to the file with timestamp at the beginning
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('CNASN.list', 'w') as file:
    file.write("# Generated from https://bgp.he.net/country/CN at EST " + timestamp + "\n")
    for item in selected_data:
        file.write(item + '\n')
