from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "//Users/adik/Downloads/chromedriver")
driver.set_page_load_timeout(10)
driver.maximize_window()

driver.get("https://www.amazon.ca/")
driver.implicitly_wait(30)
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("telescope")
driver.implicitly_wait(10)
#driver.find_element_by_name("q").send_keys("Automation")
driver.find_element_by_xpath ("//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input'] ").click()
driver.find_element_by_xpath("//span[contains(text(),'150X Astronomy Monocular Telescope 300/70mm for Ki')]").click()
driver.find_element_by_xpath("//input[@id='add-to-cart-button']").click()

