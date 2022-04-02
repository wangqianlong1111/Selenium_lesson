from framework.Base_Page import BasePage
class NewPage(BasePage):
    ww = ['id','ww']
    wr = ['id','s_btn_wr']

    def type_ww(self):
        self.type(self.ww,'selenium')

    def click_wr(self):
        self.click(self.wr)