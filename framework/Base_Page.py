from Logs.log import log1
from selenium.common.exceptions import NoSuchElementException
import getcwd
import os
import time
import configparser
from selenium import webdriver

path = getcwd.get_cwd()
config_path = os.path.join(path, 'Config/config.ini')

class BasePage():
    '''测试基类'''
    def __init__(self,driver):
        self.driver = driver


    def get_img(self):
        '''截图'''
        path = os.path.join(getcwd.get_cwd(),'screenshots/')#拼接截图保存路径
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))#按格式获取当前时间
        screen_name = path + rq + '.png'#拼接截图文件名
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log1.info("截图保存成功")
        except BaseException:
            log1.error("截图失败",exc_info = 1)

    def find_element(self,selector):
        '''定位元素'''
        by = selector[0]
        value = selector[1]
        element = None
        if by =='id' or by =='name' or by == 'class' or by == 'tag' or by =='link' or by =='plink' or by =='css' or by == 'xpath':
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    log1.error('没有找到元素')
                log1.info('元素定位成功。定位方式：%s，使用的值%s：' % (by,value))
                return element
            except NoSuchElementException:
                log1.error("报错信息：",exc_info = 1)
                self.get_img()#调用截图
        else:
            log1.error('输入的元素定位方式错误')


    def type(self,selector,value):
        '''输入内容'''
        element=self.find_element(selector)
        element.clear()
        log1.info('清空输入内容')
        try:
            element.send_keys(value)
            log1.info('输入的内容：%s' % value)
        except BaseException:
            log1.error('内容输入报错',exc_info = 1)
            self.get_img()


    def click(self,selector):
        '''点击元素'''
        element = self.find_element(selector)
        try:
            element.click()
            log1.info('点击元素成功')
        except BaseException:
            log1.error('点击元素报错',exc_info = 1)
            self.get_img()


    def sleep(self,secondes):
        '''强制暂停'''
        time.sleep(secondes)
        log1.info('暂停%d秒' % secondes)


    def get_title(self):
        '''获取title'''
        title = self.driver.title
        log1.info('当前窗口的title是:%s' % title)
        return  title

    def quit(self):
        self.driver.quit()
        log1.info('关闭浏览器')


    def config_get(self,key,section=None):
        '''读取配置文件字段的值并返回'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        switch = config.get('environment', 'switch')
        if section==None and switch == str(0):
            section = 'test'
        elif section==None and switch == str(1):
            section = 'prod'
        config_get = config.get(section,key)
        return  config_get


    def config_write(self,key = None,value = None,section = None):
        '''往配置文件写入键值'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        switch = config.get('environment', 'switch')
        if section == None and switch == str(0):
            section = 'test'
        elif section == None and switch == str(1):
            section = 'prod'
        if key is not None and value is not None:
            config.set(section,key,value)
            log1.info('在section:%s下写入%s=%s' %(section,key,value))
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)
        else:
            config.add_section(section)
            log1.info('新增section：%s' % section)
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)


    def config_delete(self,key = None,section = None):
        '''删除配置文件字段'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        switch = config.get('environment', 'switch')
        if section == None and switch == str(0):
            section = 'test'
        elif section == None and switch == str(1):
            section = 'prod'
        if key is not None :
            config.remove_option(section,key)
            log1.info('删除section:%s下key为：%s的记录' % (section,key))
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)
        else:
            config.remove_section(section)
            log1.info('删除section:%s' % section)
            with open(config_path,'w',encoding='utf-8')as f :
                config.write(f)


    def open_browser(self,driver):
        browser = self.config_get('browser','environment')
        log1.info('读取浏览器配置')
        url = self.config_get('url')
        log1.info('读取url：%s' % url)
        try:
            if browser == str(0) :
                driver = webdriver.Chrome()
                log1.info('打开的浏览器为chrome')
            elif browser == str(1) :
                driver = webdriver.Firefox()
                log1.info('打开的浏览器为chrome')
            driver.get(url)
            driver.maximize_window()
            log1.info('浏览器最大化')
            driver.implicitly_wait(10)
            log1.info('设置静态等待时间10秒')
            return driver
        except BaseException:
            log1.error('浏览器打开报错')

    def config_options(self,section):
        '''读取配置文件某section下所有键'''
        config = configparser.ConfigParser()
        config.read(config_path,encoding="utf-8-sig")
        username = config.options(section)
        return username


    def get_addkey(self,user):
        '''遍历获得配置文件收件人email'''
        sum = 0
        L = []
        for i in user:
            if sum < len(user):
                emails = self.config_get(i,'addressed')
                L.append(emails)
                sum += 1
        return L
