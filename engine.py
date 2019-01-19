from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from infoFunctions import getTeamInfo

class Engine:
	def __init__(self):
		pass

	def main(self):
		# enable browser logging
		d = DesiredCapabilities.CHROME
		d['loggingPrefs'] = { 'browser':'ALL' }
		driver = webdriver.Chrome(desired_capabilities=d)
		self.login(driver)
		self.acceptMatch(driver)
		#self.randomMatch(driver)
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

		driver.find_element_by_name('username').send_keys("BottyBoy")
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
	def randomMatch(self, driver):
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//span[@data-name=" BottyBoy"]')))
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

		myTeam = getTeamInfo(driver)
		driver.find_element_by_xpath('//button[@name="chooseMove"][@value=1]').click()
		currentPoke = 0
		while True:
			worked = False
			while not worked:
				try:
					WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'whatdo')))
					worked = True
				except:
					pass
			if "Switch" in driver.find_element_by_class_name('whatdo').text:
				currentPoke += 1
				driver.find_element_by_xpath('//button[@name="chooseSwitch"][@value={0}]'.format(currentPoke)).click()
			else:
				driver.find_element_by_xpath('//button[@name="chooseMove"][@value=1]').click()

if __name__ == '__main__':
	bot = Engine()
	bot.main()