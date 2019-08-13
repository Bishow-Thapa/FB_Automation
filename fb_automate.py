import time
import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.firefox.options import Options 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of the program')

class FB:
	def __init__(self, username, password):
		self.username = username
		self.password = password

		options = Options()
		options.set_preference("dom.webnotifications.enabled", False)
		self.browser = webdriver.Firefox(firefox_options = options)
		self.browser.get('http://facebook.com')

	def login(self):
		browser = self.browser
		email = browser.find_element(by=By.ID, value="email")
		email.send_keys(self.username)
		pwd = browser.find_element(by=By.ID, value="pass")
		pwd.send_keys(self.password)
		pwd.send_keys(Keys.RETURN)

	def takeaNap(self):
		time.sleep(15)

	def update_status(self):
		browser = self.browser
		# variable to store 
		binary = "Your status here."
		try:
			status = browser.find_element(by=By.TAG_NAME, value="textarea")
			status.send_keys(binary)
			share = browser.find_element(by=By.CLASS_NAME, value="_6c0o")
			share.click()
			logging.debug("Facebook status updated successfully")
			browser.refresh()
		except:
			logging.debug("Facebook status not uploaded")

	def like_post(self):
		browser = self.browser
		i = 0
		while i < 3:
			toLike = browser.find_element(by=By.CLASS_NAME, value="_666k")

			atag = browser.find_element(by=By.CLASS_NAME, value="_6a-y")
			getAttribute = atag.get_attribute("aria-pressed") 
			logging.debug(getAttribute)

			if getAttribute == 'false':
				toLike.click()
				logging.debug("I liked this post!! ")
			else:
				logging.debug("already liked!! Refresh")
				time.sleep(6)
		
			i += 1
			browser.refresh()

	def logout(self):
		browser = self.browser
		logoutBtn = browser.find_element(by=By.ID, value="logoutMenu")
		logoutBtn.click()

		try:
			ab = "/html/body/div[24]/div/div/div/div/div[1]/div/div/ul/li[19]/a/span/span"
			element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[24]/div/div/div/div/div[1]/div/div/ul/li[19]/a/span/span")))
			logout.find_element(by=By.XPATH, value=ab)
			logout.click()
			winsound.PlaySound("CTU24", winsound.SND_FILENAME)

		except Exception as err:
			browser.quit()
			winsound.PlaySound("silicon", winsound.SND_FILENAME)
			logging.debug("An exception happened: " + str(err))


# myFB = FB('username@gmail.com', 'yourpasshere')
myFB = FB('fbemailhere or number', 'yourpasshere')
myFB.login()
myFB.takeaNap()
myFB.update_status()
myFB.takeaNap()
myFB.like_post()
myFB.takeaNap()
myFB.logout()