from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from infoFunctions import getTeamInfo, getGameState

# 1: passive
# 2: challenge
# 3: matchmaking
mode = 3
player = "BottyGurl"
username = ""
if mode == 2:
	username = "BottyBoy"
else:
	username = "BottyGurl"

class Engine:
	def __init__(self):
		pass

	def main(self):
		# enable browser logging
		d = DesiredCapabilities.CHROME
		d['loggingPrefs'] = { 'browser':'ALL' }
		driver = webdriver.Chrome(desired_capabilities=d)
		self.login(driver)
		if mode == 1:
			while True:
				self.acceptMatch(driver)
		elif mode == 2:
			while True:
				self.challengePlayer(driver, player)
		else:
			while True:
				self.randomMatch(driver)
	def login(self, driver):
		# load some site
		driver.get('https://pokemonshowdown.com/')
		# click play
		driver.find_element_by_link_text('Play').click()
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, .03).until(EC.presence_of_element_located((By.XPATH, '//button[@class="button mainmenu1 big"]')))
				worked = True
			except:
				pass
		driver.find_element_by_xpath('//button[@class="button mainmenu1 big"]').click()
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'username')))
				worked = True
			except:
				pass
		driver.find_element_by_name('username').send_keys(username)
		driver.find_element_by_xpath("//button[@type='submit']").click()
	def acceptMatch(self, driver):
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'acceptChallenge')))
				worked = True
			except:
				pass
		driver.find_element_by_name('acceptChallenge').click()
		self.playGame(driver)

	def challengePlayer(self, driver, player):
		while not driver.find_elements_by_xpath('//span[@data-name=" '+username+'"]'):
			pass
		driver.find_element_by_name('finduser').click()
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'data')))
				worked = True
			except:
				pass
		driver.find_element_by_name('data').send_keys(player)
		driver.find_element_by_xpath("//button[@type='submit']").click()
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'challenge'))).click()
				worked = True
			except:
				pass
		#driver.find_element_by_name('challenge').click()
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.NAME, 'makeChallenge')))
				worked = True
			except:
				pass
		driver.find_element_by_name('makeChallenge').click()
		self.playGame(driver)



	def randomMatch(self, driver):
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//span[@data-name=" '+username+'"]')))
				worked = True
			except:
				pass
		driver.find_element_by_xpath('//button[@class="button mainmenu1 big"]').click()
		self.playGame(driver)
	def playGame(self, driver):
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'whatdo')))
				worked = True
			except:
				pass
		gamestate = getGameState(driver)
		driver.find_element_by_xpath('//button[@name="chooseMove"][@value=1]').click()
		while True:
			inc = False
			try:
				whatdo = driver.find_element_by_class_name('whatdo')
				
				if "Switch" in whatdo.text:
					self.choosePoke(driver)
				else:
					self.chooseMove(driver)
			except:
				pass
			try:
				driver.find_element_by_name('closeAndRematch')
				driver.find_element_by_name('closeRoom').click()
				return
			except:
				pass
	def choosePoke(self, driver):
		for i in range(6):
			if driver.find_elements_by_xpath('//button[@name="chooseSwitch"][@value={0}]'.format(i)):
				driver.find_element_by_xpath('//button[@name="chooseSwitch"][@value={0}]'.format(i)).click()
				return
	def chooseMove(self, driver):
		for i in range(1,5):
			if driver.find_elements_by_xpath('//button[@name="chooseMove"][@value={0}]'.format(i)):
				driver.find_element_by_xpath('//button[@name="chooseMove"][@value={0}]'.format(i)).click()
				return

if __name__ == '__main__':
	bot = Engine()
	bot.main()