from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities    
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Engine:
	def __init__(self):
		pass

	def main(self):
		# enable browser logging
		d = DesiredCapabilities.CHROME
		d['loggingPrefs'] = { 'browser':'ALL' }
		driver = webdriver.Chrome(desired_capabilities=d)
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
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//span[@data-name=" BottyBoy"]')))
				worked = True
			except:
				pass
		driver.find_element_by_xpath('//button[@class="button mainmenu1 big"]').click()
		worked = False
		while not worked:
			try:
				WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'whatdo')))
				worked = True
			except:
				pass
		ActionChains(driver).move_to_element(driver.find_element_by_name('chooseSwitch')).perform()

		# print messages
		for entry in driver.get_log('browser'):
			print(entry)
if __name__ == '__main__':
	bot = Engine()
	bot.main()
	print('worked')