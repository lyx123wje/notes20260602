from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://localhost:8000')

assert 'Django' in browser.page_source

