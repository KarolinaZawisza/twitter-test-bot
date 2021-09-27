from selenium_connection import SeleniumConnection
from internet_speed_test import InternetSpeedTest
from time import sleep

provider_download_speed = 150
provider_upload_speed = 180

driver = SeleniumConnection.driver
SeleniumConnection.connect_to_test(driver)

speed_test = InternetSpeedTest(driver)
InternetSpeedTest.start_test(speed_test)
sleep(60)
download_speed = InternetSpeedTest.get_download_speed(speed_test)
upload_speed = InternetSpeedTest.get_upload_speed(speed_test)
InternetSpeedTest.quit(speed_test)

if download_speed < provider_download_speed or upload_speed <provider_upload_speed:
    pass