from selenium.webdriver.common.keys import Keys
from envr import TWITTER_LOGIN, TWITTER_PASSWORD, PROVIDER_DOWNLOAD_SPEED, PROVIDER_UPLOAD_SPEED
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

    @staticmethod
    def complain_download(download_speed: float) -> str:
        return f'Hey @FineMEDIA, you promised me {PROVIDER_DOWNLOAD_SPEED}Mb/s, but my current download speed is {download_speed}Mb/s. What the hell?'

    @staticmethod
    def complain_upload(upload_speed: float):
        return f'Hey @FineMEDIA, you promised me {PROVIDER_UPLOAD_SPEED}Mb/s, but my current download speed is {upload_speed}Mb/s. What the hell?'

    def tweet(self, tweet):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(tweet)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()