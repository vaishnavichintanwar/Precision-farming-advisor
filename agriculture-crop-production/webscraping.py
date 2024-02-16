from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time

# Set up Selenium with your web driver
# Replace with the path to your ChromeDriver executable
driver = webdriver.Chrome()
driver.get("https://www.fao.org/faostat/en/#data/QCL")

# Wait for the page to load
time.sleep(5)

# Select filters, for example, let's select "Animal Production" and "2010" as filters
element = driver.find_element(By.ID, "select-commodity")
commodity_select = Select(element)
commodity_select.select_by_value("total-meat")

element = driver.find_element(By.ID, "select-year")
year_select = Select(element)
year_select.select_by_value("2010")

# Click the "Apply" button to filter data
driver.find_element(By.ID, "apply-filter").click()

# Wait for the data to load
time.sleep(5)

# Get the page source after filters are applied
page_source = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# You can now extract data from the 'soup' object as needed
# For example, let's print the titles of all tables on the page
tables = soup.find_all('table')
for table in tables:
    headers = table.find_all('th')
    if headers:
        column_names = [header.text for header in headers]
        print(column_names)
    else:
        print("No headers found")

# Close the Selenium web driver
driver.quit()
