import selenium 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

excluded_times = [
    "10:30am - 4:30am",
]

def get_unique_numbers(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    rows = driver.find_elements(By.TAG_NAME, "tr")
    return rows

def interactWithTestEnv():
    link = "http://localhost:3000"
    driver = webdriver.Chrome()
    driver.get(link)
    driver.get_log('browser')

    # flowchart = driver.find_elements(By.CSS_SELECTOR, "tr")
    flowchart = get_unique_numbers(driver)

    print(flowchart)
    for row_element in flowchart: 
        valid = True
        cell = row_element.find_elements(By.TAG_NAME, 'td')
        for time in excluded_times:
            if (time in row_element.text):
                print(f'Exclude this unique number: {cell[0].text}')
                valid=False
                continue
        if ("Section" in row_element.text):
            valid = False
        if valid:
            print("Perform operations on this unique number: " + cell[0].text)
            cell[0].click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "setSeatNumber")))
            textInput = driver.find_element(By.ID, "setSeatNumber")
            submitButton = driver.find_element(By.TAG_NAME, "button")
            textInput.clear()
            textInput.send_keys(6)
            submitButton.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))
            sleep(10)
            flowchart = get_unique_numbers(driver)

    
    # flowchart.click()
    input("")
    driver.quit()

def interactWithGoogle():
    link = "https://www.google.com"
    driver = webdriver.Chrome()
    driver.get(link)

    searchBar = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
    searchBar.send_keys("canvas ut")
    searchBar = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
    searchBar.send_keys(Keys.RETURN)
    # searchBar = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
    # searchBar.click()
    


    
    # driver.quit()

def main():
    interactWithTestEnv()
    # interactWithGoogle()

main()