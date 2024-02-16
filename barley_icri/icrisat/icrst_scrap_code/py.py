from bs4 import BeautifulSoup
import json

with open('icrisat.html',"r") as file:
    data = file.read()
# print(data)
#barley = []
soup = BeautifulSoup(data,"html.parser")

table = soup.find("table",id="GridView1")
# print(table)

rows = table.find_all("tr")

for index in range(6,len(rows)):
    row = rows[index]
    columns = row.find_all("td")

    # print(columns)
    year = columns[0].text
    area = columns[1].text
    production = columns[2].text
    yield1 = columns[3].text

#    barley.append({
 #       "year": year,
  #      "area": area,
  #      "production": production,
  #      "yield": yield1
  #  })


# print(barley)

# save the temperatures in json format
# convert the list of dictionaries to json formatted string
json_structure = json.dumps(barley)

with open("icrisat.json", "w") as file:
    file.write(json_structure)

#for i in barley:
    print(i)

# df = pd.read_json("barley.json")
#print(df)
