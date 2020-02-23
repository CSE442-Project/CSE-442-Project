import time
import unittest
import os
import pages

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexTest(unittest.TestCase):

    def setUp(self):
        caps = {'browserName': os.getenv('BROWSER', 'chrome')}
        self.browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=caps
            )

    def test_h1_heading(self):
        self.browser.get('http://127.0.0.1/')
        h1s = self.browser.find_elements_by_tag_name('h1')
        self.assertEqual(len(h1s), 1)
        main_heading = h1s[0]
        self.assertEqual(main_heading.text, 'Welcome to Plow Me!')

    def test_create_client_account_button(self):
        self.browser.get('http://127.0.0.1/')
        index_page = pages.IndexPage(self.browser)
        index_page.click_create_client_account_button()
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1/accounts/create/client/')

    def test_create_contractor_account_button(self):
        self.browser.get('http://127.0.0.1/')
        index_page = pages.IndexPage(self.browser)
        index_page.click_create_contractor_account_button()
        self.assertEqual(self.browser.current_url, 'http://127.0.0.1/accounts/create/contractor/')
