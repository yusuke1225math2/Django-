from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        driver_path = '/Users/yusuketanbo/chromedriver'
        service = Service(executable_path=driver_path)
        cls.selenium = webdriver.Chrome(service=service)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        # ログインページを開く
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))

        # ログイン
        username_input = self.selenium.find_element(By.NAME, "login")
        username_input.send_keys('test@example.com')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('password1225')
        self.selenium.find_element(By.CLASS_NAME, 'btn').click()

        # ページタイトルの検証
        self.assertEquals('日記一覧 | Private Diary', self.selenium.title)
