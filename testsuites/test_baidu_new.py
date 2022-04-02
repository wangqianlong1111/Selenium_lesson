import unittest
from framework.Base_Page import BasePage
from pageobject.baidu_new_page import NewPage
from pageobject.BaiduPage import BaiduPage
class test_baidu_new(unittest.TestCase):
    '''百度新闻'''

    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser(self)

    def test_new(self):
        '''搜索selenium'''
        baidu = BaiduPage(self.driver)
        baidu.click_new()
        new = NewPage(self.driver)
        new.type_ww()
        new.click_wr()
        new.quit()