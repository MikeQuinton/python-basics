from selenium import webdriver; import base64

driver = webdriver.Chrome(r"C:\Users\Administrator\Desktop\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

driver.get("https://mail.protonmail.com/login")
driver.find_element_by_id("username").send_keys(base64.b64decode("My Username").decode("utf-8"))
driver.find_element_by_id ("password").send_keys(base64.b64decode("My Password").decode("utf-8"))
driver.find_element_by_id("login_btn").click()

