from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.ie.webdriver import WebDriver

from chaojiying import Chaojiying_Client

def she():
    q1=Options()
    q1.add_experimental_option('detach',True)
    a1=webdriver.Chrome(service=Service(r'C:\Users\cbq\Desktop\图片验证码登陆\chromedriver.exe'), options=q1)
    a1.implicitly_wait(3)
    return a1
a1=she()
a1.get('https://www.bilibili.com/')
a1.maximize_window()
time.sleep(2)
a1.find_element(By.XPATH,'//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div/div/span').click()
time.sleep(2)
time.sleep(2)
a1.find_element(By.CSS_SELECTOR,"[placeholder='请输入账号']").send_keys('')
time.sleep(2)
a1.find_element(By.XPATH,"//input[@placeholder='请输入密码']").send_keys('')
time.sleep(2)
a1.find_element(By.XPATH,'/html/body/div[4]/div/div[4]/div[2]/div[2]/div[2]').click()
time.sleep(4)
png_element=a1.find_element(By.CLASS_NAME,'geetest_widget')
png = png_element.screenshot_as_png

#处理x,y坐标问题

#code_tag = a1.find_element(By.XPATH,'xxxxxxiv')
code_tag_half_width = int((png_element.rect['width'])/2)
code_tag_half_height = int((png_element.rect['height'])/2)

# for pos in result_list:
#     #result_list为点选返回结果位置坐标
#     x = int(pos.split(',')[0])
#     y = int(pos.split(',')[1])
#     ActionChains(a1).move_to_element_with_offset(code_tag,x-code_tag_half_width,y-code_tag_half_height).click().perform()
#     sleep(1)

#利用超级鹰对图片进行处理
chaojiying = Chaojiying_Client('', '', '969381')	#用户中心>>软件ID 生成一个替换 96001
# im = open('png', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
#print(chaojiying.PostPic(png, 9004))		#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()

list_numbers =chaojiying.PostPic(png, 9004)['pic_str'].split('|')
for list_number in list_numbers:
    number =list_number.split(',')
    x=int(number[0])
    y=int(number[1])
    ActionChains(a1).move_to_element_with_offset(png_element,x-code_tag_half_width,y-code_tag_half_height).click().perform()
    time.sleep(1)
time.sleep(10)
a1.find_element(By.CSS_SELECTOR,'.geetest_commit_tip').click()
time.sleep(3)

