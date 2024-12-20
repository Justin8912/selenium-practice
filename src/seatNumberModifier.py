from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Setting variables for use
seat_number = ""

excluded_times = [
    # "10:30am - 4:30am",
]

excluded_sections = [
    # "49500"
]

link = "http://localhost:3000" # This will need to be updated with whatever link we need to use

# Asking for user input if the above variables do not exist
if seat_number == "":
    msg = "What is the desired number of seats: "
    seat_number = input(msg)
    while seat_number == "":
        print("Seat number cannot be set to nothing. Please try entering a valid number.")
        seat_number = input(msg)

if link == "":
    msg = "Where should the bot be run? "
    link = input(msg)
    while link == "":
        print("Link cannot be set to nothing. Please try entering a valid link.")
        link = input(msg)

if not excluded_times:
    msg = "Please list out the times of sections that should be excluded (separated by comma): "
    excluded_times = list(map(lambda x: x.strip() if x != '' else None, input(msg).split(",")))
    excluded_times = [x for x in excluded_times if x is not None]
    print(f'Here are the excluded times {excluded_times}')

if not excluded_sections:
    msg = "If there are any, list out any unique numbers you'd like to exclude (separated by comma): "
    excluded_sections = list(map(lambda x: x.strip() if x != '' else None, input(msg).split(",")))
    excluded_sections = [x for x in excluded_sections if x is not None]
    print(f'Here are the excluded sections {excluded_sections}')


def get_unique_numbers(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

    # May need to update the way we get these
    rows = driver.find_elements(By.TAG_NAME, "tr")
    return rows


def write_to_file(content):
    file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
    print(f'Writing files to {file_name}')
    file = open(f'../changes/{file_name}.txt', 'w')
    file.write(content)
    print("Modifications written to file")
    file.close()


def interact_with_test_env():
    print("Initializing web driver")
    driver = webdriver.Chrome()
    print("Web driver initialized, opening chrome")
    driver.get(link)

    flowchart = get_unique_numbers(driver)

    number_of_elements = len(flowchart)
    element_idx = 0

    modifications = 'Beep Boop Boop Bop\n\nHere are all the unique numbers iterated on:'

    '''
    Previously I was running a for loop over the elements that I had in this flowChart list 
    but when I did that I kept getting the staleElementError. I am not 100% sure why this was 
    happening, because even though I was running the for loop I was refreshing the flowchart 
    elements after each iteration.  
    '''
    while number_of_elements != element_idx:
        valid = True
        # TODO: May need to update this reference
        curr_row = flowchart[element_idx].find_elements(By.TAG_NAME, 'td')
        if (len(curr_row) == 0):
            # This row is the first row and should be skipped
            print("Skipping the first row")
            element_idx += 1
            continue
        unique_num = flowchart[element_idx].find_element(By.TAG_NAME, 'a')
        curr_unique_num = unique_num.text
        curr_time = curr_row[1].text

        # Note that this method is currently disregarding the day and only looking at the time
        for time in excluded_times:
            if time in curr_time:
                modifications += f'\n\t{curr_unique_num} : Excluded - section time {curr_time}'
                valid = False
                element_idx += 1
                break

        if curr_unique_num in excluded_sections:
            valid = False
            modifications += f'\n\t{curr_unique_num} : Excluded - unique number {curr_unique_num}'
            element_idx += 1

        if "Section" in curr_unique_num:
            valid = False
            element_idx += 1

        if valid:
            #  Navigate to new page
            unique_num.click()

            # Wait for the new page to show up, may need more time here
            # TODO: Update setSeatNumber reference, text_input, and submit_button
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "totalSeats")))
            edit_button = driver.find_element(By.ID, "totalSeats").find_element(By.TAG_NAME, "button")
            edit_button.click()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "totalSeatsForm")))
            text_input = driver.find_element(By.ID, "seatsInput")
            submit_button = driver.find_element(By.TAG_NAME, "button")
            text_input.clear()
            text_input.send_keys(seat_number)
            submit_button.click()
            modifications += f'\n\t{curr_unique_num} : Modified - number of seats changed to {seat_number}'

            # Move onto the next element
            element_idx += 1

            # TODO: Update wait statements
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))
            flowchart = get_unique_numbers(driver)

    modifications += f'\n\nThe bot ran with the following parameters:\
    \n\t-> Excluded times: {excluded_times}\
    \n\t-> Excluded sections: {excluded_sections}'
    print(modifications)

    write_to_file(modifications)
    driver.quit()

def interact_with_live_env():
    print("Initializing web driver")
    driver = webdriver.Chrome()
    print("Web driver initialized, opening chrome")
    driver.get(link)
    input("Enter any key once you have finished logging in")
    flowchart = get_unique_numbers(driver)

    number_of_elements = len(flowchart)
    element_idx = 0

    modifications = 'Beep Boop Boop Bop\n\nHere are all the unique numbers iterated on:'

    '''
    Previously I was running a for loop over the elements that I had in this flowChart list 
    but when I did that I kept getting the staleElementError. I am not 100% sure why this was 
    happening, because even though I was running the for loop I was refreshing the flowchart 
    elements after each iteration.  
    '''
    while number_of_elements != element_idx:
        valid = True
        curr_row = flowchart[element_idx].find_elements(By.TAG_NAME, 'td')
        if (len(curr_row) == 0):
            print("Skipping the header row")
            element_idx += 1
            continue

        try:
            unique_num = flowchart[element_idx].find_element(By.TAG_NAME, 'a')
        except:
            print("Element with Tag name a not found; this must not be a correct row.")
            element_idx += 1
            continue
        curr_unique_num = unique_num.text
        curr_time = curr_row[1].text

        print(f'Modifying the current section: {curr_unique_num} {curr_time}')

        for time in excluded_times:
            if time.lower() in curr_time.lower():
                modifications += f'\n\t{curr_unique_num} : Excluded - section time {curr_time}'
                valid = False
                element_idx += 1
                break

        if curr_unique_num in excluded_sections:
            valid = False
            modifications += f'\n\t{curr_unique_num} : Excluded - unique number {curr_unique_num}'
            element_idx += 1

        if "Section" in curr_unique_num:
            valid = False
            element_idx += 1

        if valid:
            #  Navigate to new page
            unique_num.click()

            # Wait for the new page to show up
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "totalSeats")))
            interact_with_specific_unique_number(driver)
            
            modifications += f'\n\t{curr_unique_num} : Modified - number of seats changed to {seat_number}'
            driver.back()
            driver.back()
            # Move onto the next element
            element_idx += 1
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))
            flowchart = get_unique_numbers(driver)

    modifications += f'\n\nThe bot ran with the following parameters:\
    \n\t-> Excluded times: {excluded_times}\
    \n\t-> Excluded sections: {excluded_sections}'
    print(modifications)

    write_to_file(modifications)
    driver.quit()


def interact_with_specific_unique_number(driver):
    seat_limit_div = driver.find_element(By.ID, "totalSeats")
    edit_btn = seat_limit_div.find_element(By.TAG_NAME, "button")
    edit_btn.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "totalSeatsForm")))

    seat_form = driver.find_element(By.ID, "totalSeatsForm")
    text_input = seat_form.find_element(By.ID, "seatsInput")
    submit_button = seat_form.find_element(By.CLASS_NAME, "seats-btn")
    
    text_input.clear()
    text_input.send_keys(seat_number)
    submit_button.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "totalSeats")))


def main():
    interact_with_test_env()
    # interact_with_live_env()


main()
