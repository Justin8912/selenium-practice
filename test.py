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

    numberOfElements = len(flowchart)
    elementIdx = 0

    '''
    Previously I was running a for loop over the elements that I had in this flowChart list 
    but when I did that I kept getting the staleElementError. I am not 100% sure why this was 
    happening, becuase even though I was running the for loop I was refreshing the flowchart 
    elements after each iteration.  
    '''
    while (numberOfElements != elementIdx):
        valid = True
        cell = flowchart[elementIdx].find_elements(By.TAG_NAME, 'td')
        for time in excluded_times:
            if (time in cell[0].text):
                print(f'Exclude this unique number: {cell[0].text}')
                valid = False
                elementIdx += 1
                break
        if ("Section" in cell[0].text):
            valid = False
            elementIdx += 1
        if valid:
            print("Perform operations on this unique number: " + cell[0].text)
            cell[0].click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "setSeatNumber")))
            textInput = driver.find_element(By.ID, "setSeatNumber")
            submitButton = driver.find_element(By.TAG_NAME, "button")
            textInput.clear()
            textInput.send_keys(6)
            submitButton.click()
            elementIdx += 1
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))
            sleep(3)
            flowchart = get_unique_numbers(driver)

    driver.quit()

def interactWithGoogle():
    link = "https://www.google.com"
    driver = webdriver.Chrome()
    driver.get(link)

    searchBar = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
    searchBar.send_keys("canvas ut")
    searchBar = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
    searchBar.send_keys(Keys.RETURN)
    searchBar = driver.find_element(by=By.CSS_SELECTOR, value="textarea")
    searchBar.click()

    driver.quit()

def main():
    interactWithTestEnv()
    # interactWithGoogle()

main()