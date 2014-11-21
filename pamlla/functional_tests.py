__author__ = 'stephaniehippo'

from selenium import webdriver
from django.test import TestCase

browser = webdriver.Firefox()
browser.get('http://localhost:8000/home/')

#confirms page loads
assert 'PAMLLA Login' in browser.title

browser.get('http://localhost:8000/patients/')

table = browser.find_element_by_id("patient_list")
assert len(table.find_elements_by_tag_name('tr')) >= 2

browser.close()