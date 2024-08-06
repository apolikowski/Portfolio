from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from src.Pages.homepage import Homepage
from src.Pages.book_this_room_section import BookView
from time import sleep


def tc01():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://automationintesting.online/")
    driver.maximize_window()

    homepage = Homepage(driver)
    book_this_room_section = BookView(driver)

    homepage.click_let_me_hack_btn()
    sleep(1)

    book_this_room_fnd = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div/div/div[3]/button')

    action = ActionChains(driver)
    action.move_to_element(book_this_room_fnd)
    action.perform()

    homepage.click_book_this_room_btn()
    sleep(1)


tc01()
