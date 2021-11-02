#document of login (insta-cookies)
#username password number_to_follow
from selenium import webdriver
import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=D:\\python-ecom\\insta-cookies-dija")
driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\NAJAT\\AppData\\Local\\chromedriver.exe")


def connect(username, password):
    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').click()
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').click()
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    print('Finished')

def suche(word):
    driver.get("https://www.instagram.com/explore/tags/" + word + "/")

def follow(N):
    i = 1
    while i < N:
        print(f'Start Following {i}...')
        driver.implicitly_wait(10)
        sleep(1)
        #Follow
        driver.find_element_by_xpath(f'/html/body/div[7]/div/div/div[2]/div/div/div[{i}]/div[3]/button').click()
        intg = random.randrange(start=3, stop=10)
        print(f'Waiting {intg}s')
        sleep(intg)
        i += 1

def increase():
    driver.get('https://www.instagram.com/' + username + '/saved/')
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/div[2]/div/div/div[1]/div[1]/a').click()
    print('Accessed to All post')
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[3]/article/div[1]/div/div[1]/div[1]/a').click()
    print('Accessed to the post')
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[2]/section[2]/div/div/a').click()
    follow(10)



def dija(N):
    driver.get('https://www.instagram.com/jalaba_marocain_traditionel/')
    driver.implicitly_wait(10)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a').click()
    print('Accessed to followers')
    pop_up_window = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "//div[@class='isgrP']")))

    i = 1
    x = 1
    downed = False
    while x <= N:
        driver.implicitly_wait(10)
        sleep(1)
        #Follow
        if downed:
            usr = driver.find_element_by_xpath(
                f'/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span').text
            elem = driver.find_element_by_css_selector(f'body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({i}) > div > div.Pkbci > button')
        else:
            try:
                elem = driver.find_element_by_css_selector(f'body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({i}) > div > div.qF0y9.Igw0E.rBNOH.YBx95.ybXk5._4EzTm.soMvl > button')
                usr = driver.find_element_by_xpath(
                    f'/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[2]/div[1]/div/div/span').text
            except:
                elem = driver.find_element_by_css_selector(f'body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div > li:nth-child({i}) > div > div.Pkbci > button')
                usr = driver.find_element_by_xpath(
                    f'/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div[1]/div[2]/div[1]/span').text
                print('downed')
                downed = True

        word = elem.text
        if "abonner" in word.lower():
            elem.click()
            x += 1
            print(f' ({x})\tFollowing {i}:\t{usr}...')

            intg = random.randrange(start=6, stop=23)
            sleep(intg)
        else:
            print(f' Skipping {i}:\t{usr}...')
        if i % 5 == 0:
            driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
        i += 1

username = 'mouhcine_qr'
dija(200)

