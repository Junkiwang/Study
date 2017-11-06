from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time


def SetUp():
    username = 'root'
    password = '000000'
    global driver
    driver = webdriver.Chrome()
    # driver.maximize_window()  # 最大化浏览器窗口
    driver.get('http://172.18.20.250')
    driver.implicitly_wait(10)  # 智能等待10秒，意思等待页面加载最长10秒时间,全局使用，只使用一次即可
    driver.find_element_by_id('user').clear()  # 清除一下
    elem = driver.find_element_by_id('user')
    elem.send_keys(username)
    driver.find_element_by_id('password').clear()
    elem = driver.find_element_by_id('password')
    elem.send_keys(password)
    # driver.find_element_by_id('password').send_keys(Keys.ENTER) # 直接发送Enter登录，需导入Keys包
    driver.find_element_by_xpath('//input[@value="Login"]').click()
    # driver.quit()
    # 首页登陆完成，下面进入网页上想定位的元素所在的框架
    time.sleep(1)


SetUp()


def Change_to_Chinese():
    currentWin = driver.current_window_handle  # 获取当前窗口的句柄
    driver.switch_to.frame('head')
    driver.find_element_by_link_text('中文').click()
    print('切换到中文界面')
    time.sleep(1)
    handles = driver.window_handles  # 获取所有窗口的句柄
    for i in handles:
        if currentWin == i:
            continue
        else:
            driver.switch_to.window(i)  # 将driver与新的页面绑定起来
    driver.refresh()
    print('页面刷新')
    time.sleep(1)


# Change_to_Chinese()


def Change_to_ManualBt():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('sidebar')
    driver.find_element_by_xpath("//span[contains(text(), 'System Control')]").click()  # or System Control
    # 判断当前工作模式
    time.sleep(1)
    driver.switch_to.parent_frame()
    driver.switch_to.frame('head')
    time.sleep(3.5)
    elem = driver.find_element_by_id('opmode')
    if elem.text == 'Auto' or elem.text == '自动':
        print('当前工作模式为自动模式，不能进行手动控制操作')
        time.sleep(1)
        driver.switch_to.parent_frame()
        driver.switch_to.frame('main')
        driver.find_element_by_id('ManualBt').click()
        print('转换到手动工作模式')
        time.sleep(1)
        driver.switch_to.alert.accept()
        time.sleep(1)
        alert = driver.switch_to.alert
        if alert.text == 'Set Failed' or alert.text == '设置失败':
            print('工作模式转换失败')
        else:
            print('工作模式转换成功')
        alert.accept()
    else:
        print('当前工作模式为手动模式，可以进行手动控制操作')
    time.sleep(1)


# Change_to_ManualBt()

def ManualBLVD():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main')
    time.sleep(1)
    elem = driver.find_element_by_id('BLVDTxt')
    if elem.text == 'Connected' or elem.text == '连接':
        print('当前BLVD是上电状态，可以手动下电')
    else:
        print('当前BLVD是下电状态，可以手动上电')
    try:  # 尝试手动电池上下电
        driver.find_element_by_id('BLVDConBt').click()
        print('手动电池上电')
    except:
        driver.find_element_by_id('BLVDDisConBt').click()
        print('手动电池下电')
    # finally:
    #    print('手动电池上下电控制动作执行完成')
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(1)
    alert = driver.switch_to.alert
    if alert.text == 'Set Failed' or alert.text == '设置失败':
        print('手动电池上下电控制失败')
    else:
        print('手动电池上下电控制成功')
    alert.accept()


# ManualBLVD()


def Change_to_AutoBt():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main')
    driver.find_element_by_id('AutoBt').click()
    driver.switch_to.alert.accept()
    time.sleep(1)
    driver.switch_to.alert.accept()
    print('恢复转换到自动工作模式')
    print('测试结束')


# Change_to_AutoBt()

def BusVolt():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('sidebar')
    # 将滚动条移动到页面的顶部
    js = "document.body.scrollTop=0"
    driver.execute_script(js)
    time.sleep(3)
    driver.find_element_by_xpath("//a[contains(text(), 'Power System')]").click()  # or Power System
    time.sleep(1)
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main')
    elem = driver.find_element_by_id('busVolt')
    print('当前模块输出电压：' + elem.text)
    elem = driver.find_element_by_id('battCurr')
    print('当前电池电流：' + elem.text)
    elem = driver.find_element_by_id('loadCurr')
    print('当前负载电流：' + elem.text)
    return


# BusVolt()


