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
