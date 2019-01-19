from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def getTeamInfo(driver):
	for i in range(1,5):
		ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@name="chooseSwitch"][@value={0}]'.format(i))).perform()
		print(driver.find_element_by_xpath('//div[@class="tooltip"]/h2'))

