from selenium_connection import SeleniumConnection
from internet_speed_test import InternetSpeedTest
from twitter_manager import TwitterManager
from time import sleep
from envr import PROVIDER_DOWNLOAD_SPEED, PROVIDER_UPLOAD_SPEED


driver = SeleniumConnection.driver
SeleniumConnection.connect_to_test(driver)

speed_test = InternetSpeedTest(driver)
InternetSpeedTest.start_test(speed_test)
sleep(50)
download_speed = InternetSpeedTest.get_download_speed(speed_test)
upload_speed = InternetSpeedTest.get_upload_speed(speed_test)
InternetSpeedTest.quit(speed_test)

twitter = TwitterManager(driver)
SeleniumConnection.connect_to_twitter(driver)
sleep(2)
TwitterManager.log_in(twitter)

if download_speed < PROVIDER_DOWNLOAD_SPEED:
    print(f'Download speed is lower than promised! ({download_speed} )')
    tweet = TwitterManager.complain_download(download_speed)
    TwitterManager.tweet(twitter, tweet)
elif upload_speed < PROVIDER_UPLOAD_SPEED:
    print(f'Upload speed is lower than promised! ({upload_speed} )')
    tweet = TwitterManager.complain_download(upload_speed)
    TwitterManager.tweet(twitter, tweet)

