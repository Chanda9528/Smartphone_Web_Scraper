from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=option, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.flipkart.com/search?q=smartphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=smartphone&requestId=64f3b9f0-75ae-4ed7-a014-2321ebcff667')


# Apply the filter
filter_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[3]/div[1]/div[1]/div/div[1]/div/section[7]/div[2]/div/div[1]/div/label/div[2]'))
)
filter_button.click()

page_number = 1

while True:
    try:
        # Save the HTML source of the current page
        html = driver.page_source
        with open(f"smartphone_page_{page_number}.html", 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Page {page_number} HTML saved.")

        # Wait for the "Next" button to be clickable and click it
        driver.find_element(by=By.XPATH,value='/html/body/div/div/div[3]/div/div[2]/div[26]/div/div/nav/a[11]').click()

        # Allow time for the new page to load
        time.sleep(2)
        page_number += 1
    except Exception as e:
        print(f"Error: {e}")
        break


