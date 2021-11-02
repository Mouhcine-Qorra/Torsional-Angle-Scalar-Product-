from selenium import webdriver
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=D:\\python-ecom\\fb-cookies")
driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\NAJAT\\AppData\\Local\\chromedriver.exe")

def create():
    driver.implicitly_wait(10)
    sleep(1)
    # Upload
    driver.find_element_by_xpath(
        '//*[@id="mount_0_0_ur"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[3]/div[2]/div/div/div/div/div/div[1]').send_keys(
        "E:\\Bilden\\nada1.jpg")
    driver.implicitly_wait(10)
    sleep(1)

    # Title
    driver.find_element_by_xpath('//*[@id="jsc_c_v"]').click()
    driver.find_element_by_xpath('//*[@id="jsc_c_v"]').send_keys("بلغة جلد بثمن جد مناسب")
    driver.implicitly_wait(10)
    sleep(1)

    # Price
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[5]/div/div/label/div/div/input').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[5]/div/div/label/div/div/input').send_keys(
        "79")
    driver.implicitly_wait(10)
    sleep(1)

    # Category
    driver.find_element_by_xpath('//*[@id="mount_0_0_Mn"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[6]/div/div/div/label/div').click()
    driver.implicitly_wait(3)
    sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="mount_0_0_Mn"]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/span/div/div[12]/div/div[1]/div/div/div/div/div/span/div').click()
    driver.implicitly_wait(10)
    sleep(1)

    # State
    driver.find_element_by_xpath('//*[@id="mount_0_0_Mn"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[7]/div/div/div/label/div').click()
    driver.implicitly_wait(3)
    sleep(1)
    driver.find_element_by_xpath('//*[@id="mount_0_0_Mn"]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]').click()
    driver.implicitly_wait(10)
    sleep(1)

    # Tags
    driver.find_element_by_xpath('//*[@id="jsc_c_17"]').click()
    driver.find_element_by_xpath('//*[@id="jsc_c_17"]').send_keys("Babouche")
    driver.implicitly_wait(10)
    sleep(1)


def fb():
    driver.get("https://www.facebook.com/marketplace/create/item")

    # create post using vendre un article
    create()

fb()
