from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from team import Team
from pokemon import Pokemon

def getTeamInfo(driver):
	team = Team()
	ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@name="chooseDisabled"]')).perform()
	team.pokemon.append(getPoke(driver))
	for i in range(1,6):
		ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@name="chooseSwitch"][@value={0}]'.format(i))).perform()
		team.pokemon.append(getPoke(driver))

def getPoke(driver):
	poke = Pokemon()
	elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2')
	poke.name = elem.text.split()[0:-1]
	poke.level = elem.text.split()[-1][1:]

	elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2/img[1]')
	if elem.get_property("alt") != "M" and elem.get_property("alt") != "F":
		poke.types.append(elem.get_property("alt"))

	try:
		elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2/img[2]')
		poke.types.append(elem.get_property("alt"))
	except:
		pass

	try:
		elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2/img[3]')
		poke.types.append(elem.get_property("alt"))
	except:
		pass
	print(poke.name)
	print(poke.level)
	print(poke.types)
	return poke


