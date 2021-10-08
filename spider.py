from selenium import webdriver
import time
import argparse
import logging
import os
import sys
import pandas as pd
import selenium

cookies = [
{
    "domain": ".medsci.cn",
    "expirationDate": 1695523873,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_ga",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GA1.2.377394777.1632408083",
    "id": 1
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1632451928,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_gat",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 2
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1632538273,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_gid",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GA1.2.1645063706.1632408083",
    "id": 3
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1727059387,
    "hostOnly": False,
    "httpOnly": False,
    "name": "exterior_info",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "%7B%22project_id%22%3A1%2C%22project_code%22%3A%22MSYX%22%2C%22redirect_url%22%3A%22https%3A%2F%2Fwww.medsci.cn%22%7D",
    "id": 4
},
{
    "domain": ".medsci.cn",
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lpvt_410ec554592b4d7b85b3e6cdc413fa52",
    "path": "/",
    
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "1632451873",
    "id": 5
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1663987873,
    "hostOnly": False,
    "httpOnly": False,
    "name": "Hm_lvt_410ec554592b4d7b85b3e6cdc413fa52",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1632408083",
    "id": 6
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1947768082,
    "hostOnly": False,
    "httpOnly": False,
    "name": "msStatisUserId",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1632408082494_e851b310",
    "id": 7
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1727059387,
    "hostOnly": False,
    "httpOnly": False,
    "name": "redirect_url",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "https%3A%2F%2Fwww.medsci.cn%3Fsso_sessionid%3D2dd35615071_f2ff2aef6cbe4c71901fdd7474ade6d3",
    "id": 8
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1947811873,
    "hostOnly": False,
    "httpOnly": False,
    "name": "registerBusinessName",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "sci",
    "id": 9
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1947811873,
    "hostOnly": False,
    "httpOnly": False,
    "name": "registerBusinessNameChild",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "nsfc.do",
    "id": 10
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1727059387,
    "hostOnly": False,
    "httpOnly": False,
    "name": "sso_sessionid",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "2dd35615071_f2ff2aef6cbe4c71901fdd7474ade6d3",
    "id": 11
},
{
    "domain": ".medsci.cn",
    "expirationDate": 1727059873.089947,
    "hostOnly": False,
    "httpOnly": False,
    "name": "userInfo",
    "path": "/",
    
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "%7B%22getRoleLoginResponses%22%3A%5B%7B%22identityFlag%22%3A0%2C%22roleId%22%3A8%2C%22roleName%22%3A%22%E5%89%8D%E5%8F%B0%E8%A7%92%E8%89%B2%22%7D%5D%2C%22mobile%22%3A%2218811577526%22%2C%22plaintextUserId%22%3A5615071%2C%22projectCode%22%3A%22MSYX%22%2C%22projectId%22%3A1%2C%22projectName%22%3A%22%E6%A2%85%E6%96%AF%E5%8C%BB%E5%AD%A6%22%2C%22projectType%22%3A0%2C%22projectUserStatus%22%3A1%2C%22realName%22%3A%22echooo%22%2C%22token%22%3A%7B%22accessToken%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJtczMwMDAwMDAxODc2NzY1NTIiLCJ1c2VySWQiOiI1NjE1MDcxIiwidXNlcm5hbWUiOiJtczMwMDAwMDAxODc2NzY1NTIiLCJleHAiOjIyNjMxNzE4NzN9.ccn2mqLo4sGy2NQLyiq9esnKX6oxyYWDtQcRAY1GthClwQwI1JWRZYk98nXOIHgauX-mXtPjmVHv7TtbavXDleZ5Oht9fZFubn8p0XMCeuwtmr7g4flsG5rirX_v5vLVRnx_jNgrYi6JM2zdYas2_ygFmuatp0zUCdcwKEnMnng%22%2C%22accessTokenExpireTime%22%3A630720000%2C%22refreshToken%22%3A%22eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJtczMwMDAwMDAxODc2NzY1NTIiLCJ1c2VySWQiOiI1NjE1MDcxIiwidXNlcm5hbWUiOiJtczMwMDAwMDAxODc2NzY1NTIiLCJleHAiOjE2MzI1MzgyNzN9.Bdoa0BuEILTIpigp68RmEs-QCPbh8gLNb3z_KgUpzf5plxpmvawWOuXvzd8xTVe4AdhPhqTzFD2azmG_iFp-d3O6aOUfSx9VPpWGiB5RlmSymekZkpq2n160u4UVWnzmmMru-CtyKGBG_3fo-6TOvzLYT-YEEyjxC2emP8ETkzw%22%7D%2C%22userId%22%3A%222dd35615071%22%2C%22userName%22%3A%22ms3000000187676552%22%2C%22userStatus%22%3A1%7D",
    "id": 12
},
{
    "domain": "www.medsci.cn",
    "hostOnly": True,
    "httpOnly": True,
    "name": "JSESSIONID",
    "path": "/",
    
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "84B18A5E27C97C33E76E5F88A3A432E7",
    "id": 13
}
]

