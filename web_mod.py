from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
import time


def create_categories_dictionary(b):
    cats = {}
    category_checkboxes = b.find_elements_by_class_name('category_checkbox')
    for checkbox in category_checkboxes:
        category_id = checkbox.get_attribute('id')
        category_name = b.find_element_by_xpath('//label[@for="{}"]'.format(category_id)).text.lower()
        cats[category_name] = category_id
    return cats


def opendns_modification(just_uncheck_all):
    options = Options()
    options.binary_location = os.environ["GOOGLE_CHROME_BIN"]
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ["CHROMEDRIVER_PATH"], options=options)
    browser.get('https://login.opendns.com/')
    browser.implicitly_wait(10)

    # LOG IN
    username_input = browser.find_element_by_id('username')
    password_input = browser.find_element_by_id('password')

    username_input.send_keys(os.environ['EMAIL'])
    password_input.send_keys(os.environ['PASSWORD'])

    password_input.submit()

    # GO TO SETTINGS
    settings_element = browser.find_element_by_xpath('//ul[@id="dashboard-nav"]//li[3]//a[1]')
    settings_element.click()

    # GO TO SPECIFIC IP
    specific_ip_element = browser.find_element_by_xpath('//span[@class="Tips1"]//a[1]')
    specific_ip_element.click()

    # CHOOSE CUSTOM CATEGORIES
    custom_categories_radio = browser.find_element_by_id('custom')
    custom_categories_radio.click()

    # UNCHECK ALL CATEGORIES CHECKBOXES
    categories = create_categories_dictionary(browser)
    for category in categories:
        category_checkbox = browser.find_element_by_id(categories[category])
        if category_checkbox.is_selected():
            category_checkbox.click()

    if not just_uncheck_all:
        # READ CATEGORIES FROM categories_to_block.txt AND CHECK CHOSE CATEGORIES
        categories_to_block = open('categories_to_block.txt', 'r').read().split(',')
        for category in categories_to_block:
            if category:
                try:
                    category_checkbox = browser.find_element_by_id(categories[category])
                    category_checkbox.click()
                except:
                    print('Warning - check with "{}" category. Check if typo.'.format(category))

    # APPLY CHANGES
    apply_input = browser.find_element_by_id('save-categories')
    apply_input.click()

    # QUIT
    browser.quit()


now = datetime.datetime.now()  # na serwerach heroku godzina przesunięta jest o 2 godziny do tyłu

while True:
    time.sleep(60)
    if now.hour == 22:
        opendns_modification(True)
    elif now.hour == 5 and now.minutes >= 50:
        opendns_modification(False)
