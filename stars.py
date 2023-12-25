from bs4 import BeautifulSoup
import time
import csv
from selenium import webdriver 

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/apoorvelous/Downloads/chromedriver")
browser.get(START_URL)
time.sleep(10)
headers = ["name", "distance", "mass", "radius"]
star_data = []

def scrape():

    for i in range(0, 428):
        soup = BeautifulSoup(browser.page_source, "html.parser")

        for ul_tag in soup.find_all("tr"):
            li_tags = ul_tag.find_all("td")
            temp_list = []

            for index, li_tag in enumerate(li_tags):

                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])

                else:
                    try:
                        temp_list.append(li_tag.contents[0])

                    except:
                        temp_list.append("")

            star_data.append(temp_list)
            
        browser.find_element_by_xpath('/wiki/Sirius').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)
scrape()