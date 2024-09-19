from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# captcha = driver.find_element(By.LINK_TEXT, "Try different image")
# captcha.click()
#
# price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"Total price {price_dollars.text}.{price_cents.text}")

dict_event = {}

date = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
value = driver.find_elements(By.CSS_SELECTOR, '.event-widget ul a')

for i in range(len(date)):
    dict_event[i] = {"time": date[i].text, "name": value[i].text}

print(dict_event)

driver.quit()

