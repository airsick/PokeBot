from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from pokemon import Team
#from pokemon import gameData as game
from pokemon import Pokemon
from pokemon import pokeTypes

def getTeamInfo(driver):
	team = Team()
	ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@name="chooseDisabled"]')).perform()
	team.pokemon.append(getPoke(driver))
	for i in range(1,6):
		ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@name="chooseSwitch"][@value={0}]'.format(i))).perform()
		team.pokemon.append(getPoke(driver))
	return team

def getPoke(driver):
	poke = Pokemon()
	elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2')
	poke.name = elem.text.split()[0:-1]
	poke.level = elem.text.split()[-1][1:]

	elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2/img[1]')
	if elem.get_property("alt") != "M" and elem.get_property("alt") != "F":
		poke.types.append(elem.get_property("alt"))

	if driver.find_elements_by_xpath('//div[@class="tooltip"]/h2/img[2]'):
		elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2/img[2]')
		poke.types.append(elem.get_property("alt"))
	if driver.find_elements_by_xpath('//div[@class="tooltip"]/h2/img[3]'):
		elem = driver.find_element_by_xpath('//div[@class="tooltip"]/h2/img[3]')
		poke.types.append(elem.get_property("alt"))
		#test
#	if driver.find_elements_by_xpath('//div[@class="tooltip"]/p'):
#		elem = driver.find_elements_by_xpath('//div[@class="tooltip"]/p'+[1] ).text.split()[:-1]
#		print(elem)
#	print(driver.find_elements_by_xpath('//div[@class="tooltip"]/p'))
#		poke.hp = elem
	return poke

def getOpponent(driver):
	ActionChains(driver).move_to_element(driver.find_element_by_xpath('//div[@class="foehint"]/div[3]')).perform()
	return getPoke(driver)

def getMoves(driver):
	moves = []
	for i in range(1,5):
		if  driver.find_elements_by_xpath('//button[@name="chooseMove"][@value={0}]'.format(i)):
			moveName = driver.find_element_by_xpath('//button[@name="chooseMove"][@value={0}]'.format(i)).get_attribute("data-move")
			moveType = driver.find_element_by_xpath('//button[@name="chooseMove"][@value={0}]'.format(i)).get_attribute("class")[5:]
			ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@name="chooseMove"][@value={0}]'.format(i))).perform()
			movePower = driver.find_element_by_xpath('//div[@class="tooltip"]/p[1]').text.split()[-1]
			if movePower == "—":
				movePower = 0
			moves.append({'name':moveName, 'type':moveType, 'power':movePower})
	while len(moves) < 4:
		print('adding')
		moves.append({'name':0, 'type':"None",'power':-1})
	return moves

def getGameState(driver):
	gamestate = {}
	gamestate['team'] = getTeamInfo(driver)
	gamestate['opponent'] = getOpponent(driver)
	gamestate['team'].pokemon[0].moves = getMoves(driver)
	#game.teams=gamestate
	return gamestate

def buildFeatures(driver, gamestate):
	features = []
	for i in range(6):

		for types in gamestate['team'].pokemon[i].types:
			features.append(int(pokeTypes[types]))
		if len(gamestate['team'].pokemon[i].types) < 2:
			features.append(-1)

	gamestate['opponent'] = getOpponent(driver)
	for types in gamestate['opponent'].types:
		features.append(int(pokeTypes[types]))
	if len(gamestate['opponent'].types) < 2:
		features.append(-1)
	moves = getMoves(driver)
	for move in moves:
		features.append(int(pokeTypes[move['type']]))
		features.append(int(move['power']))
	return features

