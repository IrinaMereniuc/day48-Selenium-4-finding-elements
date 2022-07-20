# Description 

This is my coding bootcamp day 48 Selenium refresh code.
It creates and prints a dictionary from all the events listed on the https://www.python.org/events/. 

## Usage: Selenium 4 related
https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/#find-elements-utility-methods-in-python

Selenium provides the following method to locate elements in a page: find_element.
To find multiple elements (these methods will return a list): find_elements.
Example usage:
```python
from selenium.webdriver.common.by import By

driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_elements(By.XPATH, '//button')
```
The ‘By’ class is used to specify which attribute is used to locate elements on a page. These are the various ways the attributes are used to locate elements on a page:
```python
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
```