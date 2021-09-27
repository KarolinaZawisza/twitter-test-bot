from selenium_connection import SeleniumConnection
from internet_speed_test import InternetSpeedTest
from twitter_manager import TwitterManager
from time import sleep

provider_download_speed = 150
provider_upload_speed = 180

driver = SeleniumConnection.driver
SeleniumConnection.connect_to_test(driver)

speed_test = InternetSpeedTest(driver)
InternetSpeedTest.start_test(speed_test)
sleep(50)
download_speed = InternetSpeedTest.get_download_speed(speed_test)
upload_speed = InternetSpeedTest.get_upload_speed(speed_test)
InternetSpeedTest.quit(speed_test)

SeleniumConnection.connect_to_twitter(driver)
twitter = TwitterManager(driver)

if download_speed < provider_download_speed:
    print(f'Download speed is lower than promised! ({download_speed} )')
    twit = TwitterManager.complain_download(twitter, download_speed)
    TwitterManager.twit(twitter, twit)
elif upload_speed < provider_upload_speed:
    print(f'Upload speed is lower than promised! ({upload_speed} )')
    twit = TwitterManager.complain_download(twitter, upload_speed)
    TwitterManager.twit(twitter, twit)

