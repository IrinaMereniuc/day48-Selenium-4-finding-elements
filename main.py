from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "c:/Users/irina.mereniuc/Development/chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
URL = "https://www.python.org/events/"
driver.get(URL)

event_times = driver.find_elements(By.CSS_SELECTOR, 'ul.menu time')
event_names = driver.find_elements(By.CSS_SELECTOR, "h3 a")

events = {}

for n in range(0, len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)