import requests
from bs4 import BeautifulSoup
from lxml import html
from selenium.webdriver import Chrome

# Markiplier homepage
#url = 'https://www.youtube.com/@markiplier'

# Air Force Fact Sheets
#url = 'https:/www.af.mil/About-Us/Fact-Sheets/'

# Gmail inbox
#url = 'https://mail.google.com/mail/u/0/#inbox'

#page_data = requests.get(url)

#soup = BeautifulSoup(page_data.text, 'html.parser')

#blog_titles = soup.select('h2.blog-card__content-title')

#tree = html.fromstring(page_data.text)

#blog_titles = tree.xpath('//h2[@class="blog-card__content-title"]/text()')

driver = Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
blog_titles = driver.get_elements_by_css_selector(' h2.blog-card__content-title')

for title in blog_titles:
    print(title.text)
driver.quit() # Closing the browser
