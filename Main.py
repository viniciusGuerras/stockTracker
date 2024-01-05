from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import regex as re
from bs4 import BeautifulSoup
import time

eyesOn = ["GOGL34", "GOGL35", "PETR4", "TSLA", "VALE3", "AGRO3", "AMER3", "BBAS3"]

driver = webdriver.Chrome()
counter = 0


for search in eyesOn:
    driver.get("https://google.com")    
    element = driver.find_element(By.ID, "APjFqb")
    element.click()
    element.send_keys(search)
    element.send_keys(Keys.ENTER)    
    driver.fullscreen_window()
    time.sleep(1)
    pyautogui.moveTo(350, 880)
    pyautogui.click()
    driver.fullscreen_window()
    time.sleep(1)
    first_page_source = driver.page_source
    soup = BeautifulSoup(first_page_source, 'html.parser')

    priceNow = soup.find("div", class_="YMlKec fxKbKc").text
    try:    
        changesFromYesterday = soup.find("span", class_="P2Luy Ebnabc ZYVHBb").text
    except AttributeError:
        try:
            changesFromYesterday = soup.find("span", class_="P2Luy Ez2Ioe ZYVHBb").text
        except AttributeError:
            changesFromYesterday = soup.find("span", class_="NydbP oNKluc tnNmPe").text

    
    print(f"price: {priceNow}, [{changesFromYesterday}]")

    all_dates = driver.find_elements(By.CLASS_NAME, "VfPpkd-YVzG2b")
    all_dates[1].click()
    
    second_page_source = driver.page_source
    second_soup = BeautifulSoup(second_page_source, 'html.parser')

    try:    
        changesFrom5days = "-" + second_soup.find("span", class_="NydbP VOXKNe tnNmPe").text
    except AttributeError:
        try:
            changesFrom5days = "+" + second_soup.find("span", class_="NydbP nZQ6l tnNmPe").text
        except AttributeError:
            changesFrom5days = second_soup.find("span", class_="NydbP oNKluc tnNmPe").text
    
    print(f"from 5 days ago: {changesFrom5days}")

    driver.save_screenshot("graph" + str(counter) + ".png")
    counter += 1

driver.quit()