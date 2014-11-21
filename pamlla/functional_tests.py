__author__ = 'stephaniehippo'

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000/home/')

assert 'PAMLLA Login' in browser.title