from selenium import webdriver

browser = webdriver.Firefox()
browser.get("https://www.irctc.co.in/eticketing/loginHome.jsf")

userID=browser.find_element_by_id("usernameId")
password= browser.find_element_by_name("j_password")