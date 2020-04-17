from selenium import webdriver
import pandas as pd
import time
scraper = webdriver.Chrome('./chromedriver.exe')
scraper.get("http://ytcomments.klostermann.ca/")
##인풋 즉 url이 있는 파일
input_df = pd.read_csv("./input.csv")
input_df['video_link']
down_fail =[]
##range 에 내가 넣을 인풋의 개수를 넣고 돌린다. 한방에 돌리려면 8만개 모두!
for i in range(41840,60000):
    url = input_df['video_link'][i]
    try:
        urlinput = scraper.find_element_by_xpath("""//*[@id="yt-url"]""")
        urlinput.send_keys(url)
        scraper.find_element_by_xpath("""//*[@id="scrape-btn"]""").click()
        time.sleep(3)
        scraper.find_element_by_xpath("""//*[@id="result-tabs"]/li[2]/a""").click()
        time.sleep(0.1)
        scraper.find_element_by_xpath("""//*[@id="save-dropdown"]""").click()
        time.sleep(0.1)
        scraper.find_element_by_xpath("""//*[@id="save-csv"]""").click()
        time.sleep(0.1)
        scraper.find_element_by_xpath("""/html/body/nav/div/div[1]/a/span/span[4]""").click()
        time.sleep(2)
    except:
        print(i)
        down_fail.append(input_df['video_link'][i])
        scraper.get("http://ytcomments.klostermann.ca/")
        time.sleep(1.5)
        pass
print(len(down_fail))