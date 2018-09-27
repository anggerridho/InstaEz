from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstaEz:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('/home/s1gnific4nt/InstaEz/chromedriver')

    def menutupBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        login_btn = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_btn.click()
        time.sleep(3)
        username_element = driver.find_element_by_xpath("//input[@name='username']")
        username_element.clear()
        username_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(3)

    def liker(self,hastag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+ hastag +"/")
        time.sleep(3)

        #pengumpulan foto
        pic_hrefs = []
        for i in range(1,7):
            try:
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(3)
                #tag a
                hrefs = driver.find_elements_by_tag_name('a')
                #mencari href yang dapat digunakan
                pic_hrefs = [elemen.get_attribute('href') for elemen in hrefs]
                pic_hrefs =  [href for href in pic_hrefs if hastag in href]
                #list foto
                [pic_hrefs.append(href) for href in hrefs if href not in pic_hrefs]
                #print(hastag + ' photos: ' + str(len(pic_hrefs)))
            except Exception:
                continue

        #buat like foto
        photo = len(pic_hrefs)
        for picture_source in pic_hrefs:
            driver.get(picture_source)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            try:
                like_btn = lambda: driver.find_element_by_xpath('/html/body/span/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()
                like_btn().click()
                for detik in reversed(range(0, random.randint(18, 28))):
                    print("#" + hastag + ': unique photos left: ' + str(photo) + " | Sleeping " + str(detik))
            except Exception as ex:
                time.sleep(3)
            photo -=1


username = "USERNAME" #masukan username kamu
password = "PASSWORD" #masukan password kamu

testingBot = InstaEz(username,password)
testingBot.login()

hastag = ['amazing','like','best','code','programming','networking','followme', 'follow','muslim', 'instagood', 'instagood', 'followme','linux'] #hashtag bisa diedit/ditambahkan sesuai selera

while True:
    try:
        #randoming hastag dari list
        tags = random.choice(hastag)
        testingBot.liker(tags)
    except Exception:
        testingBot.menutupBrowser()
        time.sleep(30)
        testingBot = InstaEz(username, password)
        testingBot.login()