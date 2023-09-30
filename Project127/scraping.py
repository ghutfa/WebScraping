from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import csv
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("")
scraped_data = []
def web_scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    table = soup.find("table", attrs={"class": "wikitable"})
    table_body = table.find("tbody")
    table_row = table_body.find("tr")
    for td in table_row:
        table_column = td.find_all("td")
        temp_list = []
        for a in table_column:
            data = a.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)
web_scrape()

headers = ["Star Name", "Distance", "Mass", "Radius", "Luminosity"]
with open("class127output.csv", "w") as data:
    writer = csv.writer(data)
    writer.writerow(headers)
    writer.writerows(scraped_data)

         
            
            

    
            
    
    
