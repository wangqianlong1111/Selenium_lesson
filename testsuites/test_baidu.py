import unittest
from framework.Base_Page import BasePage
from pageobject.BaiduPage import BaiduPage
class test_baidu(unittest.TestCase):
    '''百度首页'''

    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser(self)

    def test_baisu(self):
        '''测试百度搜索'''
        baisu = BaiduPage(self.driver)
        baisu.type_kw()
        baisu.click_su()
        baisu.quit()