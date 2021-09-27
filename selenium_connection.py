from selenium import webdriver


class SeleniumConnection:
    cdp = 'C:\Development\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=cdp)

    @staticmethod
    def connect_to_test(driver):
        driver.get('https://www.speedtest.net/')
        driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]').click()