def FirmwareUpdate():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('sidebar')
    # 将页面滚动条拖到底部
    js = "document.body.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(3)
    driver.find_element_by_xpath("//span[contains(text(), 'About')]").click()  # about
    time.sleep(1)
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main')
    driver.find_element_by_xpath('//*[@id="formFirm"]/input[1]').send_keys(
        'F:\\SVN\Controller\SC501软件版本升级\SC501 FIRMWARE V107\SZ1101_SC501_APP_83550112_V107.dat')
    driver.find_element_by_xpath('//*[@id="formFirm"]/input[2]').click()
    time.sleep(30)
    print('完成')


# FirmwareUpdate()


def Horizontal_scrolling():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('sidebar')
    # 将页面滚动条拖到底部
    js = "document.body.scrollTop=10000"
    driver.execute_script(js)
    time.sleep(1)
    driver.find_element_by_xpath("//a[contains(text(), 'History Operation')]").click()
    time.sleep(1)
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main')
    time.sleep(1)
    # 将页面滚动条拖到右边
    js = 'document.getElementById("sc1").scrollLeft=10000'
    driver.execute_script(js)
    time.sleep(1)
    # 将页面滚动条拖到左边
    js = 'document.getElementById("sc1").scrollLeft=0'
    driver.execute_script(js)
    time.sleep(1)


# Horizontal_scrolling()


def Getcookies():
    print(driver.get_cookies())
    driver.add_cookie({'name': 'wjunqi', 'value': 's123456'})
    cookies = driver.get_cookies()
    for cookie in cookies:
        print('%s -> %s' % (cookie['name'], cookie['value']))
    driver.delete_cookie(name='wjunqi')
    cookies = driver.get_cookies()
    for cookie in cookies:
        print('%s -> %s' % (cookie['name'], cookie['value']))
    # driver.delete_all_cookies()
    print(driver.get_cookies())


# Getcookies()
row = (
    'tr1', 'tr2', 'tr3', 'tr4', 'tr5', 'tr6', 'tr7', 'tr8', 'tr9', 'tr10', 'tr11', 'tr12', 'tr13', 'tr14', 'tr15',
    'tr16', 'tr17', 'tr18', 'tr19', 'tr20')


def Text_is_here():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('sidebar')
    driver.find_element_by_xpath("//span[contains(text(), 'Current alarm')]").click()
    time.sleep(2)
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main')
    currentnum = driver.find_element_by_id('pnum').get_attribute("value")
    currentnum = list(map(int, currentnum.split('/')))
    print(currentnum)
    pagenum = currentnum[1]
    global row
    # row = (
    #     'tr1', 'tr2', 'tr3', 'tr4', 'tr5', 'tr6', 'tr7', 'tr8', 'tr9', 'tr10', 'tr11', 'tr12', 'tr13', 'tr14', 'tr15', 'tr16',
    #     'tr17', 'tr18', 'tr19', 'tr20')
    i = 0
    for m in range(pagenum):
        try:
            for n in row:
                i += 1
                locator = ('id', n)
                text = 'SFGHGFSG'
                result = EC.text_to_be_present_in_element(locator, text)(driver)
                if result:
                    print('第%s条告警为%s，断言测试成功' % (i, text))
                    break
            else:  # for....else语句，表示for语句正常循环结束后再执行else后面的语句，若for循环语句不是正常循环结束的，则不执行esle后面的语句
                try:
                    driver.find_element_by_id('next').click()
                    time.sleep(0.3)
                except:
                    print('翻下一页失败')
                else:
                    continue
            break
        except:
            print('无此告警，断言测试失败')


Text_is_here()


def History():
    driver.switch_to.parent_frame()
    driver.switch_to.frame('sidebar')
    driver.find_element_by_xpath("// a[contains(text(), 'History Alarm')]").click()  # 历史记录
    time.sleep(2)
    driver.switch_to.parent_frame()
    driver.switch_to.frame('main')
    historynum = driver.find_element_by_id('pnum').get_attribute("value")  # 获取input里面的页码
    historynum = list(map(int, historynum.split('/')))
    print(historynum)
    pagenum = historynum[1]
    # row = (
    #     'tr1', 'tr2', 'tr3', 'tr4', 'tr5', 'tr6', 'tr7', 'tr8', 'tr9', 'tr10', 'tr11', 'tr12', 'tr13', 'tr14', 'tr15', 'tr16',
    #     'tr17', 'tr18', 'tr19', 'tr20')
    for n in range(pagenum):
        try:
            for m in row:
                print(driver.find_element_by_id(m).text)
                time.sleep(0.4)
        except:
            print('打印完成')
        try:
            driver.find_element_by_id('next').click()
            time.sleep(0.3)
        except:
            print('翻下一页失败')

# History()
driver.quit()
