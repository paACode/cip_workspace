from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (e.g., for Chrome)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

try:
    # Wait for the confirmation box to appear and click "ablehnen"
    wait = WebDriverWait(driver, 2)
    ablehnen_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[div[contains(text(), 'Alle ablehnen')]]")))
    ablehnen_button.click()
    
    # Now the page should be loaded without the confirmation
except Exception as e:
    print(f"An error occurred: {e}")

# Do other tasks...

# find element
textarea = driver.find_element(By.ID, "APjFqb")
# Write to the textarea

textarea.send_keys('Your text here')

# Hit Enter
textarea.send_keys(Keys.RETURN)
driver.quit()


