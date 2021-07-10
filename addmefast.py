import secrets
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


class Bot():
    def __init__(self):
        options = Options()
        options.add_experimental_option(
            "excludeSwitches", ['enable-automation'])
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        options.add_experimental_option("prefs", prefs)
        self.driver = webdriver.Chrome(options=options)

    def action(self):
        # FB login first
        self.driver.get('https://m.facebook.com/login.php')

        email_in = self.driver.find_element_by_xpath(
            '//*[@id="m_login_email"]')
        email_in.send_keys(secrets.fb_username)

        pw_in = self.driver.find_element_by_xpath(
            '//*[@id="m_login_password"]')
        pw_in.send_keys(secrets.fb_password)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="login_password_step_element"]/button')
        login_btn.click()

        sleep(10)

        self.driver.get('https://addmefast.com')

        sleep(1)

        email_in = self.driver.find_element_by_xpath(
            '//*[@id="wrapper"]/section[2]/div/div[3]/form/div[1]/div[1]/input[1]')
        email_in.send_keys(secrets.amf_username)

        pw_in = self.driver.find_element_by_xpath(
            '//*[@id="wrapper"]/section[2]/div/div[3]/form/div[1]/div[1]/input[2]')
        pw_in.send_keys(secrets.amf_password)

        login_btn = self.driver.find_element_by_xpath(
            '//*[@id="wrapper"]/section[2]/div/div[3]/form/div[1]/div[1]/input[3]')
        login_btn.click()

        fb_likes = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div[2]/div[9]/a')
        fb_likes.click()

        sleep(4)

        count = 0
        ok = True
        while ok:
            # 100 times 1 day
            if (count == 100):
                ok = False

            sleep(1)
            try:
                btn_like = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, 'single_like_button'))
                )
                btn_like.click()
            except:
                self.driver.quit()

            base_window = self.driver.window_handles[0]
            self.driver.switch_to.window(self.driver.window_handles[1])

            btn_fb_like_page = self.driver.find_element_by_xpath(
                '//div[@aria-label="nút thích"]')
            sleep(random.randint(3, 9)) # A human behavior
            btn_fb_like_page.click()

            sleep(2)
            self.driver.close()
            self.driver.switch_to.window(base_window)

            count += 1


bot = Bot()
bot.action()
