import time
import eel
import TextToSpeech
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

course_link = ""

@eel.expose
def getUdemyCourse(course_name, driver):
    try:
        frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
        driver.switch_to.frame(frame)
        isCaptcha = driver.find_element_by_class_name('rc-anchor-logo-text')
        if isCaptcha.text == 'reCAPTCHA':
            print("-> ", isCaptcha.text)
            try:
                wait = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-checked")))
                print("pass that")
            except TimeoutException:
                print("inside captcha exception ")
                pass

            if wait:
                print("inside that")
                driver.switch_to.default_content()
            time.sleep(3)
    except NoSuchElementException:
        pass

    search_bar = driver.find_element_by_xpath(
        '//*[@placeholder="Search for anything"]')  # driver.find_element_by_id("header-search-field")//*[@id="header-desktop-search-bar"]
    search_bar.send_keys(course_name)

    try:
        search_bar_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '(//*[@placeholder="Search for anything"]//following::button)')))
        # old => //*[@placeholder="Search for anything"]//following::button
        # new => (//*[@placeholder="Search for anything"]//following::button)[3]
        search_bar_button.click()
        print("1. clicked")
    except (NoSuchElementException, TimeoutException) as e:
        print("+++++++++>", e)
        pass

    try:
        search_bar_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
            (By.XPATH, '(//*[@placeholder="Search for anything"]//following::button[3])')))
        # old => //*[@placeholder="Search for anything"]//following::button
        # new => (//*[@placeholder="Search for anything"]//following::button)[3]
        search_bar_button.click()
        print("2 .clicked")
    except (NoSuchElementException, TimeoutException) as e:
        print("+++++++++>")
        pass

    # try:
    #     search_bar_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    #         (By.XPATH, '(//*[@placeholder="Search for anything"]/following-sibling::button)[2]')))
    #     # old => //*[@placeholder="Search for anything"]/following-sibling::button
    #     # new => (//*[@placeholder="Search for anything"]/following-sibling::button)[2]
    #     print("3. clicked")
    #     search_bar_button.click()
    #
    #     print("3. clicked")
    # except TimeoutException as e:
    #     print("Exception------", e.msg)
    #     pass

    try:
        frame = driver.find_element_by_xpath('//iframe[contains(@src, "recaptcha")]')
        driver.switch_to.frame(frame)
        isCaptcha = driver.find_element_by_class_name('rc-anchor-logo-text')
        if isCaptcha.text == 'reCAPTCHA':
            print("-> ", isCaptcha.text)
            try:
                wait = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.CLASS_NAME, "recaptcha-checkbox-checked")))
                print("pass that")
            except TimeoutException:
                print("inside captcha exception ")
                pass

            if wait:
                print("inside that")
                driver.switch_to.default_content()
            time.sleep(3)
    except NoSuchElementException:
        pass

    time.sleep(3)

    global course_link
    links = []
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount==lenOfPage:
            match=True
    for i in range(0, 7):
        try:
            # bestseller = driver.find_elements_by_class_name('course-list--container--3zXPS')
            # print(bestseller[i])
            # print(bestseller[i].get_attribute(''))
            bs = driver.find_elements_by_xpath(
                "//*[contains(text(), 'Bestseller')]/ancestor::a")
            # //*[*//span[@class='badge-text' and contains(text(), 'Bestseller')]]/ancestor::a
            print(bs[i].get_attribute('href'))
            links.append(bs[i].get_attribute('href'))
        except (NoSuchElementException, IndexError):
            print("lol")
            pass

    for link in set(links):
        course_link += link + " \n"

    with open('CourseLinks.txt', mode='w') as file:
        file.write(course_link)
    eel.printAgentDom("Your Best course links are stored in CourseLinks.txt")
    TextToSpeech.say("Your Best course links are stored in CourseLinks.txt")

@eel.expose
def getYoutubeCourse(course_name, driver):
    time.sleep(2)

    search_bar = driver.find_element_by_xpath('//input[@id="search"]')  # driver.find_element_by_id("header-search-field")
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="search"]'))).send_keys(course_name)
    search_bar.send_keys(course_name)

    search_bar_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="search-icon-legacy"]')))
    search_bar_button.click()

    time.sleep(2)
    global course_link

    try:
        for i in range(0, 2):
            parentElement = driver.find_elements_by_tag_name('ytd-playlist-renderer')
            elementList = parentElement[i].find_element_by_tag_name("a")
            print(elementList.get_attribute('href'))
            course_link += (elementList.get_attribute('href') + " \n")
    except IndexError as e:
        print(e)
        pass
    try:
        for i in range(0, 3):
            parentElement = driver.find_elements_by_tag_name('ytd-video-renderer')
            elementList = parentElement[i].find_element_by_tag_name("a")
            print(elementList.get_attribute('href'))
            course_link += (elementList.get_attribute('href') + " \n")
    except IndexError as e:
        print(e)
        pass
    course_link += "\n"

@eel.expose
def getUdacityCourse(course_name):
    option = webdriver.ChromeOptions()
    option.add_argument("window-size=1200x600");
    # driver = webdriver.Chrome('/usr/bin/chromedriver', options=option)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.get('https://www.udacity.com/courses/all')
    eel.printAgentDom("please wait, I am Working on the web, to scrap your best result")
    TextToSpeech.say("please wait, I am Working on the web, to scrap your best result")
    time.sleep(2)

    search_bar = driver.find_element_by_xpath(
        '//*[@id="catalog-search-input"]')  # driver.find_element_by_id("header-search-field")
    # //*[@id="catalog-search-input"]
    search_bar.send_keys(course_name)
    time.sleep(3)
    global course_link
    a_tag = driver.find_elements_by_class_name('card__top')
    for i in range(5):
        try:
            url = a_tag[i].get_attribute('href')
            if url is not None:
                print(url)
                course_link += (url + " \n")
        except (NoSuchElementException, IndexError):
            pass
    course_link += "\n"
    time.sleep(2)
    actions = ActionChains(driver)
    about = driver.find_element_by_link_text(
        'Sign In')
    actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()

    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://www.youtube.com")
    getYoutubeCourse(course_name, driver)
    time.sleep(2)
    actions = ActionChains(driver)
    about = driver.find_element_by_link_text('Home')
    actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()

    driver.switch_to.window(driver.window_handles[-1])
    driver.get("https://www.udemy.com/")
    getUdemyCourse(course_name, driver)

    driver.quit()

# getUdacityCourse('web development')
