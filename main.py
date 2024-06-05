import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

df = pd.read_excel('parse1.xlsx')

driver = webdriver.Chrome()


# driver.get('https://www.autodoc.ru/')

# search_input = driver.find_element(By.ID, "partNumberSearch") 


# search_input.send_keys('HZT-HD-000')
# search_input.send_keys(Keys.RETURN)

driver.get('https://www.autodoc.ru/')
cabinet = driver.find_element(By.CLASS_NAME, "cabinet") 
cabinet.click()
time.sleep(2) 
login_box = driver.find_element(By.ID, "Login") 
login_box.send_keys('ADH-3702')

password_box = driver.find_element(By.ID, "Password") 
password_box.send_keys('BEB783FA')
password_box.send_keys(Keys.RETURN)




time.sleep(3) 


def get_price(model, brand):

    driver.get('https://www.autodoc.ru/')
    
    try:
        search_box = driver.find_element(By.ID, "partNumberSearch") 
        search_box.send_keys(model)
        search_box.send_keys(Keys.RETURN)
    except:
        pass


    try:
        brands = driver.find_elements(By.CLASS_NAME, "company")
        for brand_chooser in brands:
            if brand_chooser.text == brand:
                brand_chooser.click()

    except:
        pass



    time.sleep(2)  
    
    # price = driver.find_element_by_css_selector('price-number').text
    try:
        prices = driver.find_elements(By.CLASS_NAME, "price")
        price = prices[1].text
        directions = driver.find_elements(By.CLASS_NAME, "direction")
        direction = directions[1].text
    except:
        price = 'нет цены'
        direction = 'некуда'
    
    return price, direction


for index, row in df.iterrows():
    model = row['Model'] 
    brand = row['Brand'] 
    price, direction = get_price(model, brand)
    df.at[index, 'Price'] = price 
    df.at[index, 'Direction'] = direction 


df.to_excel('parse12.xlsx', index=False)

driver.quit()