from selenium_connection import SeleniumConnection
from internet_speed_test import InternetSpeedTest
from twitter_manager import TwitterManager
from time import sleep
from envr import PROVIDER_DOWNLOAD_SPEED, PROVIDER_UPLOAD_SPEED


driver = SeleniumConnection.driver
SeleniumConnection.connect_to_test(driver)

speed_test = InternetSpeedTest(driver)
speed_test.start_test()
sleep(50)
download_speed = speed_test.get_download_speed()
upload_speed = speed_test.get_upload_speed()
speed_test.quit()

twitter = TwitterManager(driver)
SeleniumConnection.connect_to_twitter(driver)
sleep(2)
twitter.log_in()

if download_speed < PROVIDER_DOWNLOAD_SPEED:
    print(f'Download speed is lower than promised! ({download_speed} )')
    tweet = twitter.complain_download(download_speed)
    twitter.tweet(tweet)
elif upload_speed < PROVIDER_UPLOAD_SPEED:
    print(f'Upload speed is lower than promised! ({upload_speed} )')
    tweet = twitter.complain_download(upload_speed)
    twitter.tweet(tweet)

