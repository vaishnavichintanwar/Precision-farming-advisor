from bs4 import BeautifulSoup
import json

with open('icrisat_101-200.html', "r") as file:
    data = file.read()
# print(data)
crops = []
soup = BeautifulSoup(data,"html.parser")
#
table = soup.find("table",id="DataTables_Table_0")
# print(table)

rows = table.find_all("tr")

for index in range(1,len(rows)):
    row = rows[index]
    columns = row.find_all("td")
    # print(columns)
    dist_code = columns[0].text
    year = columns[1].text
    state_code = columns[2].text
    state_name = columns[3].text
    dist_name = columns[4].text

    rice_area = columns[5].text
    rice_prod = columns[6].text
    rice_yield = columns[7].text

    wheat_area = columns[8].text
    wheat_prod = columns[9].text
    wheat_yield = columns[10].text


    kharif_sorghum_area = columns[11].text
    kharif_sorghum_prod = columns[12].text
    kharif_sorghum_yield = columns[13].text

    rabi_sorghum_area = columns[14].text
    rabi_sorghum_prod = columns[15].text
    rabi_sorghum_yield = columns[16].text

    sorghum_area = columns[17].text
    sorghum_prod = columns[18].text
    sorghum_yield = columns[19].text

    pearl_millet_area = columns[20].text
    pearl_millet_prod = columns[21].text
    pearl_millet_yield = columns[22].text

    maize_area = columns[23].text
    maize_prod = columns[24].text
    maize_yield = columns[25].text

    finger_millet_area = columns[26].text
    finger_millet_prod = columns[27].text
    finger_millet_yield = columns[28].text

    barley_area = columns[29].text
    barley_prod = columns[30].text
    barley_yield = columns[31].text

    chickpea_area = columns[32].text
    chickpea_prod = columns[33].text
    chickpea_yield = columns[34].text

    pigeonpea_area = columns[35].text
    pigeonpea_prod = columns[36].text
    pigeonpea_yield = columns[37].text

    minor_pulses_area = columns[38].text
    minor_pulses_prod = columns[39].text
    minor_pulses_yield = columns[40].text

    groundnut_area = columns[41].text
    groundnut_prod = columns[42].text
    groundnut_yield = columns[43].text

    sesamum_area = columns[44].text
    sesamum_prod = columns[45].text
    sesamum_yield = columns[46].text

    rapeseed_area = columns[47].text
    rapeseed_prod = columns[48].text
    rapeseed_yield = columns[49].text

    safflower_area = columns[50].text
    safflower_prod = columns[51].text
    safflower_yield = columns[52].text

    castor_area = columns[53].text
    castor_prod = columns[54].text
    castor_yield = columns[55].text

    linseed_area = columns[56].text
    linseed_prod = columns[57].text
    linseed_yield = columns[58].text

    sunflower_area = columns[59].text
    sunflower_prod = columns[60].text
    sunflower_yield = columns[61].text

    soyabean_area = columns[62].text
    soyabean_prod = columns[63].text
    soyabean_yield = columns[64].text

    oilseeds_area = columns[65].text
    oilseeds_prod = columns[66].text
    oilseeds_yield = columns[67].text

    sugarcane_area = columns[68].text
    sugarcane_prod = columns[69].text
    sugarcane_yield = columns[70].text

    cotton_area = columns[71].text
    cotton_prod = columns[72].text
    cotton_yield = columns[73].text





    crops.append({
        "dist_code": dist_code,
        "year": year,
        "state": state_code,
        "state_name": state_name,
        "dist_name": dist_name,

        "rice_area": rice_area,
        "rice_prod": rice_prod,
        "rice_yield": rice_yield,

        "wheat_area": wheat_area,
        "wheat_prod": wheat_prod,
        "wheat_yield": wheat_yield,

        "kharif_sorghum_area": kharif_sorghum_area,
        "kharif_sorghum_prod": kharif_sorghum_prod,
        "kharif_sorghum_yield": kharif_sorghum_yield,

        "rabi_sorghum_area": rabi_sorghum_area,
        "rabi_sorghum_prod": rabi_sorghum_prod,
        "rabi_sorghum_yield": rabi_sorghum_yield,

        "sorghum_area": sorghum_area,
        "sorghum_prod": sorghum_prod ,
        "sorghum_yield" : sorghum_yield,

        "pearl_millet_area": pearl_millet_area,
        "pearl_millet_prod": pearl_millet_prod,
        "pearl_millet_yield": pearl_millet_yield,

        "maize_area": maize_area,
        "maize_prod": maize_prod,
        "maize_yield": maize_yield,

        "finger_millet_area": finger_millet_area,
        "finger_millet_prod": finger_millet_prod,
        "finger_millet_yield": finger_millet_yield,

        "barley_area": barley_area,
        "barley_prod": barley_prod,
        "barley_yield": barley_yield,

        "chickpea_area": chickpea_area,
        "chickpea_prod": chickpea_prod,
        "chickpea_yield": chickpea_yield,

        "pigeonpea_area": pigeonpea_area,
        "pigeonpea_prod": pigeonpea_prod,
        "pigeonpea_yield": pigeonpea_yield,

        "minor_pulses_area": minor_pulses_area,
        "minor_pulses_prod": minor_pulses_prod,
        "minor_pulses_yield": minor_pulses_yield,

        "groundnut_area": groundnut_area,
        "groundnut_prod": groundnut_prod,
        "groundnut_yield": groundnut_yield,

        "sesamum_area": sesamum_area,
        "sesamum_prod": sesamum_prod,
        "sesamum_yield": sesamum_yield,

        "rapeseed_area": rapeseed_area,
        "rapeseed_prod": rapeseed_prod,
        "rapeseed_yield": rapeseed_yield,

        "safflower_area": safflower_area,
        "safflower_prod": safflower_prod,
        "safflower_yield": safflower_yield,

        "castor_area": castor_area,
        "castor_prod": castor_prod,
        "castor_yield": castor_yield,

        "linseed_area": linseed_area,
        "linseed_prod": linseed_prod,
        "linseed_yield": linseed_yield,

        "sunflower_area": sunflower_area,
        "sunflower_prod": sunflower_prod,
        "sunflower_yield": sunflower_yield,

        "soyabean_area": soyabean_area,
        "soyabean_prod": soyabean_prod,
        "soyabean_yield": soyabean_yield,

        "oilseeds_area": oilseeds_area,
        "oilseeds_prod": oilseeds_prod,
        "oilseeds_yield": oilseeds_yield,

        "sugarcane_area": sugarcane_area,
        "sugarcane_prod": sugarcane_prod,
        "sugarcane_yield": sugarcane_yield,

        "cotton_area": cotton_area,
        "cotton_prod": cotton_prod,
        "cotton_yield": cotton_yield


    })

print(crops)

# save the temperatures in json format
# convert the list of dictionaries to json formatted string
json_structure = json.dumps(crops)

with open("icrisat_101-200.json", "w") as file:
    file.write(json_structure)

for i in crops:
    print(i)




