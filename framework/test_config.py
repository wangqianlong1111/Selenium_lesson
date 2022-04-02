from framework.Base_Page import BasePage

s = BasePage(driver=1)
bro =s.config_get('browser','environment')
print('browser是：%s' %bro)

url = s.config_get('url')
print('url是：%s' % url)


s.config_write('用户名','username','environment')
s.config_write('yonghuming','username')
s.config_write(section='yonghu')

s.config_delete('用户名','environment')
s.config_delete('yonghuming')
s.config_delete(section='yonghu')

