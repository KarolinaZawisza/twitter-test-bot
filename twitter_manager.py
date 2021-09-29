from selenium.webdriver.common.keys import Keys
from envr import TWITTER_LOGIN, TWITTER_PASSWORD
from time import sleep

class TwitterManager:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/div[4]/span/span').click()
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/a/div/span/span').click()
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(TWITTER_LOGIN + Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input').send_keys(TWITTER_PASSWORD + Keys.ENTER)

    def complain_download(self, download_speed: float):
        pass

    def complain_upload(self, upload_speed: float):
        pass

    def tweet(self, twit):
        pass