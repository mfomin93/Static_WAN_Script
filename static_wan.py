import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium import webdriver


# myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'IdOfMyElement')))


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# Test Parameters
# Auto generated application URL parameter
ApplicationURL = "http://192.168.1.1/"

# 1. Navigate to '{ApplicationURL}'
driver.get(f'{ApplicationURL}')
# 2. Click 'username'
username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
# username = driver.find_element(By.CSS_SELECTOR,
#                                "#username")
username.click()

# 3. Type 'araknis' in 'username'
username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#username')))
username.send_keys("araknis")

# 4. Type 'araknis1' in 'password1'
# password1 = driver.find_element(By.CSS_SELECTOR,
#                                 "#password")
password = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
# password1.send_keys("araknis")
password.send_keys("araknis")

# 5. Send 'ENTER' key(s)
ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(2)

# 6. Click 'newpassword'
newpassword = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#newpassword')))
# newpassword = driver.find_element(By.CSS_SELECTOR,
#                                   "#newpassword")
newpassword.click()
'''

'''
# (STEP DISABLED)
# 7. Type 'araknis1' in 'newpassword'
newpassword = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#newpassword')))
# newpassword = driver.find_element(By.CSS_SELECTOR,
#                                   "#newpassword")
newpassword.send_keys("araknis1")
'''

'''
# (STEP DISABLED)
# 8. Type 'araknis1' in 'confpassword'
confpassword = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#confpassword')))
# confpassword = driver.find_element(By.CSS_SELECTOR,
#                                    "#confpassword")
confpassword.send_keys("araknis1")
'''

'''
# (STEP DISABLED)
# 9. Click 'Apply'
apply = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#checkDataValidation')))
# apply = driver.find_element(By.CSS_SELECTOR,
#                             "#checkDataValidation")
apply.click()

driver.get(f'{ApplicationURL}/settings/wan.html')

time.sleep(3)
# 12. Click '0_connection_type'
# _0_connection_type = driver.find_element(By.CSS_SELECTOR,
#                                          "[id = '0_connection_type']")
_0_connection_type = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, '0_connection_type')))
_0_connection_type.click()

# 13. Select the 'static' option in '0_connection_type'
_0_connection_type = driver.find_element(By.CSS_SELECTOR,
                                         "[id = '0_connection_type']")
Select(_0_connection_type).select_by_value("static")

# 14. Clear '10.0.0.2' contents
_10_0_0_2 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_IP_address']")
_10_0_0_2.clear()

# 15. Type '10.0.0.2' in '10.0.0.2'
_10_0_0_2 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_IP_address']")
_10_0_0_2.send_keys("10.0.0.2")

# 16. Clear '0.0.0.0' contents
_0_0_0_0 = driver.find_element(By.CSS_SELECTOR,
                               "[id = '0_subnet_mask']")
_0_0_0_0.clear()

# 17. Type '255.255.255.0' in '0.0.0.0'
_0_0_0_0 = driver.find_element(By.CSS_SELECTOR,
                               "[id = '0_subnet_mask']")
_0_0_0_0.send_keys("255.255.255.0")

# 18. Clear '0.0.0.01' contents
_0_0_0_01 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_default_gateway']")
_0_0_0_01.clear()

# 19. Type '10.0.0.1' in '0.0.0.01'
_0_0_0_01 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_default_gateway']")
_0_0_0_01.send_keys("10.0.0.1")

# 20. Clear '0.0.0.02' contents
_0_0_0_02 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_dns1']")
_0_0_0_02.clear()

# 21. Type '8.8.8.8' in '0.0.0.02'
_0_0_0_02 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_dns1']")
_0_0_0_02.send_keys("8.8.8.8")

# 22. Clear '0.0.0.03' contents
_0_0_0_03 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_dns2']")
_0_0_0_03.clear()

# 23. Type '8.8.4.4' in '0.0.0.03'
_0_0_0_03 = driver.find_element(By.CSS_SELECTOR,
                                "[id = '0_dns2']")
_0_0_0_03.send_keys("8.8.4.4")

# 24. Click 'Apply1'
apply1 = driver.find_element(By.CSS_SELECTOR,
                             "#checkDataValidation")
apply1.click()

# 25. Click 'Apply2'
apply2 = driver.find_element(By.CSS_SELECTOR,
                             "#wan_apply")
time.sleep(1)
apply2.click()

time.sleep(20)
driver.quit()
