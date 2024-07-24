from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.Pages.homepage import Homepage
from src.Pages.book_this_room_section import BookView
import time


def tc01():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://automationintesting.online/")
    driver.maximize_window()

    homepage = Homepage(driver)
    book_this_room_section = BookView(driver)

    homepage.click_let_me_hack_btn()
    time.sleep(2)

    element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div/div[3]/button')
    driver.execute_script("arguments[0].scrollIntoView();", element)

    homepage.click_book_this_room_btn()


tc01()
