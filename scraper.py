from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import json

ua = UserAgent()
header = {
    "User-Agent": ua.random
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
wait = WebDriverWait(chrome, 5)

year = 2023

for i in range(2024-2020):

    print("scraping for year", year)

    if year == 2023:
        gen = "programs"
    else:
        gen = "archive"

    url = f"https://summerofcode.withgoogle.com/{gen}/{year}/organizations"

    chrome.get(url)
    time.sleep(3)

    end_no = chrome.find_element(By.CLASS_NAME, "mat-paginator-range-label").get_attribute('outerHTML').split(" ")[-2]
    progress = int(end_no)
    print("total organizations:", progress)
    cycle = int(int(end_no)/50) + 1
    next_pg = chrome.find_element(By.CLASS_NAME, "mat-paginator-navigation-next")

    data = []

    for i in range(cycle):
        cards = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card")))
        
        for org in cards:
            progress -= 1
            soup = BeautifulSoup(org.get_attribute("outerHTML"), 'html.parser')

            name =  soup.find('div', class_="name").text
            info = soup.find('div', class_="short-description").text
            link = soup.find('a', class_="content").get('href')
            page_link = f"https://summerofcode.withgoogle.com{link}"

            technology = []
            topics = []
            
            chrome.execute_script("window.open('', '_blank');")
            chrome.switch_to.window(chrome.window_handles[1])
            chrome.get(page_link)
            time.sleep(3)
            page_source = chrome.page_source
            another_soup = BeautifulSoup(page_source, 'html.parser')
            tech_stack = another_soup.find('div', class_="tech__content").text
            technology.append(tech_stack)
            topic = another_soup.find('div', class_="topics__content").text
            topics.append(topic)
            chrome.close()
            chrome.switch_to.window(chrome.window_handles[0])

            schema = {
                "Name": name.strip(),
                "Tagline": info.strip(),
                "Tech-stack": technology,
                "Topics": topics,
                "Link": page_link
            }
            data.append(schema)
            print(f"{progress} left...")
        chrome.execute_script("arguments[0].click();", next_pg)
        print("page changed")
        time.sleep(3)


    with open(f"{year}.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)
    year = year-1

chrome.quit()