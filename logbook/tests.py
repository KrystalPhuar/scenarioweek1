from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class SignupTest(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/linying/Downloads/chromedriver')
		super(SignupTest, self).setUp()

	def tearDown(self):
		self.driver.quit()
		super(SignupTest, self).tearDown()

	def test_login(self):
		print('Signup')
		driver = self.driver
		driver.get('http://127.0.0.1:8000/logbook/signup/')
		driver.find_element_by_id("id_username").send_keys("temptest@gmail.com")
		driver.find_element_by_id("id_password1").send_keys("ucl393939")
		driver.find_element_by_id("id_password2").send_keys("ucl393939")
		driver.find_element_by_css_selector("button[type=submit]").click()
		time.sleep(3)



class LoginTest(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/linying/Downloads/chromedriver')
		super(LoginTest, self).setUp()
	def tearDown(self):
		self.driver.quit()
		super(LoginTest, self).tearDown()
	def test_login(self):
		print('login')
		driver = self.driver
		driver.get('http://127.0.0.1:8000/logbook/')
		driver.find_element_by_id("id_username").send_keys("temp22@gmail.com")
		driver.find_element_by_id("id_password").send_keys("ucl393939")
		driver.find_element_by_css_selector("input[type=submit]").click()
		time.sleep(3)




class Testadd(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/linying/Downloads/chromedriver')
		super(Testadd, self).setUp()
	def tearDown(self):
		self.driver.quit()
		super(Testadd, self).tearDown()
	def test_login(self):
		print('add')
		driver = self.driver
		driver.get('http://127.0.0.1:8000/logbook/')
		driver.find_element_by_id("id_username").send_keys("temp22@gmail.com")
		driver.find_element_by_id("id_password").send_keys("ucl393939")
		driver.find_element_by_css_selector("input[type=submit]").click()
		driver.find_element_by_xpath("//a[@href='/logbook/add/']").click()
		driver.find_element_by_id("content").send_keys("test add blog");
		driver.find_element_by_css_selector("button[type=submit]").click()
		time.sleep(3)



class Testsearch(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/linying/Downloads/chromedriver')
		super(Testsearch, self).setUp()
	def tearDown(self):
		self.driver.quit()
		super(Testsearch, self).tearDown()
	def test_login(self):
		print('search')
		driver = self.driver
		driver.get('http://127.0.0.1:8000/logbook/')
		driver.find_element_by_id("id_username").send_keys("temp22@gmail.com")
		driver.find_element_by_id("id_password").send_keys("ucl393939")
		driver.find_element_by_css_selector("input[type=submit]").click()
		time.sleep(1)
		driver.find_element_by_xpath("//a[@href='/logbook/search/']").click()
		driver.find_element_by_css_selector("input[type=text]").send_keys("temp")
		driver.find_element_by_css_selector("button[type=submit]").click()
		time.sleep(3)




class TestLogout(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome('/Users/linying/Downloads/chromedriver')
		super(TestLogout, self).setUp()
	def tearDown(self):
		self.driver.quit()
		super(TestLogout, self).tearDown()
	def test_login(self):
		print('logout')
		driver = self.driver
		driver.get('http://127.0.0.1:8000/logbook/')
		driver.find_element_by_id("id_username").send_keys("temp22@gmail.com")
		driver.find_element_by_id("id_password").send_keys("ucl393939")
		driver.find_element_by_css_selector("input[type=submit]").click()
		time.sleep(1)
		driver.find_element_by_xpath("//a[@href='/accounts/logout/?next=/logbook/']").click()
		time.sleep(3)