def main(opt):
    logger = get_logger('spider', file_name=os.path.join('/Users/echooo/Downloads', '国自然基金'))
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    #配置并获得WebDriver对象
    driver = webdriver.Chrome('/Users/echooo/Documents/中科院/chromedriver', options=option)
    journal_list = []
    for i, keyword in enumerate(opt.keyword):
    #发起get请求
        driver.get(opt.url)
        # input_element = driver.find_element_by_name('txtitle')
        # input_element.send_keys('滇池')
        # input_element.submit()

        for item in cookies:
            driver.add_cookie(item)

        search_text = driver.find_element_by_id('searchValue') 
        search_text.send_keys(keyword) 
        search_text.submit()
        driver.find_element_by_id("search-button").click()

        title = driver.title # 打印当前页面title
        logger.info(title)
        user = driver.find_element_by_class_name('list-result').text # # 获取结果数目
        num = get_num(user)
        logger.info(num)
        for i in range(num%15+2):
            read_journal(driver=driver, journal_list=journal_list, keyword=keyword)
            # now_url = driver.current_url # 打印当前页面URL
            result = driver.find_element_by_id('journalList').text
            # result = driver.find_element_by_class_name('journal-item flex').text
            logger.info(result)
            driver.find_element_by_link_text('下一页').click()
            time.sleep(2)
        pd.DataFrame(journal_list).to_csv(os.path.join('/Users/echooo/Downloads', '国自然基金' + '.csv'))
     

def read_journal(driver, journal_list:list, keyword):
    for i in range(1, 16):
        try:
            title = driver.find_element_by_xpath(f'//*[@id="journalList"]/div[{i}]/div/strong/a').text
            people = driver.find_element_by_xpath(f'//*[@id="journalList"]/div[{i}]/div/div/div[1]/p[1]').text.split('：')[1]
            origination = driver.find_element_by_xpath(f'//*[@id="journalList"]/div[{i}]/div/div/div[1]/p[2]').text.split('：')[1]
            value = driver.find_element_by_xpath(f'//*[@id="journalList"]/div[{i}]/div/div/div[2]/p[1]').text.split('：')[1]
            type = driver.find_element_by_xpath(f'//*[@id="journalList"]/div[{i}]/div/div/div[2]/p[2]').text.split('：')[1]
            code = driver.find_element_by_xpath(f'//*[@id="journalList"]/div[{i}]/div/div/div[3]/p[1]').text.split('：')[1]
            time = driver.find_element_by_xpath(f'//*[@id="journalList"]/div[{i}]/div/div/div[3]/p[2]').text.split('：')[1]
            dict = {'关键词':keyword, '名称':title, '负责人':people, '单位':origination, '金额':value, '类型':type, '学科代码':code, '开始时间':time}
            journal_list.append(dict)
        except:
            continue

def get_logger(name, file_name='./', level=logging.INFO):
    # logging.basicConfig(filename=file_name+'model.log', level=level)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    # Logging to console
    stream_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        '%(asctime)s [%(threadName)s] %(levelname)s %(name)s - %(message)s')
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    if not os.path.exists(file_name):
        os.makedirs(file_name)

    file_handler = logging.FileHandler(file_name+'.txt')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', nargs='+', type=str, default='https://www.medsci.cn/sci/nsfc.do')
    parser.add_argument('--keyword', nargs='+', type=list, default=['滇池', '滇中', '滇东', '三江并流', '澜沧江', '怒江', '金沙江', '横断山', '洱海', '抚仙湖', '阳宗海', '澜湄', '红河断裂带','航空遥感', '多源数据', '高分辨率', '天空地', '空天地', '深度学习', '人工智能'])
    opt = parser.parse_args()
    return opt

def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)
