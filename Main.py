from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
import regex as re
from bs4 import BeautifulSoup
import time

eyesOn = ["PETR4", "TSLA", "VALE3", "AGRO3", "AMER3", "BBAS3"]

driver = webdriver.Chrome()
counter = 0

pyautogui.moveTo(350, 880)

for search in eyesOn:
    driver.get("https://google.com")    
    element = driver.find_element(By.ID, "APjFqb")
    element.click()
    element.send_keys(search)
    element.send_keys(Keys.ENTER)    
    driver.fullscreen_window()
    time.sleep(1)
    pyautogui.click()
    driver.fullscreen_window()
        
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    priceNow = soup.find("div", class_="YMlKec fxKbKc").text
    try:    
        changesFromYesterday = soup.find("span", class_="P2Luy Ebnabc ZYVHBb").text
    except AttributeError:
        changesFromYesterday = soup.find("span", class_="P2Luy Ez2Ioe ZYVHBb").text
    
    print(f"price: {priceNow}, [{changesFromYesterday}]")
    driver.save_screenshot("graph" + str(counter) + ".png")
    counter += 1

driver.quit()