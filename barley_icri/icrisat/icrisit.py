from bs4 import BeautifulSoup
import json

# read the contents from file
with open("icrisit.html", "r") as file:
    data = file.read()

# create a soup
soup = BeautifulSoup(data, "html.parser")

# find the section with id = "top_gainer"
section = soup.find("section", {"id": "top_gainer"})

# find table tag from section
table = section.find("table")

# find the tbody from table
tbody = table.find("tbody")

# find all rows (tr) from tbody
rows = tbody.find_all("tr")

# create an empty list to collect all top gainers
top_gainers = []

# iterate over all rows
for row in rows:
    # find columns (td) from every row
    columns = row.find_all("td")

    # extract the required info
    company_name = columns[0].text
    high = columns[1].text
    low = columns[2].text

    # create a dictionary and append to top_gainers
    top_gainers.append({
        "company_name": company_name,
        "high": high,
        "low": low
    })

print(top_gainers)

json_data = json.dumps(top_gainers)
with open("top_gainers.json", "w") as file:
    file.write(json_data)