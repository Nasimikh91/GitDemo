from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from testLoginData.TestLoginData import TestData
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_end_to_end(self, data_load):
        login = LoginPage(self.driver)
        login.get_username().send_keys(data_load["username"])
        login.get_password().send_keys(data_load["password"])
        sleep(2)
        login.get_checkbox().click()
        sleep(2)
        login.get_login_button().click()
        trade = TradePage(self.driver)
        trade.get_trade_button().click()
        trade.get_symbol().send_keys("TW")
        trade.get_symbol_lookup().click()
        trade.get_side().click()
        trade.get_quantity().click()
        for i in range(3):
            trade.get_quantity_input().send_keys(Keys.BACK_SPACE)
        trade.get_quantity_input().send_keys(15)
        sleep(1)
        trade.get_review_order().click()
        trade.get_send_order().click()
        trade.get_notification().click()
        trade.get_order_confirmation()
        sleep(2)
        login.get_logout_button().click()
        print("Hey hey hey")
        print("Our new changes that are going to git")
        ##############################################

    @pytest.fixture(params=TestData.test_data)
    def data_load(self, request):
        return request.param
