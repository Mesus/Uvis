import webbrowser,requests
# from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/smart'
url2 = 'http://www.google.co.jp/trends/explore?q=Unmanned_ground_vehicle'
# r = requests.get(url2)
# r.encoding = 'utf-8'
# doc = r.text
# print doc
# pagesoup = BeautifulSoup(doc, 'lxml')
# print pagesoup.find(id='mw-content-text')
# from pyvirtualdisplay import Display
from selenium import webdriver
driver = webdriver.PhantomJS()
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('/home/vicent/PycharmProjects/UvisEnv/frame/geckodriver')
# display = Display(visible=0, size=(800, 600))
# display.start()
# driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()
# driver.find_element_by_id('mw-content-text')
driver.save_screenshot('screenshot.png')