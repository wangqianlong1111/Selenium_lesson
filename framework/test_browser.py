from framework.Base_Page import BasePage
import unittest
class baidu(unittest.TestCase):

    def test_nos(self):
        s = BasePage(self)
        self.driver = s.open_browser(self)

if __name__ == '__main__':
    unittest.main()